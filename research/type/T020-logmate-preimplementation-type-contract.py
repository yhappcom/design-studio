from pathlib import Path
import json, hashlib, base64, os, shutil
from fontTools.ttLib import TTFont
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent

def resolve_font(env_name, filename):
    candidates = [
        os.environ.get(env_name),
        str(ROOT / filename),
        str(Path('/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF') / filename),
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return Path(candidate)
    raise SystemExit(
        f'Missing {filename}. Set {env_name} to an open-source Roboto control font path.'
    )

FONTS = {
    400: resolve_font('T020_ROBOTO_400', 'Roboto-Regular.ttf'),
    500: resolve_font('T020_ROBOTO_500', 'Roboto-Medium.ttf'),
    700: resolve_font('T020_ROBOTO_700', 'Roboto-Bold.ttf'),
}
SCALES = [1.0, 1.10, 1.20, 1.25, 1.30, 1.50, 2.0]
AIRPORTS = ['ICN','NRT','SIN','JFK','LHR','CDG','HND','DXB','FRA','LAX']
OPEN_TIMES = ['00:45','02:18','09:55','12:40']
REGS = ['HL8301','N12345','G-EUOH','UR-82060']
AIRCRAFT = ['B738','B38M','B77W','B737-900','B737-8','A320-200']
CARRIERS = ['7C','KE','AA','BA','AF']
FLIGHT_NUMBERS = ['28','132','1123','1234A','704','117','264']
TOTALS = ['12+30','99,987+29','99,999+59','1,284:35','9,999:59']
DATES = ['09.02','02/09','9/2','12.31','31/12']
IDENTS = ['KE704','BA117','AF264','B737-900','B737-8','A320-200','HL8301','N12345','G-EUOH','UR-82060']


def font_meta(path):
    font = TTFont(path)
    def name(name_id):
        for record in font['name'].names:
            if record.nameID == name_id:
                try:
                    return record.toUnicode()
                except Exception:
                    pass
        return None
    tags = []
    for table in ('GSUB', 'GPOS'):
        if table in font and getattr(font[table].table, 'FeatureList', None):
            tags += [record.FeatureTag for record in font[table].table.FeatureList.FeatureRecord]
    return {
        'file': path.name,
        'bytes': path.stat().st_size,
        'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'version': name(5),
        'weightClass': font['OS/2'].usWeightClass,
        'unitsPerEm': font['head'].unitsPerEm,
        'hhea': {
            'ascent': font['hhea'].ascent,
            'descent': font['hhea'].descent,
            'lineGap': font['hhea'].lineGap,
        },
        'features': sorted(set(tags)),
    }


def data_uri(path):
    return 'data:font/ttf;base64,' + base64.b64encode(path.read_bytes()).decode('ascii')

html = f'''<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:LMRoboto;src:url("{data_uri(FONTS[400])}") format("truetype");font-weight:400;font-style:normal}}
@font-face{{font-family:LMRoboto;src:url("{data_uri(FONTS[500])}") format("truetype");font-weight:500;font-style:normal}}
@font-face{{font-family:LMRoboto;src:url("{data_uri(FONTS[700])}") format("truetype");font-weight:700;font-style:normal}}
body{{font-family:LMRoboto,sans-serif;font-synthesis:none;margin:20px}}
.probe{{display:inline-block;white-space:nowrap}}
</style><div id="root"></div>'''

(ROOT / 'T020-logmate-preimplementation-type-contract-specimen.html').write_text(
    '<!doctype html><meta charset="utf-8"><title>T020 specimen contract</title>'
    '<p>Runtime harness injects local control fonts as data URIs. No font binaries are stored in Design Studio.</p>'
    '<div>Opening: DEP 44 | connector 46 | ARR 44 | flexible | time 68</div>'
    '<div>Ledger: Date 64, Type 60, Reg 84, Flight 84, DEP 50, ARR 50, Block/Night/Instrument 96</div>',
    encoding='utf-8',
)

probe_js = '''async ({airports,times,regs,aircraft,carriers,flightNumbers,totals,dates,idents,scales}) => {
 await Promise.all([document.fonts.load('400 15px LMRoboto'),document.fonts.load('500 17px LMRoboto'),document.fonts.load('700 34px LMRoboto')]);
 await document.fonts.ready;
 const root=document.querySelector('#root');
 const measure=(text,size,weight=400,features='normal')=>{const el=document.createElement('span');el.className='probe';el.textContent=text;el.style.fontSize=size+'px';el.style.fontWeight=weight;el.style.fontVariantNumeric=features;root.appendChild(el);const w=el.getBoundingClientRect().width;el.remove();return w};
 const scaled=(strings,base,weight,features,cell)=>Object.fromEntries(scales.map(s=>[String(s),{widths:Object.fromEntries(strings.map(x=>[x,measure(x,base*s,weight,features)])),failures:strings.filter(x=>measure(x,base*s,weight,features)>cell)}]));
 const digitWidths=(features)=>Object.fromEntries('0123456789'.split('').map(x=>[x,measure(x,15,400,features)]));
 const dprop=digitWidths('normal'),dtnum=digitWidths('tabular-nums'),spread=o=>Math.max(...Object.values(o))-Math.min(...Object.values(o));
 return {userAgent:navigator.userAgent,fontChecks:{r400:document.fonts.check('400 15px LMRoboto'),r500:document.fonts.check('500 17px LMRoboto'),r700:document.fonts.check('700 34px LMRoboto')},opening:{airportCell:44,connectorCell:46,timeCell:68,airports:scaled(airports,17,500,'normal',44),times:scaled(times,17,500,'tabular-nums',68)},ledger:{airportContent:42,registrationContent:76,typeContent:52,totalContent:84,dateContent:56,flightCellContent:68,carrierZone:19,flightNumberZone:47,airports:scaled(airports,15,400,'normal',42),registrations:scaled(regs,15,400,'normal',76),aircraft:scaled(aircraft,15,400,'normal',52),totals400:scaled(totals,15,400,'tabular-nums',84),totals500:scaled(totals,15,500,'tabular-nums',84),dates:scaled(dates,15,400,'tabular-nums',56),carriers:scaled(carriers,15,400,'normal',19),flightNumbers:scaled(flightNumbers,15,400,'tabular-nums',47)},identifiers15:Object.fromEntries(idents.map(x=>[x,measure(x,15,400,'normal')])),digits:{proportional:dprop,tabular:dtnum,proportionalSpread:spread(dprop),tabularSpread:spread(dtnum)}};
}'''

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=True,
        executable_path='/usr/bin/chromium',
        args=['--no-sandbox'],
    )
    page = browser.new_page(viewport={'width': 1200, 'height': 900})
    page.set_content(html, wait_until='load')
    data = page.evaluate(probe_js, {
        'airports': AIRPORTS,
        'times': OPEN_TIMES,
        'regs': REGS,
        'aircraft': AIRCRAFT,
        'carriers': CARRIERS,
        'flightNumbers': FLIGHT_NUMBERS,
        'totals': TOTALS,
        'dates': DATES,
        'idents': IDENTS,
        'scales': SCALES,
    })
    browser.close()


def threshold(cell, widths):
    key, value = max(widths.items(), key=lambda item: item[1])
    return {
        'limitingValue': key,
        'maxWidth': value,
        'cellOrContentWidth': cell,
        'linearScaleRatio': cell / value,
        'slack': cell - value,
    }

ledger = data['ledger']
derived = {
    'thresholds': {
        'openingAirport': threshold(44, data['opening']['airports']['1']['widths']),
        'openingTime': threshold(68, data['opening']['times']['1']['widths']),
        'ledgerAirport': threshold(42, ledger['airports']['1']['widths']),
        'registration': threshold(76, ledger['registrations']['1']['widths']),
        'aircraftType': threshold(52, ledger['aircraft']['1']['widths']),
        'total500': threshold(84, ledger['totals500']['1']['widths']),
        'date': threshold(56, ledger['dates']['1']['widths']),
        'carrierCurrent19': threshold(19, ledger['carriers']['1']['widths']),
        'flightNumberCurrent47': threshold(47, ledger['flightNumbers']['1']['widths']),
    },
    'flightZoneProposal': {
        'carrierWidth': 20,
        'gap': 2,
        'numberWidth': 46,
        'contentWidth': 68,
        'carrierFits': all(v <= 20 for v in ledger['carriers']['1']['widths'].values()),
        'numberFits': all(v <= 46 for v in ledger['flightNumbers']['1']['widths'].values()),
    },
    'assertions': {
        'openingAirportsFitNormal44': not data['opening']['airports']['1']['failures'],
        'openingTimesFitNormal68': not data['opening']['times']['1']['failures'],
        'openingAirportFixed44FailsBy1_25': bool(data['opening']['airports']['1.25']['failures']),
        'ledgerAirportsFitNormal42Content': not ledger['airports']['1']['failures'],
        'registrationsFitNormal76Content': not ledger['registrations']['1']['failures'],
        'currentFullAircraftCorpusDoesNotFit52Content': bool(ledger['aircraft']['1']['failures']),
        'currentCarrier19DoesNotFitAll': bool(ledger['carriers']['1']['failures']),
        'proposedCarrier20AndNumber46FitNormal': all(v <= 20 for v in ledger['carriers']['1']['widths'].values()) and all(v <= 46 for v in ledger['flightNumbers']['1']['widths'].values()),
        'totalsFitNormal84Content': not ledger['totals500']['1']['failures'],
        'tabularDigitSpreadZero': data['digits']['tabularSpread'] == 0,
    },
}

result = {
    'study': 'T020',
    'evidenceBoundary': 'Chromium geometry control uses installed Roboto v2.138; product asset identity/provenance is separately verified as Google Fonts Roboto v2.137. Scale factors are controlled linear font-size stress, not actual Flutter TextScaler proof.',
    'runtimeAvailability': {
        'flutter': shutil.which('flutter'),
        'dart': shutil.which('dart'),
        'chromium': '/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None,
    },
    'productProvenance': {
        'logmateRobotoRegular': {'gitBlobSha': '2c97eeadffe1a34bd67d3ff1c3887fd53e22c2ca', 'bytes': 171676},
        'logmateRobotoMedium': {'gitBlobSha': '1a7f3b0bba45b7470a4240c3ec67595eeeb02192', 'bytes': 172064},
        'matchingGoogleFontsCommit': '724bf98e9f5cb98a1d3d5044f45a2e286b817401',
        'matchingRobotoBold700': {'gitBlobSha': 'd3f01ad245b628f386ac95786f53167038720eb2', 'bytes': 170760},
        'logmateNotoSansKR': {'gitBlobSha': 'b386890ba945e1f39448a6b59f20c5d194f58808', 'bytes': 10414588, 'matchesCurrentGoogleFontsAsset': True, 'wghtAxis': [100, 900]},
    },
    'controlFonts': {str(weight): font_meta(path) for weight, path in FONTS.items()},
    'fontChecks': data['fontChecks'],
    'digitSpread': {
        'proportional': data['digits']['proportionalSpread'],
        'tabular': data['digits']['tabularSpread'],
    },
    'normalWidths': {
        'openingAirport': data['opening']['airports']['1']['widths'],
        'openingTime': data['opening']['times']['1']['widths'],
        'ledgerAirport': ledger['airports']['1']['widths'],
        'registration': ledger['registrations']['1']['widths'],
        'aircraft': ledger['aircraft']['1']['widths'],
        'total500': ledger['totals500']['1']['widths'],
        'date': ledger['dates']['1']['widths'],
        'carrier': ledger['carriers']['1']['widths'],
        'flightNumber': ledger['flightNumbers']['1']['widths'],
    },
    'scaleFailures': {
        'openingAirport': {scale: values['failures'] for scale, values in data['opening']['airports'].items()},
        'openingTime': {scale: values['failures'] for scale, values in data['opening']['times'].items()},
        'ledgerAirport': {scale: values['failures'] for scale, values in ledger['airports'].items()},
        'registration': {scale: values['failures'] for scale, values in ledger['registrations'].items()},
        'aircraft': {scale: values['failures'] for scale, values in ledger['aircraft'].items()},
        'total500': {scale: values['failures'] for scale, values in ledger['totals500'].items()},
        'date': {scale: values['failures'] for scale, values in ledger['dates'].items()},
        'carrier': {scale: values['failures'] for scale, values in ledger['carriers'].items()},
        'flightNumber': {scale: values['failures'] for scale, values in ledger['flightNumbers'].items()},
    },
    'derived': derived,
}

(ROOT / 'T020-logmate-preimplementation-type-contract-results.json').write_text(
    json.dumps(result, ensure_ascii=False, indent=2),
    encoding='utf-8',
)
print(json.dumps(result, ensure_ascii=False, indent=2))
