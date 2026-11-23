"""Stampati e cartellonistica 3blaze 2027 → HTML → PDF vettoriale (Chromium) + anteprime PNG."""
import json, os
from render import render
B='/home/claude/brand'; O=B+'/out/print'; os.makedirs(O,exist_ok=True)
L=json.load(open(B+'/logo_assets.json'))
CREAM='#FDF6E2'; BLACK='#000000'; OR='#FB4F31'; TEAL='#006172'; WINE='#4D1821'; MUTED_L='#6B665C'; MUTED_D='#A8A294'

CO={ "ragione":"3BLAZE S.R.L.S.", "sede":"Strada Valle Verde 6, 05100 Terni (TR)", "mail":"ciao@3blaze.it", "web":"3blaze.it",
     "piva":"P.IVA 00000000000", "pec":"PEC da inserire", "tel":"+39 000 000 0000" }

def logo(key, color, css=''):
    x,y,w,h=L[key]['viewBox']
    return f'<svg class="lg-{key}" viewBox="{x} {y} {w} {h}" style="aspect-ratio:{w}/{h};{css}" aria-label="{L[key]["title"]}"><path fill="{color}" d="{L[key]["d"]}"/></svg>'

def flame(color, css=''):
    return logo('3blaze_flame', color, css)

HEAD=f'''<!doctype html><html lang="it"><head><meta charset="utf-8">
<style>
@font-face{{font-family:'3blaze Sans';src:url({B}/out/fonts/3blazeSans-Regular.woff2);font-weight:500}}
@font-face{{font-family:'3blaze Sans';src:url({B}/out/fonts/3blazeSans-Italic.woff2);font-style:italic;font-weight:500}}
@font-face{{font-family:'3blaze Display';src:url({B}/out/fonts/3blazeDisplay-Regular.woff2)}}
@font-face{{font-family:'JetBrains Mono';src:url({B}/out/fonts/JetBrainsMono-Medium.woff2);font-weight:500}}
@font-face{{font-family:'JetBrains Mono';src:url({B}/out/fonts/JetBrainsMono-Regular.woff2);font-weight:400}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:'3blaze Sans',sans-serif;font-weight:500}}
.mono{{font-family:'JetBrains Mono',monospace;font-weight:500;text-transform:uppercase;letter-spacing:.12em}}
.page{{position:relative;overflow:hidden;page-break-after:always;break-after:page}}
.page:last-child{{page-break-after:auto;break-after:auto}}
svg{{display:block}}
'''

def doc(name, css, body, page_w, page_h, png_w=1400):
    html=HEAD+f'@page{{size:{page_w}mm {page_h}mm;margin:0}} .page{{width:{page_w}mm;height:{page_h}mm}}'+css+'</style></head><body>'+body+'</body></html>'
    f=f'{O}/{name}.html'; open(f,'w').write(html)
    pxw=png_w; pxh=int(png_w*page_h/page_w)
    render(f, png=f'{O}/{name}.png', pdf=f'{O}/{name}.pdf', w=int(page_w*3.7795), h=int(page_h*3.7795), scale=pxw/(page_w*3.7795), wait=900)
    return f

DIV=[('media',BLACK,'3blaze'),('academy',OR,'academy'),('news',TEAL,'.net'),('ia',WINE,'luisa')]

# ---------------- CARTA INTESTATA A4 ----------------
def letterhead(variant='bianco'):
    bg = '#FFFFFF' if variant=='bianco' else CREAM
    css=f'''
.lh{{background:{bg};color:{BLACK}}}
.lh .logo{{position:absolute;left:20mm;top:17mm;width:52mm}}
.lh .meta{{position:absolute;right:20mm;top:17.6mm;text-align:right;font-size:6.6pt;line-height:1.55;color:{MUTED_L}}}
.lh .meta b{{color:{BLACK};font-weight:500}}
.lh .fold{{position:absolute;left:7mm;width:4mm;border-top:.25pt solid #B9B2A2}}
.lh .body{{position:absolute;left:30mm;right:30mm;top:62mm;font-size:10pt;line-height:1.6}}
.lh .body .to{{margin-left:95mm;margin-bottom:12mm;font-size:10pt;line-height:1.5}}
.lh .body .obj{{font-style:italic;margin:8mm 0 6mm}}
.lh .body p{{margin-bottom:3.6mm;max-width:150mm}}
.lh .sig{{margin-top:10mm}}
.lh .foot{{position:absolute;left:20mm;right:20mm;bottom:12mm;display:grid;grid-template-columns:1.25fr 1fr 1fr 1.5fr;gap:6mm;
  border-top:.4pt solid #00000026;padding-top:3.2mm;font-size:5.9pt;line-height:1.6;color:{MUTED_L}}}
.lh .foot b{{color:{BLACK};font-weight:500}}
.lh .divs{{display:flex;gap:3.2mm;justify-content:flex-end;align-items:center}}
.lh .divs span{{display:flex;align-items:center;gap:1.1mm}}
.lh .divs svg{{width:1.9mm;height:auto}}
.lh .corner{{position:absolute;right:-14mm;bottom:-30mm;width:62mm;opacity:{.05 if variant=="bianco" else .06}}}
'''
    divs=''.join(f'<span>{flame(c,"")}{lab}</span>' for _,c,lab in DIV)
    p1=f'''<section class="page lh">
 {logo('3blaze_logo_horizontal',BLACK,'')}
 <div class="meta mono"><b>{CO["ragione"]}</b><br>Media · Academy · News · IA<br>{CO["web"]}</div>
 <div class="fold" style="top:99mm"></div><div class="fold" style="top:148.5mm;width:6mm"></div><div class="fold" style="top:198mm"></div>
 <div class="body">
  <div class="to">Spett.le<br>Nome Azienda<br>Via Esempio 12<br>00100 Città (XX)</div>
  <div>Terni, 15 gennaio 2027</div>
  <div class="obj">Oggetto: proposta di collaborazione 2027</div>
  <p>Gentile Nome Cognome,</p>
  <p>questa è la carta intestata del gruppo 3blaze. Il testo corrente è composto in 3blaze Sans a 10 pt con interlinea 16 pt, allineato a sinistra e mai giustificato; la misura resta tra i 65 e i 75 caratteri per riga.</p>
  <p>L'oggetto è in corsivo, la data in tondo. I numeri e i riferimenti tecnici possono usare il carattere mono delle etichette. Il logo non si ripete nel corpo della lettera e non si colora: nero su carta bianca, nero su carta crema.</p>
  <p>Cordiali saluti,</p>
  <div class="sig">Nome Cognome<br><i style="color:{MUTED_L}">Ruolo — 3blaze media</i></div>
 </div>
 {flame(BLACK,'')}
 <div class="foot mono">
  <div><b>{CO["ragione"]}</b><br>{CO["sede"]}</div>
  <div style="text-transform:none">{CO["mail"]}<br>{CO["web"]}</div>
  <div>{CO["piva"]}<br>{CO["pec"]}</div>
  <div class="divs">{divs}</div>
 </div>
</section>'''.replace(f'{flame(BLACK,"")}\n <div class="foot',f'<div class="corner">{flame(BLACK,"")}</div>\n <div class="foot',1)
    p1=p1.replace(f'<svg class="lg-3blaze_logo_horizontal"','<svg class="logo lg-3blaze_logo_horizontal"',1)
    p2=f'''<section class="page lh">
 <div class="meta mono" style="left:20mm;right:auto;text-align:left"><b>{CO["ragione"]}</b> · {CO["web"]}</div>
 <div style="position:absolute;right:20mm;top:17mm;width:12mm">{logo('3blaze_symbol',BLACK)}</div>
 <div class="fold" style="top:99mm"></div><div class="fold" style="top:148.5mm;width:6mm"></div><div class="fold" style="top:198mm"></div>
 <div class="foot mono" style="grid-template-columns:1fr 1fr"><div>{CO["sede"]}</div><div style="text-align:right">pagina 2</div></div>
</section>'''
    return doc(f'carta_intestata_A4_{variant}', css, p1+p2, 210, 297, 1240)

# ---------------- BIGLIETTO DA VISITA 85x55 (+3mm abbondanza) ----------------
def business_cards():
    css=f'''
.bc{{color:{CREAM}}}
.bc .safe{{position:absolute;left:7mm;top:7mm;right:7mm;bottom:7mm}}
.bc .sym{{position:absolute;left:0;top:0;width:15mm}}
.bc .who{{position:absolute;left:0;bottom:7.2mm;font-size:10pt;line-height:1.2}}
.bc .who i{{display:block;font-size:7pt;opacity:.72;margin-top:.8mm}}
.bc .contacts{{position:absolute;left:0;bottom:0;font-size:5.4pt;line-height:1.65;opacity:.9}}
.bc .div{{position:absolute;right:0;top:.4mm;font-size:5.4pt;opacity:.8}}
.bc .back{{position:absolute;inset:0;background:url({B}/out/scene/card_back.png) center/cover}}
.bc .backurl{{position:absolute;right:7mm;bottom:6.6mm;font-size:5.6pt;color:{CREAM}}}
.bc .backlogo{{position:absolute;left:7mm;bottom:6.4mm;width:20mm}}
.crop{{position:absolute;border-color:#000;border-style:solid;border-width:0}}
'''
    pages=''
    for key,bg,lab in [('media',BLACK,'media'),('academy',OR,'academy'),('news',TEAL,'.net'),('ia',WINE,'luisa')]:
        ink = BLACK if key=='academy' else CREAM
        pages+=f'''<section class="page bc" style="background:{bg};color:{ink}">
 <div class="safe">
  {logo('3blaze_symbol' if key!='ia' else 'luisa', ink, 'width:15mm' if key!='ia' else 'width:14mm')}
  <div class="div mono">{'3blaze ' + lab if key!='ia' else 'IA by 3blaze'}</div>
  <div class="who">Nome Cognome<i>Ruolo, Area</i></div>
  <div class="contacts mono">+39 000 000 0000<br><span style="text-transform:none">nome@3blaze.it · 3blaze.it</span></div>
 </div></section>'''
    pages+=f'''<section class="page bc"><div class="back"></div>
 <div class="backlogo">{logo('3blaze_wordmark',CREAM)}</div><div class="backurl mono" style="text-transform:none">3blaze.it</div></section>'''
    return doc('biglietti_da_visita_85x55_abbondanza3mm', css, pages, 91, 61, 1092)

# ---------------- BUSTA DL ----------------
def envelope():
    css=f'''.env{{background:#fff;color:{BLACK}}}
.env .lgo{{position:absolute;left:12mm;top:11mm;width:42mm}}
.env .ret{{position:absolute;left:12mm;top:27mm;font-size:6pt;line-height:1.6;color:{MUTED_L}}}
.env .strip{{position:absolute;left:12mm;bottom:10mm;display:flex;gap:2.4mm}}
.env .strip svg{{width:2.4mm}}
.env .win{{position:absolute;left:110mm;top:50mm;width:90mm;height:45mm;border:.3pt dashed #0000002E;border-radius:2mm}}
.env .win span{{position:absolute;left:3mm;top:2mm;font-size:5pt;color:#00000055}}'''
    strip=''.join(flame(c) for _,c,_ in DIV)
    body=f'''<section class="page env"><div class="lgo">{logo('3blaze_logo_horizontal',BLACK)}</div>
<div class="ret mono">{CO["ragione"]}<br>{CO["sede"]}</div><div class="strip">{strip}</div>
<div class="win"><span class="mono">area indirizzo / finestra</span></div></section>'''
    return doc('busta_DL_220x110', css, body, 220, 110, 1320)

# ---------------- ROLL-UP 85x200 cm (scala 1:4) ----------------
def rollup():
    css=f'''.ru{{background:{BLACK};color:{CREAM}}}
.ru .top{{position:absolute;left:16mm;top:20mm;width:150mm}}
.ru .img{{position:absolute;left:0;right:0;top:110mm;height:250mm;background:url({B}/out/scene/prisma_flame.png) center/cover}}
.ru .img::before,.ru .img::after{{content:'';position:absolute;left:0;right:0;height:40mm}}
.ru .img::before{{top:0;background:linear-gradient({BLACK},transparent)}} .ru .img::after{{bottom:0;background:linear-gradient(transparent,{BLACK})}}
.ru .divs{{position:absolute;left:16mm;right:16mm;bottom:40mm;display:grid;grid-template-columns:1fr 1fr;gap:9mm 12mm;align-items:end}}
.ru .divs svg{{height:11mm;width:auto}}
.ru .url{{position:absolute;left:16mm;bottom:16mm;font-size:7mm;color:{MUTED_D}}}
.ru .ground{{position:absolute;left:0;right:0;bottom:0;height:8mm;background:{OR}}}'''
    body=f'''<section class="page ru"><div class="top">{logo('3blaze_logo_claim',CREAM)}</div>
<div class="img"></div>
<div class="divs">{logo('3blaze_symbol',CREAM,'height:11mm')}{logo('3blaze_academy',OR,'height:11mm')}{logo('3blaze_net','#3FA9BA','height:11mm')}{logo('luisa','#D98C99','height:11mm')}</div>
<div class="url mono" style="text-transform:none">3blaze.it — media · academy · news · ia</div><div class="ground"></div></section>'''
    return doc('rollup_85x200cm_scala1-4', css, body, 212.5, 500, 850)

# ---------------- AFFISSIONE 6x3 m (scala 1:10) ----------------
def billboard():
    css=f'''.bb{{background:{BLACK};color:{CREAM}}}
.bb .img{{position:absolute;inset:0;background:url({B}/out/scene/prisma_flame.png) center 46%/cover}}
.bb .img::after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,#000 0%,transparent 16%,transparent 66%,#000 94%)}}
.bb .sub{{position:absolute;left:26mm;top:24mm;width:300mm;font-size:8mm;line-height:1.3;color:{MUTED_D}}}
.bb .lgo{{position:absolute;left:26mm;bottom:20mm;width:150mm}}
.bb .url{{position:absolute;right:24mm;bottom:22mm;font-size:8mm}}'''
    body=f'''<section class="page bb"><div class="img"></div>
<div class="sub mono">media · academy · news · ia</div>
<div class="lgo">{logo('3blaze_logo_claim',CREAM)}</div><div class="url mono" style="text-transform:none">3blaze.it</div></section>'''
    return doc('affissione_6x3m_scala1-10', css, body, 600, 300, 1800)

# ---------------- INSEGNE ----------------
def signage():
    css=f'''.tg{{background:{BLACK};color:{CREAM}}}
.tg .st{{position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);width:170mm}}
.tg .ln{{position:absolute;left:0;right:0;bottom:22mm;text-align:center;font-size:5.4mm;color:{MUTED_D}}}
.tg .screw{{position:absolute;width:6mm;height:6mm;border-radius:50%;background:radial-gradient(circle at 35% 35%,#d9d4c7,#6b665c)}}
.lb{{background:{BLACK}}}
.lb .lgo{{position:absolute;left:30mm;top:50%;transform:translateY(-50%);width:110mm}}
.lb .divs{{position:absolute;right:30mm;top:50%;transform:translateY(-50%);display:flex;gap:12mm;align-items:flex-end}}
.lb .divs svg{{height:6.5mm;width:auto}}'''
    s='<div class="screw" style="left:10mm;top:10mm"></div><div class="screw" style="right:10mm;top:10mm"></div><div class="screw" style="left:10mm;bottom:10mm"></div><div class="screw" style="right:10mm;bottom:10mm"></div>'
    t=f'''<section class="page tg">{s}<div class="st">{logo('3blaze_logo_stacked',CREAM)}</div><div class="ln mono">media · academy · news · ia — {CO["sede"]}</div></section>'''
    doc('targa_ingresso_400x200mm', css, t, 400, 200, 1600)
    l=f'''<section class="page lb"><div class="lgo">{logo('3blaze_logo_horizontal',CREAM)}</div>
<div class="divs">{logo('3blaze_academy',OR)}{logo('3blaze_net','#3FA9BA')}{logo('luisa','#D98C99')}</div></section>'''
    return doc('insegna_cassonetto_300x60cm_scala1-10', css, l, 300, 60, 1800)

# ---------------- SOCIAL ----------------
def social():
    css=f'''.av{{background:{BLACK}}} .av .s{{position:absolute;left:50%;top:50%;transform:translate(-50%,-52%);width:60%}}
.li{{background:url({B}/out/scene/linkedin.png) center/cover}}
.ig{{background:{BLACK};color:{CREAM}}}
.ig .img{{position:absolute;inset:0;background:url({B}/out/scene/prisma_flame.png) center 45%/cover}}
.ig .img::after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,transparent 62%,#000 90%)}}
.ig .lab{{position:absolute;right:8%;bottom:7%;font-size:2.6mm;color:#A8A294}}
.ig .lgo{{position:absolute;left:8%;bottom:6.5%;width:40%}}'''
    doc('social_avatar_1080', css, f'<section class="page av"><div class="s">{logo("3blaze_symbol",CREAM)}</div></section>', 100, 100, 1080)
    doc('social_linkedin_cover_1584x396', css, '<section class="page li"></section>', 158.4, 39.6, 1584)
    return doc('social_post_1080x1350', css, f'''<section class="page ig"><div class="img"></div><div class="lab mono">2027</div>
<div class="lgo">{logo('3blaze_logo_claim',CREAM)}</div></section>''', 108, 135, 1080)

if __name__=='__main__':
    import sys
    w=sys.argv[1] if len(sys.argv)>1 else 'all'
    if w in('lh','all'): letterhead('bianco'); letterhead('crema')
    if w in('bc','all'): business_cards()
    if w in('env','all'): envelope()
    if w in('ru','all'): rollup()
    if w in('bb','all'): billboard()
    if w in('sign','all'): signage()
    if w in('soc','all'): social()
