"""Lockup logo + claim 'Ignite Beyond.' (firma, mai titolo)."""
import json
import pathops
from fontTools.ttLib import TTFont
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
A=json.load(open('logo_assets.json'))
F=TTFont('out/fonts/3blazeSans-Italic.ttf'); gs=F.getGlyphSet(); cm=F.getBestCmap(); hm=F['hmtx']
def text_path(txt, size, x0, base, track=0):
    s=size/1000; p=pathops.Path(); x=x0
    for ch in txt:
        g=cm[ord(ch)]; gs[g].draw(TransformPen(p.getPen(),(s,0,0,-s,x,base))); x+=hm[g][0]*s+track
    pen=SVGPathPen(None, ntos=lambda v:f"{round(v,1):g}"); p.draw(pen); return pen.getCommands(), p.bounds
CLAIM='Ignite Beyond.'
SIZE=280                 # cap-height claim = 28% dell'altezza fiamma (196 su 700)
GAP=200                  # 10u tra base del logo e maiuscole del claim
cap=700*SIZE/1000; base=700+GAP+cap
cd,cb=text_path(CLAIM, SIZE, 2040-12, base, track=6)
L=A['3blaze_logo_horizontal']; vx,vy,vw,vh=L['viewBox']
x0=min(vx,cb[0]); y1=max(vy+vh,cb[3])
vb=(x0,vy,max(vx+vw,cb[2])-x0,y1-vy)
def svg(fill,d,vb,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb[0]:g} {vb[1]:g} {vb[2]:g} {vb[3]:g}" role="img" aria-label="{title}"><title>{title}</title><path fill="{fill}" d="{d}"/></svg>\n'
out={}
for nm,fill in [('','currentColor'),('_black','#000000'),('_cream','#FDF6E2')]:
    open(f'out/logo/3blaze_logo_claim{nm}.svg','w').write(svg(fill, L['d']+' '+cd, vb, '3blaze — Ignite Beyond.'))
# claim da solo (per firme a piè di pagina)
cd2,cb2=text_path(CLAIM, 1000, 0, 700, track=20)
vb2=(cb2[0],cb2[1],cb2[2]-cb2[0],cb2[3]-cb2[1])
for nm,fill in [('','currentColor'),('_black','#000000'),('_cream','#FDF6E2')]:
    open(f'out/logo/3blaze_claim{nm}.svg','w').write(svg(fill, cd2, vb2, 'Ignite Beyond.'))
A['3blaze_logo_claim']={'viewBox':list(vb),'d':L['d']+' '+cd,'title':'3blaze — Ignite Beyond.'}
A['3blaze_claim']={'viewBox':list(vb2),'d':cd2,'title':'Ignite Beyond.'}
json.dump(A,open('logo_assets.json','w'))
print(vb, vb2)
