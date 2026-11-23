"""Scena Prisma 2027: logo 3blaze ripetuto a bassa opacità + oggetto di vetro reale (pannello, fiamma o simbolo a tre fiamme)."""
import json, os, sys
from render import render
B='/home/claude/brand'
P=json.load(open(B+'/parts.json'))
LOGO=json.load(open(B+'/logo_assets.json'))

def pattern(w, h, lh=None, opacity=1, color=None, key=None, pos='center'):
    """Trama Vetro 2027: '3blaze' in vetro gigante su Nero (file in out/trama), scelto per formato."""
    r=w/h; f='16x9' if r>1.25 else ('1x1' if r>0.8 else '9x16')
    return f'<div class="bg" style="opacity:{opacity};background:#000 url(file://{B}/out/trama/3blaze_trama_vetro_{f}.jpg) {pos}/cover"></div>'

def scene(name, w, h, rows, size, glass, ground='#000', scale=2, rule=None, offset=0, extra='', opacity=0.17, ink='#FDF6E2'):
    import zlib; rows_html=pattern(w, h, pos=['30% 40%','70% 25%','20% 75%','80% 60%','50% 50%','60% 85%','10% 20%'][zlib.crc32(name.encode())%7])
    g=''
    for gl in glass:
        st=f'left:{gl["x"]}px;top:{gl["y"]}px;width:{gl["w"]}px;height:{gl["h"]}px' + (f';background:{gl["tint"]}' if gl.get('tint') else '')
        attrs=f'data-lg-bezel="{gl.get("bezel",40)}" data-lg-scale="{gl.get("scale",70)}" data-lg-dispersion="{gl.get("disp",0.22)}" data-lg-blur="{gl.get("blur",1.2)}"'
        shp=gl.get('shape')
        if shp=='flame':
            attrs+=f' data-lg-path="{P["flame"]}" data-lg-viewbox="0 0 480 700"'
        elif shp=='symbol':
            vb=LOGO['3blaze_symbol']['viewBox']; attrs+=f' data-lg-path="{LOGO["3blaze_symbol"]["d"]}" data-lg-viewbox="{vb[0]} {vb[1]} {vb[2]} {vb[3]}"'
        else:
            attrs+=f' data-lg-radius="{gl.get("radius",32)}"'
        inner=gl.get('html','')
        g+=f'<div class="glass" style="{st}" data-lg {attrs}>{inner}</div>'
        if shp in ('flame','symbol'):
            pd = P["flame"] if shp=='flame' else LOGO['3blaze_symbol']['d']; vbs = '0 0 480 700' if shp=='flame' else ' '.join(str(v) for v in LOGO['3blaze_symbol']['viewBox'])
            g+=(f'<svg class="rim" viewBox="{vbs}" preserveAspectRatio="none" style="{st};position:absolute;overflow:visible;mix-blend-mode:screen">'
                '<defs><linearGradient id="pr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF4F31"/><stop offset=".2" stop-color="#FFD23F"/>'
                '<stop offset=".4" stop-color="#3DDC97"/><stop offset=".6" stop-color="#2EC4FF"/><stop offset=".8" stop-color="#7B61FF"/><stop offset="1" stop-color="#FF5FA2"/></linearGradient></defs>'
                f'<path d="{pd}" fill="none" stroke="url(#pr)" stroke-width="3" vector-effect="non-scaling-stroke" opacity=".7"/></svg>')
    html=f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="{B}/out/code/tokens.css"><link rel="stylesheet" href="{B}/out/code/liquid-glass.css">
<style>
@font-face{{font-family:'3blaze Display';src:url({B}/out/fonts/3blazeDisplay-Regular.woff2)}}
@font-face{{font-family:'3blaze Sans';src:url({B}/out/fonts/3blazeSans-Regular.woff2)}}
html,body{{margin:0;background:{ground};width:{w}px;height:{h}px;overflow:hidden}}
.bg{{position:absolute;inset:0;overflow:hidden}}
.row{{font:400 {size}px/1.02 '3blaze Display';white-space:nowrap;border-top:1px solid {rule};padding-top:.02em}}
.glass{{position:absolute}}
</style></head><body><div class="bg">{rows_html}</div>{extra}{g}
<script src="{B}/out/code/liquid-glass.js"></script></body></html>'''
    os.makedirs(B+'/out/scene',exist_ok=True)
    f=f'{B}/out/scene/{name}.html'; open(f,'w').write(html)
    render(f, png=f"{B}/out/scene/{name}.png", w=w, h=h, scale=scale, wait=1800, full=False)
    return f'{B}/out/scene/{name}.png'

def logo_img(key, color='#FDF6E2', style=''):
    vb=LOGO[key]['viewBox']; d=LOGO[key]['d']
    return f'<svg viewBox="{vb[0]} {vb[1]} {vb[2]} {vb[3]}" style="position:absolute;{style}"><path fill="{color}" d="{d}"/></svg>'

CREAM='#FDF6E2'; OR='#FB4F31'; TEAL_L='#3FA9BA'; WINE_L='#D98C99'; STONE='#A8A294'
ROWS=[('MEDIA',CREAM),('ACADEMY',OR),('.NET',TEAL_L),('LUISA',WINE_L),('HOLDING',STONE),('2027',CREAM)]

if __name__=='__main__':
    which=sys.argv[1] if len(sys.argv)>1 else 'all'
    if which in ('hero','all'):
        # hero 16:9 — pannello vetro con logo
        scene('prisma_hero',1600,900,ROWS[:5],180,[{"x":360,"y":250,"w":880,"h":400,"radius":64,"bezel":60,"scale":90,"blur":1.4,
              "html":logo_img('3blaze_logo_horizontal',CREAM,'left:110px;top:150px;width:660px')}],scale=2)
    if which in ('flame','all'):
        scene('prisma_flame',1200,1500,ROWS,170,[{"x":100,"y":500,"w":1000,"h":380,"shape":"symbol","bezel":50,"scale":120,"disp":0.32,"blur":0.8}],scale=2)
    if which in ('linkedin','all'):
        scene('linkedin',1584,396,ROWS[:4],110,[{"x":800,"y":88,"w":560,"h":220,"radius":40,"bezel":40,"scale":70,
              "html":logo_img('3blaze_logo_horizontal',CREAM,'left:70px;top:80px;width:420px')}],scale=2)
    if which in ('card','all'):
        # retro biglietto 91x61mm (con abbondanza) @ 12px/mm
        scene('card_back',1092,732,ROWS[:5],150,[{"x":166,"y":226,"w":760,"h":289,"shape":"symbol","bezel":36,"scale":70}],scale=3)
