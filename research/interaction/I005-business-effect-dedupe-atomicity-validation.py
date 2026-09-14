import json, os, shutil, sqlite3, tempfile

ROOT = tempfile.mkdtemp(prefix="i005-atomicity-")
APP = os.path.join(ROOT, "app.db")
PROVIDER = os.path.join(ROOT, "provider.db")
CONSUMER = os.path.join(ROOT, "consumer.db")

ASSERTIONS = []

def check(name, condition, detail=None):
    ASSERTIONS.append({"name": name, "pass": bool(condition), "detail": detail})
    if not condition:
        raise AssertionError(name)

def init_all():
    for path in (APP, PROVIDER, CONSUMER):
        if os.path.exists(path):
            os.remove(path)
    db = sqlite3.connect(APP)
    db.executescript("""
    create table effects(id integer primary key autoincrement, op_key text, payload text);
    create table dedupe(op_key text primary key, effect_id integer, payload text);
    create table business(id text primary key, state text);
    create table outbox(msg_id text primary key, aggregate_id text, payload text, sent integer default 0);
    """)
    db.commit(); db.close()

    db = sqlite3.connect(PROVIDER)
    db.executescript("""
    create table effects(id integer primary key autoincrement, op_key text, payload text);
    create table idempotency(op_key text primary key, effect_id integer, payload text);
    """)
    db.commit(); db.close()

    db = sqlite3.connect(CONSUMER)
    db.executescript("""
    create table effects(id integer primary key autoincrement, msg_id text, payload text);
    create table inbox(msg_id text primary key);
    """)
    db.commit(); db.close()

def count(path, table):
    db = sqlite3.connect(path)
    value = db.execute(f"select count(*) from {table}").fetchone()[0]
    db.close()
    return value

def broken_first(op_key, payload):
    db = sqlite3.connect(APP)
    cur = db.execute("insert into effects(op_key,payload) values(?,?)", (op_key, payload))
    effect_id = cur.lastrowid
    db.commit(); db.close()
    return effect_id  # simulated crash before dedupe insert

def broken_retry(op_key, payload):
    db = sqlite3.connect(APP)
    row = db.execute("select effect_id from dedupe where op_key=?", (op_key,)).fetchone()
    if row:
        db.close(); return row[0], "replay"
    cur = db.execute("insert into effects(op_key,payload) values(?,?)", (op_key, payload))
    effect_id = cur.lastrowid
    db.execute("insert into dedupe values(?,?,?)", (op_key, effect_id, payload))
    db.commit(); db.close()
    return effect_id, "new"

def atomic_apply(op_key, payload, crash_before_commit=False):
    db = sqlite3.connect(APP)
    try:
        db.execute("begin immediate")
        row = db.execute("select effect_id,payload from dedupe where op_key=?", (op_key,)).fetchone()
        if row:
            if row[1] != payload:
                db.rollback(); db.close(); return None, "mismatch"
            db.commit(); db.close(); return row[0], "replay"
        cur = db.execute("insert into effects(op_key,payload) values(?,?)", (op_key, payload))
        effect_id = cur.lastrowid
        db.execute("insert into dedupe values(?,?,?)", (op_key, effect_id, payload))
        if crash_before_commit:
            raise RuntimeError("simulated crash")
        db.commit(); db.close(); return effect_id, "new"
    except RuntimeError:
        db.rollback(); db.close(); return None, "crashed"

def provider_naive(payload):
    db = sqlite3.connect(PROVIDER)
    cur = db.execute("insert into effects(op_key,payload) values(NULL,?)", (payload,))
    effect_id = cur.lastrowid
    db.commit(); db.close(); return effect_id

def provider_idempotent(op_key, payload):
    db = sqlite3.connect(PROVIDER)
    db.execute("begin immediate")
    row = db.execute("select effect_id,payload from idempotency where op_key=?", (op_key,)).fetchone()
    if row:
        if row[1] != payload:
            db.rollback(); db.close(); return None, "mismatch"
        db.commit(); db.close(); return row[0], "replay"
    cur = db.execute("insert into effects(op_key,payload) values(?,?)", (op_key, payload))
    effect_id = cur.lastrowid
    db.execute("insert into idempotency values(?,?,?)", (op_key, effect_id, payload))
    db.commit(); db.close(); return effect_id, "new"

def local_seen(op_key):
    db = sqlite3.connect(APP)
    row = db.execute("select effect_id from dedupe where op_key=?", (op_key,)).fetchone()
    db.close(); return row

def local_record(op_key, effect_id, payload):
    db = sqlite3.connect(APP)
    db.execute("insert into dedupe values(?,?,?)", (op_key, effect_id, payload))
    db.commit(); db.close()

def business_outbox(crash=False):
    db = sqlite3.connect(APP)
    try:
        db.execute("begin immediate")
        db.execute("insert into business values('o1','created')")
        db.execute("insert into outbox(msg_id,aggregate_id,payload) values('m1','o1','notify')")
        if crash:
            raise RuntimeError("simulated crash")
        db.commit(); db.close(); return "committed"
    except RuntimeError:
        db.rollback(); db.close(); return "crashed"

def consumer_naive(msg_id, payload):
    db = sqlite3.connect(CONSUMER)
    db.execute("insert into effects(msg_id,payload) values(?,?)", (msg_id, payload))
    db.commit(); db.close()

def reset_consumer():
    os.remove(CONSUMER)
    db = sqlite3.connect(CONSUMER)
    db.executescript("create table effects(id integer primary key autoincrement,msg_id text,payload text); create table inbox(msg_id text primary key);")
    db.commit(); db.close()

def consumer_atomic(msg_id, payload, crash=False):
    db = sqlite3.connect(CONSUMER)
    try:
        db.execute("begin immediate")
        if db.execute("select 1 from inbox where msg_id=?", (msg_id,)).fetchone():
            db.commit(); db.close(); return "replay"
        db.execute("insert into effects(msg_id,payload) values(?,?)", (msg_id, payload))
        db.execute("insert into inbox values(?)", (msg_id,))
        if crash:
            raise RuntimeError("simulated crash")
        db.commit(); db.close(); return "new"
    except RuntimeError:
        db.rollback(); db.close(); return "crashed"

def run():
    init_all()
    e1 = broken_first("op1", "100")
    check("split_commit_first_effect_committed", count(APP,"effects") == 1)
    check("split_commit_ledger_missing_after_crash", count(APP,"dedupe") == 0)
    e2, mode = broken_retry("op1", "100")
    check("split_commit_retry_duplicates_effect", count(APP,"effects") == 2)
    check("split_commit_retry_created_new_effect", e2 != e1 and mode == "new")

    init_all()
    check("atomic_precommit_crash_rolls_back_effect", atomic_apply("op2","100",True) == (None,"crashed") and count(APP,"effects") == 0)
    check("atomic_precommit_crash_rolls_back_ledger", count(APP,"dedupe") == 0)
    a1, m1 = atomic_apply("op2","100")
    check("atomic_retry_commits_one_effect", m1 == "new" and count(APP,"effects") == 1 and count(APP,"dedupe") == 1)
    a2, m2 = atomic_apply("op2","100")
    check("atomic_postcommit_retry_replays_same_result", a2 == a1 and m2 == "replay")
    check("atomic_postcommit_retry_no_duplicate", count(APP,"effects") == 1)
    check("atomic_key_payload_mismatch_rejected", atomic_apply("op2","200")[1] == "mismatch" and count(APP,"effects") == 1)

    init_all()
    p1 = provider_naive("pay100")
    check("external_provider_effect_committed", count(PROVIDER,"effects") == 1)
    check("local_ledger_missing_after_external_success_crash", local_seen("pay-op") is None)
    p2 = provider_naive("pay100"); local_record("pay-op", p2, "pay100")
    check("external_retry_duplicates_without_provider_idempotency", count(PROVIDER,"effects") == 2)
    check("local_transaction_cannot_retroactively_merge_external_effects", p1 != p2 and count(APP,"dedupe") == 1)

    init_all()
    p1, m1 = provider_idempotent("pay-op","pay100")
    check("provider_idempotent_first_commits_once", m1 == "new" and count(PROVIDER,"effects") == 1)
    check("provider_success_can_exist_without_local_ledger", local_seen("pay-op") is None)
    p2, m2 = provider_idempotent("pay-op","pay100")
    check("provider_same_key_retry_replays", p2 == p1 and m2 == "replay")
    check("provider_same_key_retry_no_duplicate", count(PROVIDER,"effects") == 1)
    local_record("pay-op", p2, "pay100")
    check("local_reconciliation_records_provider_result", local_seen("pay-op")[0] == p1)

    init_all()
    check("outbox_precommit_crash_rolls_back_business", business_outbox(True) == "crashed" and count(APP,"business") == 0)
    check("outbox_precommit_crash_rolls_back_message", count(APP,"outbox") == 0)
    business_outbox(False)
    check("outbox_commit_persists_business_and_message", count(APP,"business") == 1 and count(APP,"outbox") == 1)
    consumer_naive("m1","notify"); consumer_naive("m1","notify")
    check("outbox_relay_can_duplicate_without_consumer_dedupe", count(CONSUMER,"effects") == 2)
    reset_consumer()
    check("consumer_atomic_precommit_crash_rolls_back_effect_and_inbox", consumer_atomic("m1","notify",True) == "crashed" and count(CONSUMER,"effects") == 0 and count(CONSUMER,"inbox") == 0)
    c1 = consumer_atomic("m1","notify"); c2 = consumer_atomic("m1","notify")
    check("consumer_inbox_retry_replays", c1 == "new" and c2 == "replay")
    check("consumer_inbox_prevents_duplicate_effect", count(CONSUMER,"effects") == 1 and count(CONSUMER,"inbox") == 1)

    return {"passed": sum(x["pass"] for x in ASSERTIONS), "total": len(ASSERTIONS), "all_pass": all(x["pass"] for x in ASSERTIONS), "assertions": ASSERTIONS}

if __name__ == "__main__":
    try:
        print(json.dumps(run(), indent=2))
    finally:
        shutil.rmtree(ROOT, ignore_errors=True)
