// SYNTHETIC RESEARCH ORACLE ONLY. No LogMate/Dart/Sembast execution or private corpus.
"use strict";
const assert=require("node:assert/strict"),clone=x=>JSON.parse(JSON.stringify(x));
const seed={owner:"A",flights:{F:{owner:"A",active:true,rev:4,block:85},G:{owner:"A",active:true,rev:4,block:95}},evidence:{},receipts:{}};
const base={owner:"A",id:"F",rev:4,head:null,date:true,year:true,subject:true,locator:true,matches:1,approved:true,blh:85,crew:["CC","FO"],source:"S1"};
// Closed-world, JSON-safe synthetic evidence request. This does NOT authenticate a real source.
const requestKeys=["owner","id","rev","head","date","year","subject","locator","matches","approved","blh","crew","source"];
const plain=x=>x!==null&&typeof x==="object"&&!Array.isArray(x)&&Object.getPrototypeOf(x)===Object.prototype;
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
function apply(s,r,crash){
 const reject=x=>({code:x,state:s});
 if(!validRequest(r))return reject("SCHEMA");
 const f=s.flights[r.id],p=s.evidence[r.id];
 if(r.owner!==s.owner||!f||f.owner!==r.owner||!f.active)return reject("OWNER");
 if(r.rev!==f.rev)return reject("FLIGHT_CAS");
 if(r.head!==(p?.head??null))return reject("EVIDENCE_CAS");
 if(!r.date||!r.year||!r.subject||!r.locator)return reject("AUTH");
 if(r.matches!==1)return reject("MATCH");
 if(!r.approved)return reject("REVIEW");
 const n=clone(s),snapshot={blh:r.blh,crew:r.crew,source:r.source};
 if(p?.signature===JSON.stringify(snapshot))return reject("REPLAY");
 const head=r.owner+":"+r.id+":H"+((p?.seq??0)+1);
 if(n.receipts[head])return reject("RECEIPT_CONFLICT");
 n.evidence[r.id]={head,seq:(p?.seq??0)+1,signature:JSON.stringify(snapshot),changedCrew:!!p&&JSON.stringify(p.crew)!==JSON.stringify(r.crew),crew:r.crew};
 if(crash==="evidence")return reject("ROLLBACK");
 n.receipts[head]={owner:r.owner,id:r.id};
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
assert.deepEqual(twoFlights.state.receipts["A:F:H1"],{owner:"A",id:"F"});
assert.deepEqual(twoFlights.state.receipts["A:G:H1"],{owner:"A",id:"G"});
assert.equal(Object.keys(twoFlights.state.receipts).length,2);
const tampered=clone(committed);
tampered.receipts["A:F:H2"]={owner:"A",id:"G"};
const conflict=apply(tampered,{...base,head:"A:F:H1",crew:["CC","CA"],source:"S2"});
assert.equal(conflict.code,"RECEIPT_CONFLICT");
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
console.log(JSON.stringify({kind:"SYNTHETIC_RESEARCH_ORACLE",legacyCases:cases.length,receiptRegressions:2,negativeSchemaCases:malformed.length,passed:cases.length+2+malformed.length,total:cases.length+2+malformed.length,production:false}));
