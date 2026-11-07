// SYNTHETIC RESEARCH ORACLE ONLY. No LogMate/Dart/Sembast execution or private corpus.
"use strict";
const assert=require("node:assert/strict"),clone=x=>JSON.parse(JSON.stringify(x));
const seed={owner:"A",flights:{F:{owner:"A",active:true,rev:4,block:85}},evidence:{},receipts:{}};
const base={owner:"A",id:"F",rev:4,head:null,date:true,year:true,subject:true,locator:true,matches:1,approved:true,blh:85,crew:["CC","FO"],source:"S1"};
function apply(s,r,crash){
 const f=s.flights[r.id],p=s.evidence[r.id],reject=x=>({code:x,state:s});
 if(r.owner!==s.owner||!f||f.owner!==r.owner||!f.active)return reject("OWNER");
 if(r.rev!==f.rev)return reject("FLIGHT_CAS");
 if(r.head!==(p?.head??null))return reject("EVIDENCE_CAS");
 if(!r.date||!r.year||!r.subject||!r.locator)return reject("AUTH");
 if(r.matches!==1)return reject("MATCH");
 if(!r.approved)return reject("REVIEW");
 if(r.employee||r.pdf||r.inferredDate||r.inferredRole)return reject("PRIVACY");
 const n=clone(s),snapshot={blh:r.blh,crew:r.crew,source:r.source};
 if(p?.signature===JSON.stringify(snapshot))return reject("REPLAY");
 const head="H"+((p?.seq??0)+1);
 n.evidence[r.id]={head,seq:(p?.seq??0)+1,signature:JSON.stringify(snapshot),changedCrew:!!p&&JSON.stringify(p.crew)!==JSON.stringify(r.crew),crew:r.crew};
 if(crash==="evidence")return reject("ROLLBACK");
 n.receipts[head]={owner:r.owner,id:r.id};
 if(crash==="receipt")return reject("ROLLBACK");
 assert.deepEqual(n.flights,s.flights,"canonical FlightRecord mutation");
 return{code:"COMMIT",state:n};
}
const committed=apply(seed,base).state;
const cases=[
 ["accept",seed,base,null,"COMMIT"],["replay",committed,{...base,head:"H1"},null,"REPLAY"],
 ["changed-crew",committed,{...base,head:"H1",crew:["CC","CA"],source:"S2"},null,"COMMIT"],
 ["flight-cas",seed,{...base,rev:3},null,"FLIGHT_CAS"],["evidence-cas",committed,base,null,"EVIDENCE_CAS"],
 ["wrong-owner",seed,{...base,owner:"B"},null,"OWNER"],["missing-flight",seed,{...base,id:"X"},null,"OWNER"],
 ["inactive",{...seed,flights:{F:{...seed.flights.F,active:false}}},base,null,"OWNER"],
 ["no-date",seed,{...base,date:false},null,"AUTH"],["no-year",seed,{...base,year:false},null,"AUTH"],
 ["no-subject",seed,{...base,subject:false},null,"AUTH"],["no-locator",seed,{...base,locator:false},null,"AUTH"],
 ["ambiguous",seed,{...base,matches:2},null,"MATCH"],["unmatched",seed,{...base,matches:0},null,"MATCH"],
 ["no-review",seed,{...base,approved:false},null,"REVIEW"],["employee",seed,{...base,employee:"synthetic"},null,"PRIVACY"],
 ["raw-pdf",seed,{...base,pdf:"synthetic"},null,"PRIVACY"],["inferred-date",seed,{...base,inferredDate:true},null,"PRIVACY"],
 ["inferred-role",seed,{...base,inferredRole:true},null,"PRIVACY"],
 ["crash-after-evidence",seed,base,"evidence","ROLLBACK"],["crash-after-receipt",seed,base,"receipt","ROLLBACK"],
 ["new-owner",{owner:"B",flights:{},evidence:{},receipts:{}},base,null,"OWNER"]
];
for(const [name,s,r,crash,expected] of cases){const x=apply(s,r,crash);assert.equal(x.code,expected,name);if(x.code!=="COMMIT")assert.equal(x.state,s,name+" must not mutate original");}
const changed=apply(committed,{...base,head:"H1",crew:["CC","CA"],source:"S2"});
assert.equal(changed.state.evidence.F.changedCrew,true);assert.equal(changed.state.flights.F.block,85);
console.log(JSON.stringify({kind:"SYNTHETIC_RESEARCH_ORACLE",passed:cases.length,total:cases.length,production:false}));
