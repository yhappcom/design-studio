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
 let numeric=0,nonflight=0,aux=0,ownDateNumeric=0,ownDateNonflight=0,threeDigit=0,fourDigit=0;
  // Research-only source-internal arithmetic, not operational Block/date authority.
  const clockMin=v=>{const m=/^([01]\d|2[0-3])([0-5]\d)(\+1)?$/.exec(v||"");return m?+m[1]*60+(+m[2])+(m[3]?1440:0):null;};
  const blockMin=v=>{const m=/^(\d{1,2}):([0-5]\d)$/.exec(v||"");return m?+m[1]*60+(+m[2]):null;};
 for(let i=0;i<49;i++){
  const r=rows.get(i);if(!r)return fail("MISSING_BODY_BAND");
  const activity=r.get(210),date=r.get(81),block=r.get(511);
  if(date!==undefined&&!/^(?:0[1-9]|[12]\d|3[01])Aug26$/.test(date))return fail("INVALID_OWN_DATE");
  if(activity===undefined){aux++;if(r.size!==1||!r.has(388))return fail("UNSUPPORTED_AUX_BAND");continue;}
  if(/^\d+$/.test(activity)&&!/^\d{3,4}$/.test(activity))return fail("UNSUPPORTED_NUMERIC_ACTIVITY_WIDTH");
  if(/^\d{3,4}$/.test(activity)){
   numeric++; // Activity is a raw label, not a unique physical row key.
   if(activity.length===3)threeDigit++;else fourDigit++;if(date!==undefined)ownDateNumeric++;
   if(block===undefined||!/^\d{1,2}:[0-5]\d$/.test(block))return fail("INVALID_PRINTED_BLOCK");
   if(!r.get(244)||!r.get(316))return fail("MISSING_NUMERIC_ROUTE");
    if(!/^[A-Z]{3}$/.test(r.get(244))||!/^[A-Z]{3}$/.test(r.get(316)))return fail("INVALID_NUMERIC_ROUTE_SHAPE");
   for(const x of [268,292,340,364])if(!/^(?:[01]\d|2[0-3])[0-5]\d(?:\+1)?$/.test(r.get(x)||""))return fail("INVALID_NUMERIC_CLOCK");
   const baseElapsed=clockMin(r.get(364))-clockMin(r.get(292));
   if(baseElapsed<=0||baseElapsed!==blockMin(block))return fail("PRINTED_BASE_CLOCK_BLOCK_CONTRADICTION");
  }else{nonflight++;if(block!==undefined)return fail("NONFLIGHT_WITH_BLOCK");if(date!==undefined)ownDateNonflight++;for(const x of [244,316])if(r.has(x)&&!/^[A-Z]{3}$/.test(r.get(x)))return fail("INVALID_NONFLIGHT_ROUTE_SHAPE");}
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
  check("C437 repeated Activity on separate dated bands remains detached",s=>s.replace("210 620 Td (101)","210 620 Td (100)"),good);
  check("C437 repeated Activity plus same own-Date still detached, not merged",s=>s.replace("210 620 Td (101)","210 620 Td (100)").replace("81 620 Td (02Aug26)","81 620 Td (01Aug26)"),good);
 check("base Block mismatch",s=>s.replace("511 638 Td (1:30)","511 638 Td (9:30)"),bad);
 check("base departure shift",s=>s.replace("292 638 Td (0900)","292 638 Td (0800)"),bad);
 check("base arrival shift",s=>s.replace("364 638 Td (1030)","364 638 Td (1130)"),bad);
 check("base departure +1 shift",s=>s.replace("292 638 Td (0900)","292 638 Td (0900+1)"),bad);
 check("local clock difference allowed",s=>s.replace("268 638 Td (0900)","268 638 Td (1500)"),good);
 check("joint clock and Block change remains detached",s=>s.replace("364 638 Td (1030)","364 638 Td (1130)").replace("511 638 Td (1:30)","511 638 Td (2:30)"),good);
 check("paired base +1 offsets",s=>s.replace("292 638 Td (0900)","292 638 Td (0900+1)").replace("364 638 Td (1030)","364 638 Td (1030+1)"),good);
 check("unpaired STA +1 contradicts Block",s=>s.replace("364 638 Td (1030)","364 638 Td (1030+1)"),bad);
 const r=scan(base);tests.push({name:"detached owner/revision gate",pass:r.status===good&&r.candidates===26&&r.nonflight===22&&r.aux===1&&!r.createsFlight&&!r.reportSubjectBoundToUid&&!r.publicationRevisionCertified,reason:""});
 return {passed:tests.filter(x=>x.pass).length,failed:tests.filter(x=>!x.pass).length,tests,summary:r};
}
export {inspectPdcPdfTextLayer,syntheticFixture,runSyntheticTests};
if(typeof process!=="undefined"&&process.argv&&process.argv[1]&&process.argv[1].endsWith("C426_PDC_NATIVE_PDF_TEXT_ADMISSION.mjs")){const r=runSyntheticTests();console.log(JSON.stringify(r,null,2));if(r.failed)process.exitCode=1;}

// C427: observed PDC PDF physical-envelope gate (research only).
// The prior C426 text scanner does not resolve xref, Catalog, Page, Contents or /Length.
// Strict wrapper rejects detached/hidden streams and corrupt PDF graphs before text admission.
// Exact one-source object layout; production MUST use a standards-compliant PDF parser.
function validatePdcPhysicalEnvelope(raw){
 const fail=reason=>({ok:false,reason});
 if(typeof raw!=="string"||!raw.startsWith("%PDF-1.4")||raw.length>200000)return fail("PDF_HEADER_OR_SIZE");
 if((raw.match(/%%EOF/g)||[]).length!==1||(raw.match(/(?:^|\r?\n)xref\r?\n/g)||[]).length!==1)return fail("INCREMENTAL_OR_XREF_COUNT");
 const st=[...raw.matchAll(/startxref\s+(\d+)/g)];if(st.length!==1)return fail("STARTXREF_COUNT");
 const offset=+st[0][1];if(raw.slice(offset,offset+5)!=="xref\n")return fail("XREF_OFFSET");
 const x=raw.slice(offset).match(/^xref\r?\n0 19\r?\n((?:\d{10} \d{5} [nf]\r?\n){19})trailer\r?\n/);if(!x)return fail("XREF_FORMAT");
 const entries=x[1].trim().split(/\r?\n/);if(entries.length!==19||!/^\d{10} 65535 f$/.test(entries[0]))return fail("XREF_COUNT");
 const objects=[...raw.matchAll(/(?:^|\r?\n)(\d+) 0 obj\b([\s\S]*?)\bendobj/g)],by=new Map(objects.map(a=>[+a[1],a[2]]));
 if(objects.length!==18||by.size!==18)return fail("OBJECT_CENSUS");
 for(let id=1;id<=18;id++){const e=entries[id].match(/^(\d{10}) 00000 n$/);if(!e||!raw.slice(+e[1]).startsWith(id+" 0 obj"))return fail("XREF_ENTRY_"+id)}
 const has=(id,re)=>re.test(by.get(id)||"");
 if(!has(18,/\/Type\s*\/Catalog\b/)||!has(18,/\/Pages\s+2 0 R\b/)||!has(2,/\/Type\s*\/Pages\b/)||!has(2,/\/Kids\s*\[17 0 R\]/)||!has(2,/\/Count\s+1\b/)||!has(17,/\/Type\s*\/Page\b/)||!has(17,/\/Parent\s+2 0 R\b/)||!has(17,/\/Contents\s+16 0 R\b/)||!has(17,/\/Resources\s+15 0 R\b/))return fail("PAGE_GRAPH");
 if(!has(2,/\/MediaBox\s*\[0 0 598 842\]/))return fail("MEDIA_BOX");
 if(!/trailer\r?\n<<\s*\/Size 19\s*\/Root 18 0 R\s*\/Info 1 0 R\s*>>/.test(raw.slice(offset)))return fail("TRAILER_GRAPH");
 if(!has(1,/\/Producer\s*\(PDC Pdf Generator 1\.0, PDC A\/S\)/)||!has(1,/\/Creator\s*\(PDC Crew\)/)||!has(1,/\/Title\s*\(PDC Report\)/))return fail("INFO_AUTHORITY");
 const ob=by.get(16),length=+(ob.match(/\/Length\s+(\d+)/)||[])[1],p=ob.indexOf("stream\n")+7,e=ob.indexOf("\nendstream",p);
 if(!/^\s*<<\s*\/Type\s*\/Page\s*\/Parent\s+2 0 R\s*\/Resources\s+15 0 R\s*\/Contents\s+16 0 R\s*>>\s*$/.test(by.get(17)))return fail("UNSUPPORTED_PAGE_DICTIONARY");
 if(!/^\s*<<\s*\/Length\s+\d+\s*>>\s*stream\n/.test(ob))return fail("UNSUPPORTED_CONTENT_DICTIONARY");
 if(!length||p<7||e<0||e-p!==length)return fail("STREAM_LENGTH");
 const content=ob.slice(p,e);
 // C430: observed-family graphics whitelist; NOT a renderer or portable profile.
 // Original: 1 stroke setup, 14 header fills, 876 grid strokes; synthetic: none.
 const outside=content.replace(/\bBT\b[\s\S]*?\bET\b/g,"");
 const graphics=outside.split(/\r?\n/).map(s=>s.trim()).filter(Boolean);
 const num="-?\\d+(?:\\.\\d+)?";
 const fill=new RegExp("^("+num+"\\s+){3}rg\\s+("+num+"\\s+){4}re\\s+f$");
 const stroke=new RegExp("^("+num+"\\s+){2}m\\s+("+num+"\\s+){2}l\\s+S$");
 if(graphics.length){
  if(graphics.length!==891)return fail("UNSUPPORTED_PAINT_CENSUS");
  let a=0,b=0,c=0;
  for(const line of graphics){
   if(line==="0 0 0 RG 0.10 w [] 0 d")a++;
   else if(fill.test(line))b++;
   else if(stroke.test(line))c++;
   else return fail("UNSUPPORTED_PAINT_OPERATOR");
  }
  if(a!==1||b!==14||c!==876)return fail("UNSUPPORTED_PAINT_PROFILE");
  const earlier=[...content.matchAll(/\bBT\b([\s\S]*?)\bET\b/g)].map(m=>{
   const p=m[1].match(/(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)\s+Td\b/);
   return p?{i:m.index,x:+p[1],y:+p[2]}:null;
  }).filter(Boolean);
  for(const m of content.matchAll(/(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)\s+re\s+f\b/g)){
   const x=+m[1],y=+m[2],w=+m[3],h=+m[4];
   if(earlier.some(g=>g.i<m.index&&g.x>=x&&g.x<=x+w&&g.y>=y&&g.y<=y+h))return fail("PAINT_COVERS_PRIOR_TEXT_ANCHOR");
  }
 }
 if(/\b(?:cm|Tr|Tm)\b/.test(content))return fail("UNSUPPORTED_CONTENT_TRANSFORM_OR_RENDER_MODE");
 if(!content.trimEnd().endsWith("ET"))return fail("TRAILING_NON_TEXT_AFTER_LAST_ET");
 if((raw.match(/\bstream\r?\n/g)||[]).length!==1||/\/Filter\s*\/FlateDecode|\/Encrypt\b/.test(raw))return fail("UNSUPPORTED_STREAM");
 return {ok:true,objects:18,pages:1,contentObject:16};
}

function wrapPdcSyntheticTextMock(mock){
 const start=mock.indexOf("stream\n"),end=mock.indexOf("\nendstream",start+7);
 if(start<0||end<0)throw Error("SYNTHETIC_MOCK_STREAM_MISSING");
 const payload=mock.slice(start+7,end),objects=[];
 objects[1]="<< /Producer (PDC Pdf Generator 1.0, PDC A/S) /Creator (PDC Crew) /Title (PDC Report) >>";
 objects[2]="<< /Type /Pages /Kids [17 0 R] /Count 1 /MediaBox [0 0 598 842] >>";
 for(let id=3;id<=14;id++)objects[id]="<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>";
 objects[15]="<< /ProcSet [/PDF /Text] >>";
 objects[16]="<< /Length "+payload.length+" >>\nstream\n"+payload+"\nendstream";
 objects[17]="<< /Type /Page /Parent 2 0 R /Resources 15 0 R /Contents 16 0 R >>";
 objects[18]="<< /Type /Catalog /Pages 2 0 R >>";
 let doc="%PDF-1.4\n",offsets=[0];
 for(let id=1;id<=18;id++){offsets[id]=doc.length;doc+=id+" 0 obj\n"+objects[id]+"\nendobj\n"}
 const startxref=doc.length;doc+="xref\n0 19\n0000000000 65535 f\n";
 for(let id=1;id<=18;id++)doc+=String(offsets[id]).padStart(10,"0")+" 00000 n\n";
 doc+="trailer\n<< /Size 19 /Root 18 0 R /Info 1 0 R >>\nstartxref\n"+startxref+"\n%%EOF\n";
 return doc;
}

function pdcEnvelopeMutations(s){
 const x=s.match(/\/Length (\d+)/),len=x?+x[1]:0;
 const ref=s.match(/startxref\n(\d+)/),start=ref?+ref[1]:0;
 const block=s.match(/xref\n0 19\n((?:.*\n){19})/),lines=block?block[1].trim().split("\n"):[];
 const before=lines[16]||"";
 const changed=before.replace(/^\d{10}/,v=>String(+v+1).padStart(10,"0"));
 return [
 ["page content pointer",s.replace("/Contents 16 0 R","/Contents 15 0 R")],
 ["catalog Pages pointer",s.replace("/Pages 2 0 R","/Pages 3 0 R")],
 ["Pages Kids pointer",s.replace("/Kids [17 0 R]","/Kids [15 0 R]")],
 ["Page Parent pointer",s.replace("/Parent 2 0 R","/Parent 3 0 R")],
 ["declared stream length",s.replace("/Length "+len,"/Length "+(len-1))],
 ["trailer Root pointer",s.replace("/Root 18 0 R","/Root 17 0 R")],
 ["page count",s.replace("/Count 1","/Count 2")],
 ["trailer Info pointer",s.replace("/Info 1 0 R","/Info 2 0 R")],
 ["xref object16 offset",s.replace(before,changed)],
 ["startxref offset",s.replace("startxref\n"+start,"startxref\n"+(start+1))],
 ["MediaBox clips text",s.replace("/MediaBox [0 0 598 842]","/MediaBox [0 0 100 100]")]
 ];
}

function inspectPdcPdfStrict(base64){
 const raw=fromBase64(base64),envelope=validatePdcPhysicalEnvelope(raw);
 if(!envelope.ok)return {status:"FAIL_DOCUMENT",reason:"PHYSICAL_"+envelope.reason,candidates:0,createsFlight:false,ownerBound:false,publicationCertified:false};
 return inspectPdcPdfTextLayer(base64);
}


function repackPdcSyntheticPdf(doc, edit) {
 const matches=[...doc.matchAll(/(?:^|\n)(\d+) 0 obj\n([\s\S]*?)\nendobj(?=\n)/g)];
 if(matches.length!==18)throw Error("SYNTHETIC_OBJECT_CENSUS");
 const objects=Object.fromEntries(matches.map(m=>[+m[1],m[2]]));
 edit(objects);
 let result="%PDF-1.4\n",offsets=[0];
 for(let i=1;i<=18;i++){offsets[i]=result.length;result+=i+" 0 obj\n"+objects[i]+"\nendobj\n";}
 const xref=result.length;result+="xref\n0 19\n0000000000 65535 f\n";
 for(let i=1;i<=18;i++)result+=String(offsets[i]).padStart(10,"0")+" 00000 n\n";
 return result+"trailer\n<< /Size 19 /Root 18 0 R /Info 1 0 R >>\nstartxref\n"+xref+"\n%%EOF\n";
}
function pdcVisualAndDictionaryMutations(doc) {
 const editStream=(o,edit)=>{
  o[16]=edit(o[16]);
  o[16]=o[16].replace(/\/Length \d+/, "/Length "+o[16].split("stream\n")[1].split("\nendstream")[0].length);
 };
 return [
 ["page rotation",o=>{o[17]=o[17].replace("/Contents","/Rotate 180 /Contents");}],
 ["page crop",o=>{o[17]=o[17].replace("/Contents","/CropBox [0 0 100 100] /Contents");}],
 ["unhandled stream filter",o=>{o[16]=o[16].replace("/Length","/Filter /ASCIIHexDecode /Length");}],
 ["content transformation matrix",o=>editStream(o,s=>s.replace("stream\n","stream\nq 0.5 0 0 0.5 0 0 cm\n").replace("\nendstream","\nQ\nendstream"))],
 ["duplicate Contents key",o=>{o[17]=o[17].replace("/Contents 16 0 R","/Contents 16 0 R /Contents 16 0 R");}],
 ["page annotation overlay",o=>{o[17]=o[17].replace("/Contents","/Annots [3 0 R] /Contents");}],
 ["invisible text rendering",o=>editStream(o,s=>s.replace("stream\n","stream\n3 Tr\n"))],
 ["opaque overlay after final text",o=>editStream(o,s=>s.replace("\nendstream","\n0 0 0 rg 0 0 598 842 re f\nendstream"))]
 ].map(([name,edit])=>[name,repackPdcSyntheticPdf(doc,edit)]);
}

function runPdcEnvelopeTests(){
 const full=wrapPdcSyntheticTextMock(syntheticFixture()),base=inspectPdcPdfStrict(toBase64(full));
 const tests=[{name:"xref-consistent synthetic PDF baseline",pass:base.status==="OBSERVED_FAMILY_DETACHED_HOLD",reason:base.reason||""}];
 for(const [name,mutant] of pdcEnvelopeMutations(full)){
  const r=inspectPdcPdfStrict(toBase64(mutant));
  tests.push({name,pass:mutant!==full&&r.status==="FAIL_DOCUMENT"&&r.reason.startsWith("PHYSICAL_"),reason:r.reason||""});
 }
 for(const [name,mutant] of pdcVisualAndDictionaryMutations(full)){
  const r=inspectPdcPdfStrict(toBase64(mutant));
  tests.push({name,pass:r.status==="FAIL_DOCUMENT"&&r.reason.startsWith("PHYSICAL_"),reason:r.reason||""});
 }
 const editContent=(find,replacement,extra)=>repackPdcSyntheticPdf(full,o=>{let c=o[16].replace(find,replacement);if(extra)c=c.replace("511 638 Td (1:30)","511 638 Td (2:30)");o[16]=c.replace(/\/Length \d+/,"/Length "+c.split("stream\n")[1].split("\nendstream")[0].length);});
 for(const [name,find,replacement,expected,extra] of [
  ["strict base Block mismatch","511 638 Td (1:30)","511 638 Td (9:30)","FAIL_DOCUMENT",false],
  ["strict base STD shift","292 638 Td (0900)","292 638 Td (0800)","FAIL_DOCUMENT",false],
  ["strict base STA shift","364 638 Td (1030)","364 638 Td (1130)","FAIL_DOCUMENT",false],
  ["strict local difference","268 638 Td (0900)","268 638 Td (1500)","OBSERVED_FAMILY_DETACHED_HOLD",false],
  ["strict jointly altered source remains detached","364 638 Td (1030)","364 638 Td (1130)","OBSERVED_FAMILY_DETACHED_HOLD",true]
 ]){const r=inspectPdcPdfStrict(toBase64(editContent(find,replacement,extra)));tests.push({name,pass:r.status===expected,reason:r.reason||""});}
 const overlay=editContent("BT 559 43 Td (1) Tj ET","0 0 0 rg 0 0 598 842 re f\nBT 559 43 Td (1) Tj ET",false);
 const knownVisualFailOpen=inspectPdcPdfStrict(toBase64(overlay)).status==="OBSERVED_FAMILY_DETACHED_HOLD";
 // No verified universal airport-code grammar: report a gap rather than silently claiming validation.
 const invalidRoute=editContent("244 638 Td (AAA)","244 638 Td (X)",false);
 const knownRouteShapeFailOpen=inspectPdcPdfStrict(toBase64(invalidRoute)).status==="OBSERVED_FAMILY_DETACHED_HOLD";
 tests.push({name:"opaque overlay before footer rejected",pass:!knownVisualFailOpen,reason:knownVisualFailOpen?"STILL_FAIL_OPEN":""});
 tests.push({name:"one-character numeric route rejected",pass:!knownRouteShapeFailOpen,reason:knownRouteShapeFailOpen?"STILL_FAIL_OPEN":""});
 for(const [name,needle,value] of [
  ["nonflight short route","244 629 Td (AAA)","244 629 Td (X)"],
  ["numeric four-letter route","316 638 Td (BBB)","316 638 Td (BBBB)"],
  ["nonflight lower-case route","316 629 Td (BBB)","316 629 Td (bbb)"]
 ]){
  const mutant=repackPdcSyntheticPdf(full,o=>{o[16]=o[16].replace(needle,value);o[16]=o[16].replace(/\/Length \d+/,"/Length "+o[16].split("stream\n")[1].split("\nendstream")[0].length);});
  const r=inspectPdcPdfStrict(toBase64(mutant));tests.push({name,pass:r.status==="FAIL_DOCUMENT",reason:r.reason||""});
 }
 const painted=repackPdcSyntheticPdf(full,o=>{o[16]=o[16].replace("BT 559 43 Td (1) Tj ET","0 0 0 RG 100 w 0 0 m 598 842 l S\nBT 559 43 Td (1) Tj ET");o[16]=o[16].replace(/\/Length \d+/,"/Length "+o[16].split("stream\n")[1].split("\nendstream")[0].length);});
 const paintedResult=inspectPdcPdfStrict(toBase64(painted));tests.push({name:"opaque thick stroke unsupported",pass:paintedResult.status==="FAIL_DOCUMENT",reason:paintedResult.reason||""});
 return {passed:tests.filter(x=>x.pass).length,failed:tests.filter(x=>!x.pass).length,tests,baseline:base.status,knownVisualFailOpen,knownRouteShapeFailOpen};
}
export {validatePdcPhysicalEnvelope,wrapPdcSyntheticTextMock,pdcEnvelopeMutations,inspectPdcPdfStrict,runPdcEnvelopeTests};
if(typeof process!=="undefined"&&process.argv&&process.argv[1]&&process.argv[1].endsWith("C426_PDC_NATIVE_PDF_TEXT_ADMISSION.mjs")){const r=runPdcEnvelopeTests();console.log(JSON.stringify(r,null,2));if(r.failed)process.exitCode=1;}


// C430: caller-supplied private original is never logged, copied or committed.
function runPdcOriginalReadOnlyAdversarial(base64){
 const raw=fromBase64(base64),baseline=inspectPdcPdfStrict(base64);
 const repacked=repackPdcSyntheticPdf(raw,()=>{}),repackedResult=inspectPdcPdfStrict(toBase64(repacked));
 const tests=[{name:"unchanged original detached",pass:baseline.status==="OBSERVED_FAMILY_DETACHED_HOLD",reason:baseline.reason||""},
 {name:"xref-repacked original detached",pass:repackedResult.status==="OBSERVED_FAMILY_DETACHED_HOLD",reason:repackedResult.reason||""}];
 // C437: original-derived in-memory mutants; no raw Activity or roster values persist.
 for(const width of [3,4]){
  let changed=false;
  const modified=repackPdcSyntheticPdf(raw,o=>{
   const old=o[16],start=old.indexOf("stream\n")+7,end=old.lastIndexOf("\nendstream");
   if(start<7||end<start)throw Error("ORIGINAL_STREAM_NOT_FOUND");
   const content=old.slice(start,end);
   const rows=[...content.matchAll(/BT 210 (\d+(?:\.\d+)?) Td \((\d{3,4})\) Tj ET/g)].filter(m=>m[2].length===width);
   if(rows.length<2||rows[0][2]===rows[1][2])throw Error("ACTIVITY_PAIR_UNAVAILABLE");
   const target=rows[1][0],replacement=target.replace("("+rows[1][2]+")","("+rows[0][2]+")");
   changed=target!==replacement;
   const next=content.replace(target,replacement);
   o[16]=old.slice(0,start).replace(/\/Length \d+/,"/Length "+next.length)+next+old.slice(end);
  });
  const r=inspectPdcPdfStrict(toBase64(modified));
  tests.push({name:"C437 original-derived repeated "+width+"-digit Activity held",pass:changed&&r.status==="OBSERVED_FAMILY_DETACHED_HOLD",reason:r.reason||""});
 }
 const cases=[
  ["replace original header fill with full-page opaque cover",s=>s.replace(/0\.75 0\.75 0\.75 rg [^\n]+ re f/,"0 0 0 rg 0 0 598 842 re f")],
  ["shorten original From token",s=>s.replace(/(BT 244 \d+(?:\.\d+)? Td [^\n]*?\()[A-Z]{3}(\) Tj ET)/,"$1X$2")],
  ["change original stroke setup to thick",s=>s.replace("0.10 w","100 w")],
  ["insert original full-page overlay before footer",s=>s.replace(/BT 559 43 Td/,"0 0 0 rg 0 0 598 842 re f\nBT 559 43 Td")]
 ];
 for(const [name,edit] of cases){
  let changed=false;
  const modified=repackPdcSyntheticPdf(raw,o=>{
   const old=o[16],start=old.indexOf("stream\n")+7,end=old.lastIndexOf("\nendstream");
   if(start<7||end<start)throw Error("ORIGINAL_STREAM_NOT_FOUND");
   const content=old.slice(start,end),next=edit(content);changed=next!==content;
   o[16]=old.slice(0,start).replace(/\/Length \d+/,"/Length "+next.length)+next+old.slice(end);
  });
  const r=inspectPdcPdfStrict(toBase64(modified));
  tests.push({name,pass:changed&&r.status==="FAIL_DOCUMENT",reason:r.reason||""});
 }
 return {passed:tests.filter(t=>t.pass).length,failed:tests.filter(t=>!t.pass).length,tests};
}
export {runPdcOriginalReadOnlyAdversarial};
