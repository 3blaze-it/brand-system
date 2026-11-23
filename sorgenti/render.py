import sys, os
from playwright.sync_api import sync_playwright
def render(html, png=None, pdf=None, w=1600, h=1131, scale=1, wait=600, full=True):
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':w,'height':h}, device_scale_factor=scale)
        pg.goto('file://'+os.path.abspath(html)); pg.evaluate('document.fonts.ready.then(()=>1)'); pg.wait_for_timeout(wait)
        if png: pg.screenshot(path=png, full_page=full)
        if pdf: pg.pdf(path=pdf, prefer_css_page_size=True, print_background=True)
        b.close()
if __name__=='__main__':
    render(sys.argv[1], png=sys.argv[2] if len(sys.argv)>2 and sys.argv[2]!='-' else None, pdf=sys.argv[3] if len(sys.argv)>3 else None, w=int(sys.argv[4]) if len(sys.argv)>4 else 1600, h=int(sys.argv[5]) if len(sys.argv)>5 else 1131)
