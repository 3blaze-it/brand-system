import json, math, os
from build_logo import flame_d, symbol_d, FW, FH, GAP, U, SYM_W, S3
A = json.load(open('/home/claude/brand/logo_assets.json'))
INK='#0A0A0A'; CREAM='#FDF6E2'; OR='#FB4F31'; GRID='rgba(10,10,10,.10)'; GRID2='rgba(10,10,10,.22)'
def t(x,y,s,size=34,anchor='start',fill=INK,font="'3blaze Sans'",style='normal',w=500,ls=0):
    return f'<text x="{x:g}" y="{y:g}" font-family="{font.replace(chr(39),'&apos;')}" font-size="{size}" font-style="{style}" font-weight="{w}" letter-spacing="{ls}" text-anchor="{anchor}" fill="{fill}">{s}</text>'
def line(x1,y1,x2,y2,c=OR,w=3,dash=None):
    return f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" stroke="{c}" stroke-width="{w}"' + (f' stroke-dasharray="{dash}"' if dash else '') + '/>'
out=[]
W,H=4200,2970
out.append(f'<rect width="{W}" height="{H}" fill="{CREAM}"/>')
# header
out.append(t(160,200,'3BLAZE — TAVOLA COSTRUTTIVA DEL MARCHIO',40,ls=6))
out.append(t(160,262,'Ricostruzione 2027 · griglia modulare 1u = 20 unità-font (UPM 1000) · fiamma 24u × 35u · altezza fiamma = cap-height 3blaze Sans',30,fill='rgba(10,10,10,.6)'))
out.append(t(W-160,200,'v1.0 · 2027',30,anchor='end',fill='rgba(10,10,10,.6)'))
out.append(line(160,300,W-160,300,INK,2))

# ---- Pannello 1: fiamma su griglia ----
s=2.6; ox,oy=260,520   # scala 2.6 → fiamma 1248 x 1820 troppo grande; usiamo s=1.9
s=1.6; ox=620
g=[]
for i in range(25):
    x=ox+i*U*s; g.append(line(x,oy,x,oy+FH*s,GRID2 if i%6==0 else GRID,1.5))
for j in range(36):
    y=oy+j*U*s; g.append(line(ox,y,ox+FW*s,y,GRID2 if j%5==0 else GRID,1.5))
out+=g
out.append(f'<g transform="translate({ox},{oy}) scale({s})"><path d="{flame_d()}" fill="{INK}"/></g>')
d=6*S3*U; tt=(6*S3-6)*U; r=12*U
P=lambda x,y:(ox+x*s,oy+y*s)
# assi di simmetria
x0,y0=P(FW/2,-40); x1,y1=P(FW/2,FH+40); out.append(line(x0,y0,x1,y1,OR,2.5,'14 10'))
# punti chiave
for (x,y) in [(0,tt),(FW/4,d),(FW/2,0),(3*FW/4,d),(FW,tt),(FW,FH-r),(0,FH-r)]:
    cx,cy=P(x,y); out.append(f'<circle cx="{cx:g}" cy="{cy:g}" r="9" fill="{CREAM}" stroke="{OR}" stroke-width="4"/>')
# cerchio base
cx,cy=P(FW/2,FH-r); out.append(f'<circle cx="{cx:g}" cy="{cy:g}" r="{r*s:g}" fill="none" stroke="{OR}" stroke-width="2.5" stroke-dasharray="10 8"/>')
out.append(f'<circle cx="{cx:g}" cy="{cy:g}" r="7" fill="{OR}"/>')
out.append(line(cx,cy,cx+r*s*math.cos(math.radians(35)),cy+r*s*math.sin(math.radians(35)),OR,2.5))
out.append(t(cx+40,cy+70,'r = 12u',30,fill=CREAM))
# angoli
a1x,a1y=P(FW/4,d); out.append(t(a1x-150,a1y+20,'45°',34,fill=OR,w=500))
a2x,a2y=P(FW/2,0); out.append(t(a2x+30,a2y+90,'60°',34,fill=OR))
# quote
R=ox+FW*s+70
out.append(line(R,oy,R,oy+FH*s,INK,2)); out.append(t(R+20,oy+FH*s/2,'35u',32))
out.append(line(ox,oy+FH*s+70,ox+FW*s,oy+FH*s+70,INK,2)); out.append(t(ox+FW*s/2,oy+FH*s+120,'24u',32,anchor='middle'))
for yy,lab in [(tt,'punte  6(√3−1)u ≈ 4,39u'),(d,'incavi  6√3u ≈ 10,39u'),(FH-r,'centro arco  23u')]:
    _,py=P(0,yy); out.append(line(ox-30,py,ox-150,py,OR,2,'6 6')); out.append(t(ox-160,py+10,lab,24,anchor='end',fill='rgba(10,10,10,.7)'))
out.append(t(ox,oy-60,'01 — LA FIAMMA',30,ls=4))
cap=['Base a semicerchio (r = metà larghezza), fianchi verticali,',
     'sommità a corona: incavi a 1/4 e 3/4 della larghezza.',
     'Punta→incavo a 45°, incavo→picco a 60°.',
     'Simmetria assiale perfetta (scarto originale corretto: 1,1%).']
for i,c in enumerate(cap): out.append(t(ox,oy+FH*s+200+i*44,c,28,fill='rgba(10,10,10,.75)'))

# ---- Pannello 2: simbolo ----
s2=0.6; ox2,oy2=1900,520
out.append(t(ox2,oy2-60,'02 — IL SIMBOLO',30,ls=4))
out.append(f'<g transform="translate({ox2},{oy2}) scale({s2})"><path d="{symbol_d()}" fill="{INK}"/></g>')
for i in range(2):
    xa=ox2+(FW*(i+1)+GAP*i)*s2; xb=xa+GAP*s2
    out.append(f'<rect x="{xa:g}" y="{oy2:g}" width="{GAP*s2:g}" height="{FH*s2:g}" fill="{OR}" fill-opacity=".18"/>')
    out.append(t((xa+xb)/2,oy2+FH*s2+60,'10u',28,anchor='middle',fill=OR))
yb=oy2+FH*s2+110; out.append(line(ox2,yb,ox2+SYM_W*s2,yb,INK,2)); out.append(t(ox2+SYM_W*s2/2,yb+50,'92u = 3 × 24u + 2 × 10u',28,anchor='middle'))
for i,c in enumerate(['Tre fiamme identiche, passo 34u.','Il simbolo è sempre in tre: mai una fiamma ruotata,','scalata o colorata diversamente dalle altre.']):
    out.append(t(ox2,yb+130+i*44,c,28,fill='rgba(10,10,10,.75)'))

# ---- Pannello 3: lockup ----
L=A['3blaze_logo_horizontal']; vx,vy,vw,vh=L['viewBox']
s3=0.4; ox3,oy3=ox2,1480
out.append(t(ox3,oy3-60,'03 — LOCKUP ORIZZONTALE (PRIMARIO)',30,ls=4))
base=oy3+FH*s3; capt=oy3; asc=oy3-60*s3
for yy,lab in [(asc,'ascendenti +3u (760)'),(capt,'cap-height (700)'),(oy3+(FH-500)*s3,'x-height (500)'),(base,'baseline')]:
    out.append(line(ox3-40,yy,ox3+vw*s3+40,yy,OR,2,'8 8')); out.append(t(ox3+vw*s3+60,yy+9,lab,24,fill='rgba(10,10,10,.7)'))
out.append(f'<g transform="translate({ox3},{oy3}) scale({s3})"><path d="{L["d"]}" fill="{INK}"/></g>')
xa=ox3+SYM_W*s3; out.append(f'<rect x="{xa:g}" y="{oy3:g}" width="{GAP*s3:g}" height="{FH*s3:g}" fill="{OR}" fill-opacity=".22"/>')
out.append(t(xa+GAP*s3/2,base+50,'10u',26,anchor='middle',fill=OR))
for i,c in enumerate(['Logotipo: 3blaze Sans Italic (−9°), crenatura ottica su griglia 1u:',
                      '3·b −10u · b·l −8u · l·a −8u · a·z −6u · z·e −5u.',
                      'Dove le lettere si sovrappongono, quella successiva taglia la precedente',
                      'con un canale di knockout di 2u: è la firma "a fiamme accostate".']):
    out.append(t(ox3,base+130+i*44,c,28,fill='rgba(10,10,10,.75)'))

# ---- Pannello 4: area di rispetto e dimensioni minime ----
ox4,oy4=ox2,2260; s4=0.22
out.append(t(ox4,oy4-40,'04 — AREA DI RISPETTO E DIMENSIONI MINIME',30,ls=4))
X=FW*s4
out.append(f'<rect x="{ox4:g}" y="{oy4:g}" width="{vw*s4+2*X:g}" height="{vh*s4+2*X:g}" fill="none" stroke="{OR}" stroke-width="2" stroke-dasharray="8 8"/>')
out.append(f'<g transform="translate({ox4+X},{oy4+X-vy*s4}) scale({s4})"><path d="{L["d"]}" fill="{INK}"/></g>')
out.append(f'<g transform="translate({ox4+X-FW*s4},{oy4}) scale({s4})"><path d="{flame_d()}" fill="{OR}" fill-opacity=".35"/></g>')
mx=ox4+vw*s4+2*X+80
for i,c in enumerate(['Area di rispetto = 1 fiamma (24u) su ogni lato.',
                      'Minimi: logo orizzontale 30 mm / 140 px;',
                      'simbolo 8 mm / 32 px; fiamma singola 4 mm / 16 px.']):
    out.append(t(mx,oy4+60+i*44,c,28,fill='rgba(10,10,10,.75)'))

svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'+''.join(out)+'</svg>'
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'3blaze Sans';src:url(fonts/3blazeSans-Regular.woff2)}}
@font-face{{font-family:'3blaze Sans';font-style:italic;src:url(fonts/3blazeSans-Italic.woff2)}}
@page{{size:420mm 297mm;margin:0}} html,body{{margin:0}} svg{{display:block;width:420mm;height:297mm}}
</style></head><body>{svg}</body></html>'''
open('/home/claude/brand/out/construction.html','w').write(html)
