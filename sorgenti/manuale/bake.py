"""Rende il manuale: il Liquid Glass (rifrazione reale, solo Chromium a schermo) viene 'cotto'
in immagine ad alta risoluzione per ogni superficie di vetro, poi tutto il resto esce vettoriale nel PDF."""
import base64, sys, os
from playwright.sync_api import sync_playwright

def bake(html_path, pdf_path, png_dir=None, scale=2.4, preview_pages=None):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1123, 'height': 794}, device_scale_factor=scale)
        pg.goto('file://' + os.path.abspath(html_path))
        pg.evaluate('document.fonts.ready.then(()=>1)')
        pg.wait_for_timeout(1500)
        pg.evaluate('LiquidGlass.init()')
        pg.wait_for_timeout(1500)
        n = pg.evaluate('document.querySelectorAll("[data-lg]").length')
        print('superfici di vetro:', n)
        for i in range(n):
            box = pg.evaluate('''(i)=>{const e=document.querySelectorAll("[data-lg]")[i]; e.classList.add("snap");
                const r=e.getBoundingClientRect(); return {x:r.left+scrollX, y:r.top+scrollY, w:r.width, h:r.height}}''', i)
            if box['w'] < 2 or box['h'] < 2: continue
            pg.evaluate('(y)=>window.scrollTo(0, Math.max(0, y-200))', box['y'])
            pg.wait_for_timeout(60)
            shot = pg.screenshot(clip={'x': box['x'], 'y': box['y'], 'width': box['w'], 'height': box['h']}, full_page=True, type='png')
            url = 'data:image/png;base64,' + base64.b64encode(shot).decode()
            pg.evaluate('''([i,u])=>{const e=document.querySelectorAll("[data-lg]")[i];
                e.style.backgroundImage="url("+u+")"; e.style.backgroundSize="100% 100%"; e.style.backgroundColor="transparent";
                e.classList.add("lg--baked"); e.classList.remove("snap");
                e.style.setProperty("background-color","transparent","important");}''', [i, url])
        # rimuove backdrop residui
        pg.evaluate('document.querySelectorAll(".lg--baked").forEach(e=>{e.style.backdropFilter="none";e.style.webkitBackdropFilter="none"})')
        if png_dir:
            os.makedirs(png_dir, exist_ok=True)
            total = pg.evaluate('document.querySelectorAll(".page").length')
            pages = preview_pages or range(total)
            pg.set_viewport_size({'width': 1123, 'height': 794})
            for k in pages:
                y = k * 794
                pg.screenshot(path=f'{png_dir}/p{k+1:03d}.jpg', clip={'x': 0, 'y': y, 'width': 1123, 'height': 794}, full_page=True, type='jpeg', quality=70)
        pg.emulate_media(media='print')
        pg.pdf(path=pdf_path, prefer_css_page_size=True, print_background=True)
        b.close()

if __name__ == '__main__':
    bake(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
