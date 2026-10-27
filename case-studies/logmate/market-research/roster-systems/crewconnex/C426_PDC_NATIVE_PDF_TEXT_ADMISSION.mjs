// C426: research-only PDC PDF native text-layer admission oracle.
// Verified only against one private, uncompressed, single-page August 2026 PDF.
// NO private names, IDs, routes, flight numbers, clocks or original cells embedded/returned.
// Not production PDF parser; no FlightRecord creation, UID/Publication/century proof.
const HEADERS=["Date","Pairing","DC","C/I (L)","C/O (L)","Activity","From","STD (L)","STD (B)","To","STA (L)","STA (B)","AC/Hotel","Blk Hrs"];
const HX=[75,109,143,162,186,210,244,268,292,316,340,364,388,492],BX=[81,109,143,162,186,210,244,268,292,316,340,364,388,511],BC=[31,22,1,16,16,48,44,48,48,44,48,48,33,26];
function fromBase64(s){const A="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",v={};for(let i=0;i<64;i++)v[A[i]]=i;let out=[],acc=0,bits=0;for(const c of s){if(c==="=")break;const k=v[c];if(k===undefined)continue;acc=((acc<<6)|k)&0xffffff;bits+=6;if(bits>=8){bits-=8;out.push((acc>>bits)&255)}}return String.fromCharCode(...out);}
function toBase64(s){const A="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",out=[];for(let i=0;i<s.length;i+=3){const n=(s.charCodeAt(i)<<16)|((s.charCodeAt(i+1)||0)<<8)|(s.charCodeAt(i+2)||0);out.push(A[(n>>>18)&63]+A[(n>>>12)&63]+(i+1<s.length?A[(n>>>6)&63]:"=")+(i+2<s.length?A[n&63]:"="));}return out.join("");}
const unesc=s=>s.replace(/\\([()\\])/g,"$1").replace(/\\n/g,"\n").replace(/\\r/g,"\r").replace(/\\t/g,"\t");
const esc=s=>s.replace(/\\/g,"\\\\").replace(/\(/g,"\\(").replace(/\)/g,"\\)");
function inspectPdcPdfTextLayer(base64){
 const fail=reason=>({status:"FAIL_DOCUMENT",reason,candidates:0,createsFlight:false,ownerBound:false,publicationCertified:false});
 let raw;try{raw=fromBase64(base64)}catch{return fail("BAD_BASE64");}
 if(raw.length>200000||!raw.startsWith("%PDF-1.4"))return fail("UNSUPPORTED_PDF");
 if((raw.match(/\/Type\s*\/Page\b/g)||[]).length!==1||/\/Filter\s*\/FlateDecode|\/Encrypt\b/.test(raw))return fail("UNSUPPORTED_PAGE_OR_ENCODING");
 if(!/\/Producer \(PDC Pdf Generator 1\.0, PDC A\/S\)/.test(raw)||!/\/Creator \(PDC Crew\)/.test(raw)||!/\/Title \(PDC Report\)/.test(raw))return fail("WRONG_PRODUCER");
 const streams=[...raw.matchAll(/\bstream\r?\n([\s\S]*?)\r?\nendstream\b/g)];if(streams.length!==1)return fail("STREAM_COUNT");
 const st=streams[0][1],glyphs=[];
 for(const bt of st.matchAll(/\bBT\b([\s\S]*?)\bET\b/g)){
  const p=bt[1].match(/(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)\s+Td\b/),t=bt[1].match(/\(((?:\\.|[^\\)])*)\)\s+Tj\b/);
  if(!p||!t)return fail("UNSUPPORTED_TEXT_OPERATOR");
  glyphs.push({x:+p[1],y:+p[2],text:unesc(t[1])});
 }
 if(glyphs.length!==(st.match(/\bTj\b/g)||[]).length||glyphs.length!==495)return fail("TEXT_GLYPH_CENSUS");
 const at=(x,y)=>glyphs.filter(g=>g.x===x&&g.y===y),title=glyphs.filter(g=>g.text==="Crew Roster Report");
 if(title.length!==3||at(272,801).filter(g=>g.text==="Crew Roster Report").length!==1||at(219,744).filter(g=>g.text==="Crew Roster Report").length!==2)return fail("PRINTED_REPORT_KIND");
 const periods=at(225,688);if(periods.length!==2||periods[0].text!==periods[1].text)return fail("PRINTED_PERIOD_DUPLICATES");
 if(periods[0].text!=="Period: 01Aug26 - 31Aug26")return fail("UNVERIFIED_PERIOD_VARIANT");
 const subject=at(39,702),stamp=at(36,801);
 if(subject.length!==1||!/^Crewmember:\s*\S/.test(subject[0].text))return fail("MISSING_REPORT_SUBJECT_LABEL");
 if(stamp.length!==1||!/^\d{2}-\d{2}-\d{4} \d{4}$/.test(stamp[0].text))return fail("PRINT_STAMP_GRAMMAR");
 const headers=glyphs.filter(g=>g.y===647);
 if(headers.length!==14||headers.some((g,i)=>g.x!==HX[i]||g.text!==HEADERS[i]))return fail("HEADER_OR_COLUMN_ORDER");
 const body=glyphs.filter(g=>g.y<=638&&g.y>=206),top=glyphs.filter(g=>g.y>647),foot=glyphs.filter(g=>g.y<206);
 if(top.length!==7||body.length!==473||foot.length!==1||foot[0].x!==559||foot[0].y!==43||foot[0].text!=="1")return fail("PAGE_SECTIONS");
 const rows=new Map(),xc=Object.fromEntries(BX.map(x=>[x,0]));
 for(const g of body){
  if(!BX.includes(g.x)||(638-g.y)%9!==0)return fail("OFF_GRID_GLYPH");
  const k=(638-g.y)/9;if(!rows.has(k))rows.set(k,new Map());
  if(rows.get(k).has(g.x))return fail("DUPLICATE_BODY_CELL");
  rows.get(k).set(g.x,g.text);xc[g.x]++;
 }
 if(rows.size!==49||BX.some((x,i)=>xc[x]!==BC[i]))return fail("BODY_GRID_CENSUS");
 let numeric=0,nonflight=0,aux=0,ownDateNumeric=0,ownDateNonflight=0,threeDigit=0,fourDigit=0;const seen=new Set();
 for(let i=0;i<49;i++){
  const r=rows.get(i);if(!r)return fail("MISSING_BODY_BAND");
  const activity=r.get(210),date=r.get(81),block=r.get(511);
  if(date!==undefined&&!/^(?:0[1-9]|[12]\d|3[01])Aug26$/.test(date))return fail("INVALID_OWN_DATE");
  if(activity===undefined){aux++;if(r.size!==1||!r.has(388))return fail("UNSUPPORTED_AUX_BAND");continue;}
  if(/^\d+$/.test(activity)&&!/^\d{3,4}$/.test(activity))return fail("UNSUPPORTED_NUMERIC_ACTIVITY_WIDTH");
  if(/^\d{3,4}$/.test(activity)){
   numeric++;if(seen.has(activity))return fail("DUPLICATE_NUMERIC_ACTIVITY");seen.add(activity);
   if(activity.length===3)threeDigit++;else fourDigit++;if(date!==undefined)ownDateNumeric++;
   if(block===undefined||!/^\d{1,2}:[0-5]\d$/.test(block))return fail("INVALID_PRINTED_BLOCK");
   if(!r.get(244)||!r.get(316))return fail("MISSING_NUMERIC_ROUTE");
   for(const x of [268,292,340,364])if(!/^(?:[01]\d|2[0-3])[0-5]\d(?:\+1)?$/.test(r.get(x)||""))return fail("INVALID_NUMERIC_CLOCK");
  }else{nonflight++;if(block!==undefined)return fail("NONFLIGHT_WITH_BLOCK");if(date!==undefined)ownDateNonflight++;}
 }
 if(numeric!==26||nonflight!==22||aux!==1||ownDateNumeric!==13||ownDateNonflight!==18||threeDigit!==8||fourDigit!==18)return fail("SOURCE_FAMILY_COUNTS");
 return {status:"OBSERVED_FAMILY_DETACHED_HOLD",profile:"pdc-generator-14col-Aug26-single-page-C426",glyphs:495,bodyGlyphs:473,headers:14,bands:49,numeric,nonflight,aux,ownDateNumeric,missingOwnDateNumeric:13,ownDateNonflight,threeDigit,fourDigit,printedYearSuffix:"26",fourDigitOperationalYearCertified:false,printedSubjectLabelPresent:true,reportSubjectBoundToUid:false,printedGenerationStampPresent:true,publicationRevisionCertified:false,candidates:26,createsFlight:false,overwritesBlock:false,crewProvidedPerLeg:false};
}
function syntheticFixture(){
 const lines=["%PDF-1.4","1 0 obj << /Type /Page >> endobj","2 0 obj << /Producer (PDC Pdf Generator 1.0, PDC A/S) /Creator (PDC Crew) /Title (PDC Report) /CreationDate (D:20261028000000) >> endobj","3 0 obj << /Length 1 >> stream"];
 const put=(x,y,t)=>lines.push("BT "+x+" "+y+" Td ("+esc(t)+") Tj ET");
 put(36,801,"28-10-2026 0000");put(272,801,"Crew Roster Report");put(219,744,"Crew Roster Report");put(219,744,"Crew Roster Report");
 put(39,702,"Crewmember: SYNTHETIC SUBJECT");put(225,688,"Period: 01Aug26 - 31Aug26");put(225,688,"Period: 01Aug26 - 31Aug26");HEADERS.forEach((v,i)=>put(HX[i],647,v));
 let n=0,f=0;
 for(let i=0;i<49;i++){
  const y=638-9*i;if(i===12){put(388,y,"SYNTHETIC AUX");continue;}
  const isNum=n<26&&(i%2===0||f>=22),k=isNum?n++:f++;
  if(isNum){
   if(k<13)put(81,y,String(k+1).padStart(2,"0")+"Aug26");if(k<16)put(109,y,"PAIR");if(k<15)put(162,y,"0900");if(k<14)put(186,y,"1100");
   put(210,y,k<8?String(100+k):String(1000+k-8));put(244,y,"AAA");put(268,y,"0900");put(292,y,"0900");put(316,y,"BBB");put(340,y,"1030");put(364,y,"1030");put(388,y,"SYN");put(511,y,"1:30");
  }else{
   if(k<18)put(81,y,String(k+1).padStart(2,"0")+"Aug26");if(k<6)put(109,y,"PAIR");if(k===0)put(143,y,"RAW");if(k===0)put(162,y,"0900");if(k<2)put(186,y,"1100");
   put(210,y,"OFF");if(k<18)put(244,y,"AAA");put(268,y,"0900");put(292,y,"0900");if(k<18)put(316,y,"BBB");put(340,y,"1030");put(364,y,"1030");if(k<6)put(388,y,"SYN");
  }
 }
 put(559,43,"1");lines.push("endstream","endobj","trailer << /Root 1 0 R >>","%%EOF");return lines.join("\n");
}
function runSyntheticTests(){
 const base=syntheticFixture(),scan=s=>inspectPdcPdfTextLayer(toBase64(s)),tests=[];
 const check=(name,mutate,expected)=>{const r=scan(mutate(base));tests.push({name,pass:r.status===expected,reason:r.reason||""});};
 const good="OBSERVED_FAMILY_DETACHED_HOLD",bad="FAIL_DOCUMENT";
 check("synthetic baseline",s=>s,good);
 check("wrong report",s=>s.replace("(Crew Roster Report)","(Other Report)"),bad);
 check("period duplicate disagreement",s=>s.replace("Period: 01Aug26 - 31Aug26","Period: 01Sep26 - 30Sep26"),bad);
 check("unsupported period",s=>s.replaceAll("Period: 01Aug26 - 31Aug26","Period: 01Sep26 - 30Sep26"),bad);
 check("missing subject",s=>s.replace("Crewmember: SYNTHETIC SUBJECT","Subject: SYNTHETIC"),bad);
 check("different subject still not UID proof",s=>s.replace("Crewmember: SYNTHETIC SUBJECT","Crewmember: OTHER SYNTHETIC"),good);
 check("header spoof",s=>s.replace("75 647 Td (Date)","75 647 Td (When)"),bad);
 check("header geometry",s=>s.replace("210 647 Td (Activity)","211 647 Td (Activity)"),bad);
 check("unsupported numeric width",s=>s.replace("210 638 Td (100)","210 638 Td (12345)"),bad);
 check("missing block",s=>s.replace("BT 511 638 Td (1:30) Tj ET\n",""),bad);
 check("nonflight block",s=>s.replace("endstream","BT 511 629 Td (1:30) Tj ET\nendstream"),bad);
 check("invalid Date",s=>s.replace("81 638 Td (01Aug26)","81 638 Td (32Aug26)"),bad);
 check("aux hidden clock",s=>s.replace("endstream","BT 268 530 Td (0900) Tj ET\nendstream"),bad);
 check("off-grid hidden glyph",s=>s.replace("endstream","BT 123 620 Td (HIDDEN) Tj ET\nendstream"),bad);
 check("truncated numeric",s=>s.replace("BT 210 638 Td (100) Tj ET\n",""),bad);
 check("CreationDate not Publication",s=>s.replace("D:20261028000000","D:20261231120000"),good);
 check("print stamp not Publication",s=>s.replace("28-10-2026 0000","31-12-2026 1200"),good);
 check("extra page",s=>s.replace("endobj","endobj\n4 0 obj << /Type /Page >> endobj"),bad);
 check("Flate unsupported",s=>s.replace("/Length 1","/Filter /FlateDecode /Length 1"),bad);
 check("duplicate Activity glyph",s=>s.replace("endstream","BT 210 638 Td (999) Tj ET\nendstream"),bad);
 check("raw +1 no date correction",s=>s.replace("364 638 Td (1030)","364 638 Td (1030+1)"),good);
 const r=scan(base);tests.push({name:"detached owner/revision gate",pass:r.status===good&&r.candidates===26&&r.nonflight===22&&r.aux===1&&!r.createsFlight&&!r.reportSubjectBoundToUid&&!r.publicationRevisionCertified,reason:""});
 return {passed:tests.filter(x=>x.pass).length,failed:tests.filter(x=>!x.pass).length,tests,summary:r};
}
export {inspectPdcPdfTextLayer,syntheticFixture,runSyntheticTests};
if(typeof process!=="undefined"&&process.argv&&process.argv[1]&&process.argv[1].endsWith("C426_PDC_NATIVE_PDF_TEXT_ADMISSION.mjs")){const r=runSyntheticTests();console.log(JSON.stringify(r,null,2));if(r.failed)process.exitCode=1;}
