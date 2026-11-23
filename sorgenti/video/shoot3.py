import sys, os, json
from playwright.sync_api import sync_playwright
h=open('anim3.html').read().replace('JSON.parse(DATA_JSON)', open('data2.json').read()).replace('NEON_JSON', open('neon2.json').read())
open('page3.html','w').write(h)
mode=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    errs=[]; pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: errs.append(m.text))
    pg.goto('file://'+os.path.abspath('page3.html')); pg.wait_for_timeout(800)
    if mode=='test':
        os.makedirs('t3',exist_ok=True)
        for t in [float(x) for x in sys.argv[2].split(',')]:
            pg.evaluate(f'renderAt({t})'); pg.screenshot(path=f't3/{t:05.2f}.png')
    else:
        fps=int(sys.argv[2]); dur=float(sys.argv[3]); os.makedirs('fr3',exist_ok=True)
        a,bb=int(sys.argv[4]),int(sys.argv[5])
        for i in range(a,min(bb,int(dur*fps))):
            pg.evaluate(f'renderAt({i/fps})'); pg.screenshot(path=f'fr3/f{i:05d}.jpg',type='jpeg',quality=94)
    b.close(); print(errs[:5])
