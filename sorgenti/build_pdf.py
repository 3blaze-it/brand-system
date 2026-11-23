import markdown, sys, re
sys.path.insert(0,'/home/claude/brand'); from render import render
F='/home/claude/brand/out/fonts/'
md=open('3blaze_Brand_System_2027_completo.md').read()
body=markdown.markdown(md.split('\n## Indice')[1].split('\n',1)[1] if False else md, extensions=['fenced_code','tables'])
# togli il titolo h1 dal flusso (va in copertina)
body=body.split('</h1>',1)[1]
import glob,os
def loc(rel):
    b=os.path.basename(rel); c=glob.glob('/home/claude/brand/out/**/'+b,recursive=True)+glob.glob('/home/claude/brand/'+b)
    return 'file://'+sorted(c,key=os.path.getmtime)[-1] if c else ''
body=re.sub(r'src="\.\./([^"]+)"', lambda m: f'src="{loc(m.group(1))}"', body)
body=body.replace('<h2>Indice</h2>','<h2 class="first">Indice</h2>',1)
logo=open('/home/claude/brand/out/logo/3blaze_logo_horizontal.svg').read()
css=f'''@font-face{{font-family:'3blaze Sans';src:url({F}3blazeSans-Regular.ttf)}}
@font-face{{font-family:'3blaze Sans';font-style:italic;src:url({F}3blazeSans-Italic.ttf)}}
@font-face{{font-family:'3blaze Display';src:url({F}3blazeDisplay-Regular.ttf)}}
@font-face{{font-family:'JB';src:url({F}JetBrainsMono-Regular.woff2)}}
@page{{size:A4;margin:18mm 18mm 20mm 18mm;@bottom-left{{content:"3blaze · Brand System 2027";font:7pt JB;color:#6B665C}}@bottom-right{{content:counter(page);font:7pt JB;color:#6B665C}}}}
@page:first{{margin:0}}
html{{background:#FDF6E2}} body{{margin:0;font-family:'3blaze Sans','JB';font-size:9.6pt;line-height:1.5;color:#000;-webkit-print-color-adjust:exact}}
.cover{{height:297mm;width:210mm;background:#000 url(file:///home/claude/brand/out/trama/3blaze_trama_vetro_A4_verticale.jpg) center/cover;position:relative;color:#FDF6E2;break-after:page;margin:0}}
.cover .lg{{position:absolute;left:18mm;top:20mm;width:62mm;color:#FDF6E2}} .cover .lg svg{{width:100%;height:auto}}
.cover h1{{position:absolute;left:18mm;bottom:52mm;width:170mm;font-weight:400;font-size:30pt;line-height:1.05;margin:0}}
.cover p{{position:absolute;left:18mm;bottom:30mm;width:150mm;font-style:italic;font-size:10pt;color:#C9C2B0;margin:0}}
.cover .m{{position:absolute;left:18mm;bottom:18mm;font:7pt JB;letter-spacing:.12em;color:#A8A294}}
h2{{font-weight:400;font-size:22pt;line-height:1.1;margin:0 0 6mm;padding-top:2mm;break-before:page;border-top:2px solid #000}}
h3{{font-weight:400;font-size:13pt;margin:7mm 0 2mm;break-after:avoid}} h4{{font-size:10.5pt;font-weight:400;font-style:italic;margin:5mm 0 1mm}}
p,li{{orphans:3;widows:3}} b,strong{{font-weight:400;background:#FB4F3122;padding:0 2px}}
code{{font-family:JB;font-size:8pt;background:#EDE3C6;padding:0 3px;border-radius:0 0 3px 3px}}
pre{{background:#0E0E0E;color:#E8E1CF;padding:4mm;border-radius:0 0 4mm 4mm;white-space:pre-wrap;word-break:break-all;font-size:6.6pt;line-height:1.45}}
pre code{{background:none;color:inherit;font-size:inherit;padding:0}}
table{{border-collapse:collapse;width:100%;font-size:8.6pt;margin:3mm 0}} th{{text-align:left;font:7pt JB;letter-spacing:.08em;text-transform:uppercase;color:#6B665C;border-bottom:1px solid #000;padding:2mm 2mm 1.5mm 0}}
td{{border-bottom:.5pt solid #0002;padding:1.6mm 2mm 1.6mm 0;vertical-align:top}} tr{{break-inside:avoid}}
blockquote{{margin:3mm 0;padding:3mm 4mm;background:#F6EDD3;border-radius:0 0 4mm 4mm;font-style:italic}}
hr{{display:none}} h2.first{{break-before:avoid}} img{{max-width:100%;max-height:110mm;display:block;margin:3mm 0;border-radius:0 0 4mm 4mm}} a{{color:#C93A20}}'''
cover=f'''<section class="cover"><div class="lg">{logo}</div><h1>Brand System 2027<br>Documento completo</h1>
<p>Regole, token, codice, marchio e file del sistema d'identità 3blaze, in un solo documento leggibile da persone e da IA. Ignite Beyond.</p><div class="m">VERSIONE 1.0 · 17/11/2026 · 3BLAZE S.R.L.S.</div></section>'''
html=f'<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{css}</style></head><body>{cover}{body}</body></html>'
open('guide_ia.html','w').write(html)
render('guide_ia.html', pdf='3blaze_Brand_System_2027_completo.pdf', w=794, h=1123, wait=800)
