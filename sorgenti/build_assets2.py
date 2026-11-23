"""Asset aggiuntivi 3blaze 2027: badge, cartellina, wayfinding, grafiche video, sfondi call, icone app."""
import os, json
from build_print import logo, flame, doc, HEAD, B, CREAM, BLACK, OR, TEAL, WINE, MUTED_L, MUTED_D, CO
from render import render
from build_scene import scene, ROWS, logo_img
O=B+'/out/print'
TEAL_L='#3FA9BA'; WINE_L='#D98C99'
DIVS=[('media','3blaze',BLACK,CREAM,'3blaze_symbol'),('academy','academy',OR,BLACK,'3blaze_academy'),
      ('news','.net',TEAL,CREAM,'3blaze_net'),('ia','luisa',WINE,CREAM,'luisa')]

# ---------- BADGE 85x120 (con foro asola) ----------
def badges():
    css=f'''.bd{{color:{CREAM}}}
.bd .slot{{position:absolute;left:50%;top:6mm;width:14mm;height:3.2mm;margin-left:-7mm;border-radius:2mm;background:#FFFFFF;box-shadow:inset 0 0 0 .3mm #0003}}
.bd .lg{{position:absolute;left:8mm;top:16mm;height:7mm}}
.bd .role{{position:absolute;left:8mm;right:8mm;top:44mm;font:400 15mm/0.9 '3blaze Display'}}
.bd .name{{position:absolute;left:8mm;right:8mm;bottom:24mm;font-size:6.2mm;line-height:1.1}}
.bd .org{{position:absolute;left:8mm;bottom:19mm;font-size:3.4mm;font-style:italic;opacity:.75}}
.bd .foot{{position:absolute;left:8mm;right:8mm;bottom:8mm;display:flex;justify-content:space-between;font-size:2.3mm}}
.bd .band{{position:absolute;left:0;right:0;bottom:0;height:4mm}}'''
    pages=''
    for role,bg,ink,band in [('STAFF',BLACK,CREAM,OR),('SPEAKER',OR,BLACK,BLACK),('PRESS',TEAL,CREAM,CREAM),('VISITOR',CREAM,BLACK,OR),('DOCENTE',OR,BLACK,CREAM),('TEAM',WINE,CREAM,OR)]:
        lg = '3blaze_academy' if role=='DOCENTE' else '3blaze_logo_horizontal'
        pages+=f'''<section class="page bd" style="background:{bg};color:{ink}"><div class="slot"></div>
<div class="lg">{logo(lg,ink,'height:7mm;width:auto')}</div><div class="role">{role}</div>
<div class="name">Nome<br>Cognome</div><div class="org">Azienda / Ruolo</div>
<div class="foot mono"><span>Evento 2027</span><span style="text-transform:none">3blaze.it</span></div><div class="band" style="background:{band}"></div></section>'''
    return doc('badge_evento_85x120', css, pages, 85, 120, 850)

# ---------- BADGE DIPENDENTE (CR80 54x85.6 verticale) ----------
def id_badge():
    css=f'''.id{{background:{BLACK};color:{CREAM}}}
.id .ph{{position:absolute;left:6mm;top:16mm;width:22mm;height:28mm;background:#2a2a2a;border-radius:0 0 6mm 6mm;overflow:hidden}}
.id .ph span{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:2mm;color:#777}}
.id .sym{{position:absolute;left:6mm;top:6mm;width:14mm}}
.id .n{{position:absolute;left:6mm;top:49mm;font-size:4.2mm;line-height:1.15}}
.id .r{{position:absolute;left:6mm;top:59mm;font-size:2.6mm;font-style:italic;color:{MUTED_D}}}
.id .m{{position:absolute;left:6mm;bottom:6mm;font-size:1.9mm;color:{MUTED_D}}}
.id .fl{{position:absolute;right:-6mm;bottom:-10mm;width:26mm;opacity:.18}}
.id .back{{position:absolute;inset:0;background:url({B}/out/scene/prisma_flame.png) center/cover}}'''
    p=f'''<section class="page id"><div class="sym">{logo('3blaze_symbol',CREAM)}</div><div class="ph"><span class="mono">FOTO</span></div>
<div class="n">Nome<br>Cognome</div><div class="r">Ruolo — divisione</div><div class="m mono">ID 0000 · valido 2027</div><div class="fl">{flame(OR)}</div></section>
<section class="page id"><div class="back"></div><div class="m mono" style="text-transform:none;color:{CREAM}">Se trovato: {CO["mail"]}</div></section>'''
    return doc('badge_dipendente_CR80_54x86', css, p, 54, 85.6, 540)

# ---------- CARTELLINA A4 (stesa 470x330 con alette) semplificata: fronte+retro 2 pagine 220x310 ----------
def folder():
    css=f'''.fo{{background:{BLACK};color:{CREAM}}}
.fo .sym{{position:absolute;left:20mm;top:22mm;width:38mm}}
.fo .lg{{position:absolute;left:20mm;bottom:20mm;width:70mm}}
.fo .url{{position:absolute;right:20mm;bottom:21mm;font-size:3mm;color:{MUTED_D};text-transform:none}}
.fi{{background:url({B}/out/scene/prisma_hero.png) center/cover}}
.fi .pocket{{position:absolute;left:0;right:0;bottom:0;height:100mm;background:{BLACK};border-radius:0 30mm 0 0}}
.fi .card{{position:absolute;right:30mm;bottom:70mm;width:85mm;height:55mm;border:.3mm dashed {MUTED_D};border-radius:2mm}}
.fi .card span{{position:absolute;left:3mm;top:2mm;font-size:2mm;color:{MUTED_D}}}'''
    p=f'''<section class="page fo"><div class="sym">{logo('3blaze_symbol',CREAM)}</div><div class="lg">{logo('3blaze_logo_claim',CREAM)}</div><div class="url mono">3blaze.it</div></section>
<section class="page fi"><div class="pocket"></div><div class="card"><span class="mono">fustella biglietto 85×55</span></div></section>'''
    return doc('cartellina_A4_fronte_interno_220x310', css, p, 220, 310, 1100)

# ---------- WAYFINDING interno ----------
def wayfinding():
    css=f'''.wf{{background:{BLACK};color:{CREAM}}}
.wf .num{{position:absolute;left:14mm;top:12mm;font-size:5mm;color:{MUTED_D}}}
.wf .t{{position:absolute;left:14mm;top:30mm;font-size:16mm;line-height:1}}
.wf .s{{position:absolute;left:14mm;top:50mm;font-size:5.4mm;font-style:italic;color:{MUTED_D}}}
.wf .ar{{position:absolute;right:14mm;top:22mm;width:30mm;height:30mm}}
.wf .bar{{position:absolute;left:0;bottom:0;height:6mm;right:0}}
.wf .fl{{position:absolute;left:14mm;bottom:14mm;width:7mm}}'''
    arrow=lambda rot,c: f'<svg class="ar" viewBox="0 0 100 100" style="transform:rotate({rot}deg)"><path d="M10 50 H80 M55 22 L84 50 L55 78" fill="none" stroke="{c}" stroke-width="9" stroke-linecap="square"/></svg>'
    pages=''
    for n,t,s,rot,bar in [('01','Studio media','Produzione · Sala posa',0,BLACK),('02','Aula academy','Corsi e workshop',90,OR),('03','Redazione .net','News e matchday',180,TEAL),('04','luisa lab','Intelligenza artificiale',270,WINE),('WC','Servizi','',0,'#333')]:
        pages+=f'''<section class="page wf"><div class="num mono">{n}</div><div class="t">{t}</div><div class="s">{s}</div>{arrow(rot,CREAM)}
<div class="fl">{flame(OR if bar==BLACK else CREAM)}</div><div class="bar" style="background:{bar if bar!=BLACK else OR}"></div></section>'''
    return doc('wayfinding_interno_300x100', css, pages, 300, 100, 1500)

# ---------- MERCH (piatti vettoriali) ----------
TEE='M30 8 L52 2 Q60 10 68 2 L90 8 L112 26 L98 40 L88 32 L88 118 L32 118 L32 32 L22 40 L8 26 Z'
# ---------- VIDEO: lower third + end card (1920x1080, PNG) ----------
def video():
    css=f'''.v{{background:transparent}}
.v .lt{{position:absolute;left:96px;bottom:110px;display:flex;align-items:stretch}}
.v .lt .f{{width:28px;background:{OR};border-radius:0 0 14px 14px}}
.v .lt .tx{{background:{BLACK}e6;padding:18px 28px 20px;color:{CREAM}}}
.v .lt .n{{font-size:44px;line-height:1}} .v .lt .r{{font-size:24px;font-style:italic;color:{MUTED_D};margin-top:8px}}
.v .bug{{position:absolute;right:72px;top:60px;width:180px;opacity:.9}}
.ec{{background:{BLACK}}} .ec .img{{position:absolute;inset:0;background:url({B}/out/scene/prisma_hero.png) center/cover}}
.ec .u{{position:absolute;left:0;right:0;bottom:120px;text-align:center;font-size:30px;color:{CREAM};text-transform:none}}'''
    def png(name, body, transparent=False):
        html=HEAD+css+f'@page{{size:1920px 1080px;margin:0}} html,body{{width:1920px;height:1080px;background:{"transparent" if transparent else "#000"}}} .page{{width:1920px;height:1080px}}</style></head><body>'+body+'</body></html>'
        f=f'{O}/{name}.html'; open(f,'w').write(html)
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p_:
            b=p_.chromium.launch(); pg=b.new_page(viewport={'width':1920,'height':1080})
            pg.goto('file://'+f); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(700)
            pg.screenshot(path=f'{O}/{name}.png', omit_background=transparent); b.close()
    png('video_lower_third_1920x1080', f'''<section class="page v"><div class="lt"><div class="f"></div><div class="tx"><div class="n">Nome Cognome</div><div class="r">Ruolo — 3blaze media</div></div></div>
<div class="bug">{logo('3blaze_logo_horizontal',CREAM)}</div></section>''', True)
    png('video_end_card_1920x1080', f'''<section class="page ec"><div class="img"></div><div style="position:absolute;left:50%;bottom:190px;width:300px;margin-left:-150px">{logo('3blaze_claim',CREAM)}</div><div class="u mono">3blaze.it</div></section>''')

# ---------- SFONDI CALL (Zoom/Teams/Meet) ----------
def call_bg():
    for key,label,bg,ink,lg in DIVS:
        html=HEAD+f'''@page{{size:1920px 1080px;margin:0}} html,body{{width:1920px;height:1080px;background:{bg}}}
.l{{position:absolute;right:96px;top:80px;width:{'420px' if lg!='luisa' else '200px'}}} .r{{position:absolute;right:96px;bottom:70px;font-size:22px;color:{ink};opacity:.7;text-transform:none}}
.f{{position:absolute;left:-80px;bottom:-260px;width:620px;opacity:.07}}</style></head><body>
<div class="f">{flame(ink)}</div><div class="l">{logo(lg if lg!='3blaze_symbol' else '3blaze_logo_horizontal',ink)}</div><div class="r mono">3blaze.it</div></body></html>'''
        f=f'{O}/sfondo_call_{key}.html'; open(f,'w').write(html)
        render(f, png=f'{O}/sfondo_call_{key}_1920x1080.png', w=1920, h=1080, full=False)

# ---------- ICONE APP / FAVICON ----------
def icons():
    import cairosvg
    from PIL import Image
    os.makedirs(B+'/out/icons',exist_ok=True)
    d=json.load(open(B+'/logo_assets.json'))
    fl=d['3blaze_flame']['d']; sy=d['3blaze_symbol']['d']
    variants={
      'favicon': f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-110 -10 700 720"><rect x="-110" y="-10" width="700" height="720" rx="140" fill="#000"/><path fill="#FDF6E2" d="{fl}"/></svg>',
      'app_media': f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><rect width="1024" height="1024" fill="#000"/><g transform="translate(144 380) scale(.4)"><path fill="#FDF6E2" d="{sy}"/></g></svg>',
      'app_academy': f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><rect width="1024" height="1024" fill="#FB4F31"/><g transform="translate(144 380) scale(.4)"><path fill="#000" d="{sy}"/></g></svg>',
      'app_news': f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><rect width="1024" height="1024" fill="#006172"/><g transform="translate(144 380) scale(.4)"><path fill="#FDF6E2" d="{sy}"/></g></svg>',
      'app_luisa': f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><rect width="1024" height="1024" fill="#4D1821"/><g transform="translate(332 237) scale(.75)"><path fill="#FDF6E2" d="{fl}"/></g></svg>',
    }
    for n,s in variants.items():
        open(f'{B}/out/icons/{n}.svg','w').write(s)
        sizes=[16,32,48,180,192,512] if n=='favicon' else [1024]
        for z in sizes: cairosvg.svg2png(bytestring=s.encode(), write_to=f'{B}/out/icons/{n}_{z}.png', output_width=z, output_height=z)
    Image.open(f'{B}/out/icons/favicon_48.png').save(f'{B}/out/icons/favicon.ico', sizes=[(16,16),(32,32),(48,48)])

if __name__=='__main__':
    import sys
    w=sys.argv[1] if len(sys.argv)>1 else 'all'
    for k,fn in [('badge',badges),('id',id_badge),('folder',folder),('wf',wayfinding),('video',video),('call',call_bg),('icons',icons)]:
        if w in (k,'all'): fn(); print('ok',k)
