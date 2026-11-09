// SYNTHETIC RESEARCH ORACLE ONLY. No LogMate/Dart/Sembast execution or private corpus.
"use strict";
const assert=require("node:assert/strict"),clone=x=>JSON.parse(JSON.stringify(x));
const seed={owner:"A",flights:{F:{owner:"A",active:true,rev:4,block:85},G:{owner:"A",active:true,rev:4,block:95}},evidence:{},receipts:{}};
const base={owner:"A",id:"F",rev:4,head:null,date:true,year:true,subject:true,locator:true,matches:1,approved:true,blh:85,crew:["CC","FO"],source:"S1"};
// Closed-world, JSON-safe synthetic evidence request. This does NOT authenticate a real source.
const requestKeys=["owner","id","rev","head","date","year","subject","locator","matches","approved","blh","crew","source"];
const plain=x=>x!==null&&typeof x==="object"&&!Array.isArray(x)&&Object.getPrototypeOf(x)===Object.prototype;
const seal=(owner,id,seq,previous,snapshot)=>JSON.stringify({v:1,owner,id,seq,previous,snapshot});
const token=x=>typeof x==="string"&&x.length>0&&x.length<=64&&/^[A-Za-z0-9:_-]+$/.test(x);
function validRequest(r){
 if(!plain(r)||Object.keys(r).some(k=>!requestKeys.includes(k))||requestKeys.some(k=>!Object.hasOwn(r,k)))return false;
 if(!token(r.owner)||!token(r.id)||!Number.isSafeInteger(r.rev)||r.rev<0||!(r.head===null||token(r.head)))return false;
 for(const k of ["date","year","subject","locator","approved"])if(typeof r[k]!=="boolean")return false;
 if(!Number.isSafeInteger(r.matches)||r.matches<0||r.matches>100||!Number.isSafeInteger(r.blh)||r.blh<0||r.blh>1440)return false;
 if(!Array.isArray(r.crew)||r.crew.length<1||r.crew.length>20||r.crew.some(x=>!token(x)))return false;
 if(!token(r.source))return false;
 return true;
}

// Research policy variant: global fail-closed admission; NOT owner-approved product behavior.
function validPersisted(s,owner,id,p){
 if(p){
  if(!Number.isSafeInteger(p.seq)||p.seq<1||p.head!==owner+":"+id+":H"+p.seq||
     !plain(s.receipts[p.head])||s.receipts[p.head].owner!==owner||
     s.receipts[p.head].id!==id)return false;
  // Closed-world persisted head: never trust notice fields or caller-controlled extensions.
  const headKeys=["changedCrew","crew","head","seq","signature"];
  if(Object.keys(p).sort().join(",")!==headKeys.join(",")||
     typeof p.changedCrew!=="boolean"||!Array.isArray(p.crew)||
     p.crew.length<1||p.crew.length>20||!p.crew.every(token)||
     typeof p.signature!=="string")return false;
  // Verify the COMPLETE synthetic ancestry, not only the head. Deterministic seal is NOT cryptographic.
  let previous=null;
  for(let i=1;i<=p.seq;i++){
   const key=owner+":"+id+":H"+i,receipt=s.receipts[key];
   if(!plain(receipt)||Object.keys(receipt).sort().join(",")!=="id,owner,previous,seal,seq,snapshot"||
      receipt.owner!==owner||receipt.id!==id||receipt.seq!==i||
      receipt.previous!==previous||!plain(receipt.snapshot)||
      Object.keys(receipt.snapshot).sort().join(",")!=="blh,crew,source"||
      (!Number.isSafeInteger(receipt.snapshot.blh)||receipt.snapshot.blh<0||receipt.snapshot.blh>1440)||!Array.isArray(receipt.snapshot.crew)||receipt.snapshot.crew.length<1||receipt.snapshot.crew.length>20||
      !receipt.snapshot.crew.every(token)||!token(receipt.snapshot.source)||
      receipt.seal!==seal(owner,id,i,previous,receipt.snapshot))return false;
   previous=key;
  }
  const last=s.receipts[p.head].snapshot;
  const expectedCrewChanged=p.seq===1?false:
   JSON.stringify(s.receipts[owner+":"+id+":H"+(p.seq-1)].snapshot.crew)!==JSON.stringify(last.crew);
  if(p.signature!==JSON.stringify(last)||JSON.stringify(p.crew)!==JSON.stringify(last.crew)||
     p.changedCrew!==expectedCrewChanged)return false;
 }

 return true;
}
function apply(s,r,crash){
 const reject=x=>({code:x,state:s});
 if(!validRequest(r))return reject("SCHEMA");
 const f=s.flights[r.id],p=s.evidence[r.id];
 if(r.owner!==s.owner||!f||f.owner!==r.owner||!f.active)return reject("OWNER");
 if(r.rev!==f.rev)return reject("FLIGHT_CAS");
 if(r.head!==(p?.head??null))return reject("EVIDENCE_CAS");
 // Existing evidence must point to a real, owner/flight-bound receipt with a coherent sequence.
 // This is a synthetic invariant only; it does not prove actual durable storage.
 if(!validPersisted(s,r.owner,r.id,p))return reject("RECEIPT_CHAIN");
 // Validate every foreign evidence head and its entire sealed ancestry before committing F.
 if(!plain(s.evidence)||!plain(s.receipts))return reject("RECEIPT_CHAIN");
 for(const [id,foreign] of Object.entries(s.evidence)){
  if(!token(id)||!s.flights[id]||s.flights[id].owner!==s.owner||!validPersisted(s,s.owner,id,foreign))return reject("RECEIPT_CHAIN");
 }
 // A foreign-owner or orphan receipt is not acceptable in this research state.
 for(const [key,receipt] of Object.entries(s.receipts)){
  if(!plain(receipt)||Object.keys(receipt).sort().join(",")!=="id,owner,previous,seal,seq,snapshot"||
     !Number.isSafeInteger(receipt.seq)||receipt.seq<1||receipt.owner!==s.owner||!s.flights[receipt.id]||
     receipt.owner!==s.flights[receipt.id].owner||
     key!==receipt.owner+":"+receipt.id+":H"+receipt.seq||
     !s.evidence[receipt.id]||receipt.seq>s.evidence[receipt.id].seq)return reject("RECEIPT_CHAIN");
 }
 if(!r.date||!r.year||!r.subject||!r.locator)return reject("AUTH");
 if(r.matches!==1)return reject("MATCH");
 if(!r.approved)return reject("REVIEW");
 const n=clone(s),snapshot={blh:r.blh,crew:clone(r.crew),source:r.source};
 if(p?.signature===JSON.stringify(snapshot))return reject("REPLAY");
 const head=r.owner+":"+r.id+":H"+((p?.seq??0)+1);
 if(n.receipts[head])return reject("RECEIPT_CONFLICT");
 n.evidence[r.id]={head,seq:(p?.seq??0)+1,signature:JSON.stringify(snapshot),changedCrew:!!p&&JSON.stringify(p.crew)!==JSON.stringify(r.crew),crew:clone(r.crew)};
 if(crash==="evidence")return reject("ROLLBACK");
 n.receipts[head]={owner:r.owner,id:r.id,seq:(p?.seq??0)+1,previous:p?.head??null,snapshot,seal:seal(r.owner,r.id,(p?.seq??0)+1,p?.head??null,snapshot)};
 if(crash==="receipt")return reject("ROLLBACK");
 assert.deepEqual(n.flights,s.flights,"canonical FlightRecord mutation");
 return{code:"COMMIT",state:n};
}
const committed=apply(seed,base).state;
const cases=[
 ["accept",seed,base,null,"COMMIT"],["replay",committed,{...base,head:"A:F:H1"},null,"REPLAY"],
 ["changed-crew",committed,{...base,head:"A:F:H1",crew:["CC","CA"],source:"S2"},null,"COMMIT"],
 ["flight-cas",seed,{...base,rev:3},null,"FLIGHT_CAS"],["evidence-cas",committed,base,null,"EVIDENCE_CAS"],
 ["wrong-owner",seed,{...base,owner:"B"},null,"OWNER"],["missing-flight",seed,{...base,id:"X"},null,"OWNER"],
 ["inactive",{...seed,flights:{F:{...seed.flights.F,active:false}}},base,null,"OWNER"],
 ["no-date",seed,{...base,date:false},null,"AUTH"],["no-year",seed,{...base,year:false},null,"AUTH"],
 ["no-subject",seed,{...base,subject:false},null,"AUTH"],["no-locator",seed,{...base,locator:false},null,"AUTH"],
 ["ambiguous",seed,{...base,matches:2},null,"MATCH"],["unmatched",seed,{...base,matches:0},null,"MATCH"],
 ["no-review",seed,{...base,approved:false},null,"REVIEW"],["employee",seed,{...base,employee:"synthetic"},null,"SCHEMA"],
 ["raw-pdf",seed,{...base,pdf:"synthetic"},null,"SCHEMA"],["inferred-date",seed,{...base,inferredDate:true},null,"SCHEMA"],
 ["inferred-role",seed,{...base,inferredRole:true},null,"SCHEMA"],
 ["crash-after-evidence",seed,base,"evidence","ROLLBACK"],["crash-after-receipt",seed,base,"receipt","ROLLBACK"],
 ["new-owner",{owner:"B",flights:{},evidence:{},receipts:{}},base,null,"OWNER"]
];
for(const [name,s,r,crash,expected] of cases){const x=apply(s,r,crash);assert.equal(x.code,expected,name);if(x.code!=="COMMIT")assert.equal(x.state,s,name+" must not mutate original");}
// Cross-flight receipt collision regression: original global H1 overwrote F receipt when G first attached.
const twoFlights=apply(committed,{...base,id:"G"});
assert.equal(twoFlights.code,"COMMIT");
assert.equal(twoFlights.state.evidence.F.head,"A:F:H1");
assert.equal(twoFlights.state.evidence.G.head,"A:G:H1");
assert.equal(twoFlights.state.receipts["A:F:H1"].owner,"A");assert.equal(twoFlights.state.receipts["A:F:H1"].id,"F");
assert.equal(twoFlights.state.receipts["A:G:H1"].owner,"A");assert.equal(twoFlights.state.receipts["A:G:H1"].id,"G");
assert.equal(Object.keys(twoFlights.state.receipts).length,2);
const tampered=clone(committed);
tampered.receipts["A:F:H2"]={owner:"A",id:"G"};
const conflict=apply(tampered,{...base,head:"A:F:H1",crew:["CC","CA"],source:"S2"});
assert.equal(conflict.code,"RECEIPT_CHAIN");
assert.equal(conflict.state,tampered);
const changed=apply(committed,{...base,head:"A:F:H1",crew:["CC","CA"],source:"S2"});
assert.equal(changed.state.evidence.F.changedCrew,true);assert.equal(changed.state.flights.F.block,85);

// Independent synthetic schema regression: eight previously COMMIT-accepted malformed inputs
// plus 16 adjacent type/privacy/adversarial boundary cases. No real roster payloads.
const malformed=[
 ["missing-crew",{crew:undefined}],["crew-object",{crew:{role:"CC"}}],["empty-crew",{crew:[]}],
 ["missing-source",{source:undefined}],["missing-blh",{blh:undefined}],["string-blh",{blh:"85"}],
 ["nested-employee",{crew:[{employee:"synthetic"}]}],["nested-pdf",{source:{pdf:"synthetic"}}],
 ["extra-nested",{extra:{nested:{employee:"synthetic"}}}],["crew-null",{crew:null}],
 ["source-array",{source:["S1"]}],["crew-array-with-object",{crew:["CC",{role:"FO"}]}],
 ["crew-undefined-element",{crew:["CC",undefined]}],["date-string",{date:"true"}],
 ["matches-string",{matches:"1"}],["blh-negative",{blh:-1}],["blh-nan",{blh:NaN}],
 ["blh-infinity",{blh:Infinity}],["source-empty",{source:""}],
 ["head-object",{head:{receipt:"A:F:H1"}}],
 ["proto-field",Object.assign(Object.create(null),base)],
 ["unrecognized-hash",{sourceHash:"synthetic"}],["unknown-revision",{publication:"unknown"}],
 ["crew-too-many",{crew:Array(21).fill("CC")}]
];
for(const [name,changes] of malformed){
 const request=name==="proto-field"?changes:{...base,...changes};
 const result=apply(seed,request);
 assert.equal(result.code,"SCHEMA",name);
 assert.equal(result.state,seed,name+" must not mutate original");
}
// Previously admitted tampered/missing/forged receipt ancestry; all must fail closed.
const ancestryCases=[
 ["missing-receipt",x=>{delete x.receipts["A:F:H1"];}],
 ["wrong-flight-receipt",x=>{x.receipts["A:F:H1"].id="G";}],
 ["wrong-owner-receipt",x=>{x.receipts["A:F:H1"].owner="B";}],
 ["wrong-head-sequence",x=>{x.evidence.F.head="A:F:H999";}],
 ["negative-sequence",x=>{x.evidence.F.seq=-1;}],
 ["fractional-sequence",x=>{x.evidence.F.seq=1.5;}]
];
for(const [name,mutate] of ancestryCases){
 const state=clone(committed);mutate(state);
 const req={...base,head:state.evidence.F.head,crew:["CC","CA"],source:"S2"};
 const out=apply(state,req);
 assert.equal(out.code,"RECEIPT_CHAIN",name);
 assert.equal(out.state,state,name+" no mutation");
}
// New integrity regressions: source, crew, prior seal, unbound fields, missing ancestry and orphan receipts.
const integrityCases=[
 ["prior-seal",x=>{x.receipts["A:F:H1"].seal="forged";}],
 ["prior-crew",x=>{x.receipts["A:F:H1"].snapshot.crew=["FO"]; }],
 ["prior-source",x=>{x.receipts["A:F:H1"].snapshot.source="S3";}],
 ["extra-receipt-field",x=>{x.receipts["A:F:H1"].employee="synthetic";}],
 ["orphan-foreign-owner",x=>{x.receipts["B:Z:H1"]={owner:"B",id:"Z",seq:1};}],
 ["head-snapshot",x=>{x.evidence.F.crew=["CA"]; }],
 ["head-signature",x=>{x.evidence.F.signature="forged";}],
 ["missing-ancestor",x=>{const next=apply(x,{...base,head:"A:F:H1",crew:["CC","CA"],source:"S2"});assert.equal(next.code,"COMMIT");Object.assign(x,next.state);delete x.receipts["A:F:H1"];}]
];
for(const [name,mutate] of integrityCases){
 const state=clone(committed);mutate(state);
 const out=apply(state,{...base,head:state.evidence.F.head,crew:["CC","CA"],source:"S3"});
 assert.equal(out.code,"RECEIPT_CHAIN",name);
 assert.equal(out.state,state,name+" no mutation");
}

// Persisted-state adversarial regressions (independent of request validation).
const persistedMutations=[
 ["forged-changed-crew",x=>{x.evidence.F.changedCrew=true;}],
 ["nested-changed-crew",x=>{x.evidence.F.changedCrew={flag:false};}],
 ["staff-id-extension",x=>{x.evidence.F.employee="synthetic";}],
 ["unexpected-provenance-extension",x=>{x.evidence.F.rawPdf="synthetic";}],
 ["missing-notice",x=>{delete x.evidence.F.changedCrew;}],
 ["crew-nested-object",x=>{x.evidence.F.crew=[{employee:"synthetic"}];}],
 ["crew-empty",x=>{x.evidence.F.crew=[];}],
 ["signature-type",x=>{x.evidence.F.signature={value:"synthetic"};}]
];
for(const [name,mutate] of persistedMutations){
 const state=clone(committed);mutate(state);
 const out=apply(state,{...base,head:"A:F:H1",crew:["CC","CA"],source:"S2"});
 assert.equal(out.code,"RECEIPT_CHAIN",name);
 assert.equal(out.state,state,name+" zero mutation");
}
const second=apply(committed,{...base,head:"A:F:H1",crew:["CC","CA"],source:"S2"});
assert.equal(second.code,"COMMIT");
const forgedSecond=clone(second.state);forgedSecond.evidence.F.changedCrew=false;
assert.equal(apply(forgedSecond,{...base,head:"A:F:H2",crew:["CC","FO"],source:"S3"}).code,"RECEIPT_CHAIN");
const sameCrew=apply(committed,{...base,head:"A:F:H1",source:"S2"});
assert.equal(sameCrew.code,"COMMIT");
assert.equal(sameCrew.state.evidence.F.changedCrew,false);
assert.equal(apply(sameCrew.state,{...base,head:"A:F:H2",source:"S3"}).code,"COMMIT");


// Closed-world ancestor snapshot checks: synthetic malformed receipts must fail closed.
const malformedAncestorSnapshots=[
 ["negative-blh",x=>{x.blh=-1;}],["overlimit-blh",x=>{x.blh=1441;}],
 ["empty-crew",x=>{x.crew=[];}],["overlimit-crew",x=>{x.crew=Array(21).fill("CC");}]
];
for(const [name,mutate] of malformedAncestorSnapshots){
 const state=clone(committed),receipt=state.receipts["A:F:H1"];
 mutate(receipt.snapshot);receipt.seal=seal("A","F",1,null,receipt.snapshot);
 state.evidence.F.signature=JSON.stringify(receipt.snapshot);
 state.evidence.F.crew=clone(receipt.snapshot.crew);
 const out=apply(state,{...base,head:"A:F:H1",crew:["CC","CA"],source:"S2"});
 assert.equal(out.code,"RECEIPT_CHAIN",name);
 assert.equal(out.state,state,name+" zero writes");
}
for(const [name,mutate] of malformedAncestorSnapshots){
 const state=clone(second.state),receipt=state.receipts["A:F:H1"];
 mutate(receipt.snapshot);receipt.seal=seal("A","F",1,null,receipt.snapshot);
 const out=apply(state,{...base,head:"A:F:H2",crew:["CC","FO"],source:"S3"});
 assert.equal(out.code,"RECEIPT_CHAIN","ancestor-"+name);
 assert.equal(out.state,state,"ancestor-"+name+" zero writes");
}
// Cross-flight global fail-closed research variant (not a product decision).
const foreignBase=twoFlights.state;
const foreignMutations=[
 ["foreign-signature",x=>{x.evidence.G.signature="forged";}],
 ["foreign-crew",x=>{x.evidence.G.crew=["FAKE"]; }],
 ["foreign-notice",x=>{x.evidence.G.changedCrew=true;}],
 ["foreign-head-extra",x=>{x.evidence.G.staff="forbidden";}],
 ["foreign-ancestor-blh",x=>{x.receipts["A:G:H1"].snapshot.blh=1441;}],
 ["foreign-ancestor-crew",x=>{x.receipts["A:G:H1"].snapshot.crew=[];}],
 ["foreign-seal",x=>{x.receipts["A:G:H1"].seal="forged";}]
];
for(const [name,mutate] of foreignMutations){const state=clone(foreignBase);mutate(state);const out=apply(state,{...base,head:"A:F:H1",source:"S2"});assert.equal(out.code,"RECEIPT_CHAIN",name);assert.deepEqual(out.state,state,name+" zero writes");}
assert.equal(apply(foreignBase,{...base,head:"A:F:H1",source:"S2"}).code,"COMMIT","healthy cross-flight");
// Extra receipt admission: reject out-of-range, malformed, foreign and noncontiguous receipt inventory.
const extraReceiptMutations=[
 ["zero-seq",x=>{x.receipts["A:F:H0"]={...clone(x.receipts["A:F:H1"]),seq:0};}],
 ["negative-seq",x=>{x.receipts["A:F:H-1"]={...clone(x.receipts["A:F:H1"]),seq:-1};}],
 ["fractional-seq",x=>{x.receipts["A:F:H0.5"]={...clone(x.receipts["A:F:H1"]),seq:0.5};}],
 ["forbidden-field",x=>{x.receipts["A:F:H0"]={...clone(x.receipts["A:F:H1"]),seq:0,extra:"synthetic"};}],
 ["extra-after-head",x=>{x.receipts["A:F:H2"]={...clone(x.receipts["A:F:H1"]),seq:2};}],
 ["foreign-uid",x=>{x.receipts["B:F:H0"]={...clone(x.receipts["A:F:H1"]),owner:"B",seq:0};}],
 ["missing-evidence",x=>{x.receipts["A:G:H1"]={...clone(x.receipts["A:F:H1"]),id:"G"};}]
];
for(const [name,mutate] of extraReceiptMutations){
 const state=clone(committed);mutate(state);
 const before=clone(state),out=apply(state,{...base,head:"A:F:H1",source:"S2"});
 assert.equal(out.code,"RECEIPT_CHAIN",name);assert.deepEqual(out.state,before,name+" zero writes");
}
assert.equal(apply(committed,{...base,head:"A:F:H1",source:"S2"}).code,"COMMIT","healthy existing receipt inventory");
// Input/output isolation regression: commit must never retain caller-owned mutable arrays.
const isolatedRequest=clone(base), isolatedCommit=apply(seed,isolatedRequest);
assert.equal(isolatedCommit.code,"COMMIT");
const isolatedSnapshot=clone(isolatedCommit.state.receipts["A:F:H1"].snapshot);
isolatedRequest.crew[0]="MUTATED";
assert.deepEqual(isolatedCommit.state.receipts["A:F:H1"].snapshot,isolatedSnapshot,"caller mutation must not change receipt");
assert.deepEqual(isolatedCommit.state.evidence.F.crew,isolatedSnapshot.crew,"caller mutation must not change evidence");
// Evidence and receipt must not share a mutable array even inside a committed result.
isolatedCommit.state.evidence.F.crew[0]="MUTATED";
assert.deepEqual(isolatedCommit.state.receipts["A:F:H1"].snapshot,isolatedSnapshot,"evidence mutation must not change receipt");
// Existing state must not be mutated by a later accepted update.
const oldState=clone(committed), oldCopy=clone(oldState);
const later=apply(oldState,{...base,head:"A:F:H1",crew:["CC","CA"],source:"S2"});
assert.equal(later.code,"COMMIT");
assert.deepEqual(oldState,oldCopy,"prior state remains unchanged");
console.log(JSON.stringify({kind:"SYNTHETIC_RESEARCH_ORACLE",legacyCases:cases.length,receiptRegressions:2,negativeSchemaCases:malformed.length,receiptAncestryCases:ancestryCases.length,integrityCases:integrityCases.length,persistedStateCases:persistedMutations.length+4,isolationCases:3,malformedAncestorCases:8,crossFlightCases:8,extraReceiptCases:extraReceiptMutations.length+1,passed:cases.length+2+malformed.length+ancestryCases.length+integrityCases.length+persistedMutations.length+4+3+8+8+extraReceiptMutations.length+1,total:cases.length+2+malformed.length+ancestryCases.length+integrityCases.length+persistedMutations.length+4+3+8+8+extraReceiptMutations.length+1,production:false}));
