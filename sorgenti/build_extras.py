import os, json, io
from build_print import doc, logo, flame, B, CREAM, BLACK, OR, TEAL, WINE, MUTED_L, MUTED_D, CO
from render import render
import cairosvg
from PIL import Image
O=B+'/out/extra'; os.makedirs(O,exist_ok=True)

# ---------- BADGE EVENTI 90x130 mm (fronte/retro) ----------
ROLES=[('STAFF',BLACK,CREAM,'3blaze'),('SPEAKER',OR,BLACK,'3blaze academy'),('OSPITE',CREAM,BLACK,'3blaze'),('STAMPA',TEAL,CREAM,'3blaze .net'),('LUISA LAB',WINE,CREAM,'luisa')]
def badges():
    css=f'''.bd{{background:#111;color:{CREAM}}}
.bd .slot{{position:absolute;left:50%;top:7mm;transform:translateX(-50%);width:16mm;height:3.4mm;border-radius:2mm;background:#ffffff;box-shadow:inset 0 0 0 .3mm #00000033}}
.bd .lg{{position:absolute;left:9mm;top:17mm;width:40mm}}
.bd .ev{{position:absolute;right:9mm;top:18mm;text-align:right;font-size:5.6pt;line-height:1.6;opacity:.8}}
.bd .name{{position:absolute;left:9mm;right:9mm;top:52mm;font-size:21pt;line-height:1.02}}
.bd .org{{position:absolute;left:9mm;top:79mm;font-size:9pt;font-style:italic;opacity:.75}}
.bd .role{{position:absolute;left:0;right:0;bottom:0;height:34mm;border-radius:0 0 14mm 14mm;display:flex;align-items:center;padding-left:9mm;
  font:400 25pt/1 '3blaze Display'}}
.bd .qr{{position:absolute;right:9mm;bottom:41mm;width:15mm;height:15mm;border:.3mm dashed currentColor;opacity:.5;font-size:4.5pt;display:flex;align-items:center;justify-content:center;text-align:center}}
.bk{{background:url({B}/out/scene/prisma_flame.png) center/cover}}
.bk .slot{{position:absolute;left:50%;top:7mm;transform:translateX(-50%);width:16mm;height:3.4mm;border-radius:2mm;background:#fff}}
.bk .cap{{position:absolute;left:0;right:0;bottom:9mm;text-align:center}}
.bk .cap span{{display:inline-block;background:#000000D0;color:{CREAM};border-radius:99px;padding:2mm 5mm;font-size:6pt}}'''
    pages=''
    for role,bg,ink,div in ROLES:
        key={'3blaze':'3blaze_logo_horizontal','3blaze academy':'3blaze_academy','3blaze .net':'3blaze_net','luisa':'luisa'}[div]
        lgcol=CREAM if bg!=CREAM else CREAM
        pages+=f'''<section class="page bd"><div class="slot"></div>
<div class="lg">{logo(key, OR if div=="3blaze academy" else ('#3FA9BA' if div=="3blaze .net" else ('#D98C99' if div=="luisa" else CREAM)), 'width:100%')}</div>
<div class="ev mono">NOME EVENTO<br>GG.MM.2027 · TERNI</div>
<div class="name">Nome<br>Cognome</div><div class="org">Azienda / ruolo</div>
<div class="qr mono" style="color:{CREAM}">QR<br>ACCREDITO</div>
<div class="role" style="background:{bg};color:{ink};{'box-shadow:inset 0 0 0 .4mm #00000014' if bg==CREAM else ''}">{role}</div></section>'''
    pages+=f'<section class="page bk"><div class="slot"></div><div class="cap"><span class="mono" style="text-transform:none">3blaze.it</span></div></section>'
    return doc('badge_evento_90x130mm', css, pages, 90, 130, 900).replace('print','print')

# ---------- LANYARD 20 x 900 mm (pattern) ----------
def lanyard():
    css=f'''.ly{{background:{BLACK};display:flex;flex-direction:column;align-items:center;gap:22mm;padding-top:12mm}}
.ly svg{{width:12mm}} .ly .w{{transform:rotate(90deg);width:40mm;margin:14mm 0}}'''
    items=''.join((f'<div>{logo("3blaze_symbol",CREAM,"width:12mm")}</div>' if i%2==0 else f'<div class="w">{logo("3blaze_wordmark",OR,"width:40mm")}</div>') for i in range(14))
    return doc('lanyard_20x900mm', css, f'<section class="page ly">{items}</section>', 20, 900, 200)

# ---------- COPERTINA DOCUMENTO A4 verticale ----------
def doc_cover():
    css=f'''.dc{{background:{BLACK};color:{CREAM}}}
.dc .img{{position:absolute;left:0;right:0;top:0;height:150mm;background:url({B}/out/scene/prisma_flame.png) center 35%/cover}}
.dc .img::after{{content:'';position:absolute;left:0;right:0;bottom:0;height:50mm;background:linear-gradient(transparent,{BLACK})}}
.dc .lab{{position:absolute;left:18mm;top:160mm;font-size:7pt;color:{MUTED_D}}}
.dc h1{{position:absolute;left:18mm;right:18mm;top:170mm;font:500 30pt/1.08 '3blaze Sans';margin:0}}
.dc .sub{{position:absolute;left:18mm;top:212mm;font-size:12pt;font-style:italic;color:{MUTED_D}}}
.dc .lgo{{position:absolute;left:18mm;bottom:16mm;width:55mm}} .dc .dt{{position:absolute;right:18mm;bottom:17mm;font-size:7pt;color:{MUTED_D}}}'''
    b=f'''<section class="page dc"><div class="img"></div><div class="lab mono">DOCUMENTO · RISERVATO</div>
<h1>Titolo del documento<br>su due righe</h1><div class="sub">Sottotitolo o cliente</div>
<div class="lgo">{logo('3blaze_logo_horizontal',CREAM)}</div><div class="dt mono">GENNAIO 2027 · V1.0</div></section>'''
    return doc('copertina_documento_A4', css, b, 210, 297, 1240)

# ---------- SFONDI VIDEOCHIAMATA ----------
def vbgs():
    for name,bg,col,wordcol in [('vbg_nero',BLACK,CREAM,MUTED_D),('vbg_crema',CREAM,BLACK,MUTED_L)]:
        css=f'''.v{{background:{bg}}} .v .l{{position:absolute;right:28mm;bottom:22mm;width:70mm}} .v .t{{position:absolute;left:28mm;bottom:24mm;font-size:5mm;color:{wordcol}}}'''
        doc(name, css, f'<section class="page v"><div class="l">{logo("3blaze_logo_horizontal",col)}</div><div class="t mono">media · academy · news · ia</div></section>', 508, 285.75, 1920)

# ---------- ICONE APP / FAVICON ----------
def icons():
    os.makedirs(O+'/icone',exist_ok=True)
    fl=json.load(open(B+'/logo_assets.json'))['3blaze_flame']['d']
    def icon_svg(bg, fg, radius=True):
        r='rx="230"' if radius else ''
        # fiamma alta 56% del quadrato, centrata otticamente
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><rect width="1024" height="1024" {r} fill="{bg}"/><g transform="translate(348 222) scale(0.6833)"><path fill="{fg}" d="{fl}"/></g></svg>'
    sets={'3blaze':(BLACK,CREAM),'academy':(OR,BLACK),'net':(TEAL,CREAM),'luisa':(WINE,CREAM)}
    for k,(bg,fg) in sets.items():
        sq=icon_svg(bg,fg,False); open(f'{O}/icone/{k}_icona.svg','w').write(icon_svg(bg,fg,True))
        for s in [16,32,48,180,192,512,1024]:
            cairosvg.svg2png(bytestring=sq.encode(), write_to=f'{O}/icone/{k}_{s}.png', output_width=s, output_height=s)
    Image.open(f'{O}/icone/3blaze_48.png').save(f'{O}/icone/favicon.ico', sizes=[(16,16),(32,32),(48,48)])
    # avatar social per divisione
    os.makedirs(O+'/avatar',exist_ok=True)
    keys={'3blaze':'3blaze_symbol','academy':'3blaze_symbol','net':'3blaze_symbol','luisa':'luisa'}
    A=json.load(open(B+'/logo_assets.json'))
    for k,(bg,fg) in sets.items():
        a=A[keys[k]]; x,y,w,h=a['viewBox']; tw=0.62*1080; th=tw*h/w; tx=(1080-tw)/2; ty=(1080-th)/2
        s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080"><rect width="1080" height="1080" fill="{bg}"/><g transform="translate({tx} {ty}) scale({tw/w}) translate({-x} {-y})"><path fill="{fg}" d="{a["d"]}"/></g></svg>'
        cairosvg.svg2png(bytestring=s.encode(), write_to=f'{O}/avatar/avatar_{k}_1080.png', output_width=1080)

if __name__=='__main__':
    import shutil
    badges(); lanyard(); doc_cover(); vbgs(); icons()
    for f in os.listdir(B+'/out/print'):
        if f.startswith(('badge_','lanyard_','copertina_documento','vbg_')): shutil.move(B+'/out/print/'+f, O+'/'+f)
    print(sorted(os.listdir(O)))
