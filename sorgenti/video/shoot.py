import json, sys, os
from playwright.sync_api import sync_playwright
d=open('data.json').read()
h=open('anim.html').read().replace('JSON.parse(DATA_JSON)', d)
open('page.html','w').write(h)
times=[float(x) for x in sys.argv[2].split(',')] if len(sys.argv)>2 else None
mode=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://'+os.path.abspath('page.html')); pg.wait_for_timeout(800)
    msgs=[]; pg.on('console', lambda m: msgs.append(m.text))
    if mode=='test':
        for t in times:
            pg.evaluate(f'renderAt({t})'); pg.screenshot(path=f'test_{t:05.2f}.png')
    else:
        os.makedirs('frames',exist_ok=True); fps=30; N=int(22*fps)
        for i in range(N):
            pg.evaluate(f'renderAt({i/fps})'); pg.screenshot(path=f'frames/f{i:04d}.jpg', type='jpeg', quality=95)
    b.close(); print(msgs[:5])
