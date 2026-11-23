"""Diagrammi geometrici del marchio per il manuale."""
import math
from lib import A, FLAME, OR, BLACK, CREAM, MUTED_L
S3=math.sqrt(3); U=20
def _t(x,y,s,size=7,anchor='start',col=OR):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-family="JetBrains Mono" font-size="{size}" letter-spacing=".8" fill="{col}" text-anchor="{anchor}">{s}</text>'

def flame_construction(w,h):
    s=1.0; fw,fh=480*s*0.78,700*s*0.78; k=fw/480
    ox=(w-fw)/2+40; oy=(h-fh)/2+10
    g=[f'<rect width="{w}" height="{h}" fill="#F2E8CC"/>']
    for i in range(25):
        x=ox+i*U*k; g.append(f'<line x1="{x:.1f}" y1="{oy}" x2="{x:.1f}" y2="{oy+fh:.1f}" stroke="#000" stroke-opacity="{.16 if i%6==0 else .06}" stroke-width=".7"/>')
    for j in range(36):
        y=oy+j*U*k; g.append(f'<line x1="{ox}" y1="{y:.1f}" x2="{ox+fw:.1f}" y2="{y:.1f}" stroke="#000" stroke-opacity="{.16 if j%5==0 else .06}" stroke-width=".7"/>')
    g.append(f'<g transform="translate({ox} {oy}) scale({k})"><path d="{FLAME}" fill="#000"/></g>')
    P=lambda x,y:(ox+x*k,oy+y*k)
    t=(6*S3-6)*U; d=6*S3*U; r=12*U
    cx,cy=P(240,460)
    g.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r*k:.1f}" fill="none" stroke="{OR}" stroke-width="1" stroke-dasharray="5 4"/>')
    ax,ay=P(240,-30); bx,by=P(240,730)
    g.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{OR}" stroke-width=".9" stroke-dasharray="6 4"/>')
    for x,y in [(0,t),(120,d),(240,0),(360,d),(480,t),(480,460),(0,460)]:
        px,py=P(x,y); g.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.2" fill="#F2E8CC" stroke="{OR}" stroke-width="1.4"/>')
    g.append(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{cx+r*k*.8:.1f}" y2="{cy+r*k*.6:.1f}" stroke="{OR}" stroke-width="1"/>')
    g.append(_t(cx+12,cy+30,'R = 12U',7,col=CREAM))
    for yy,lab in [(t,'PUNTE 6(√3−1)U ≈ 4,39U'),(d,'INCAVI 6√3U ≈ 10,39U'),(460,'CENTRO ARCO 23U')]:
        _,py=P(0,yy); g.append(f'<line x1="{ox-8}" y1="{py:.1f}" x2="{ox-70}" y2="{py:.1f}" stroke="{OR}" stroke-width=".8" stroke-dasharray="3 3"/>'); g.append(_t(ox-74,py+2.5,lab,6.2,'end'))
    px,py=P(70,d-30); g.append(_t(px,py,'45°',9))
    px,py=P(255,70); g.append(_t(px,py,'60°',9))
    g.append(f'<line x1="{ox}" y1="{oy+fh+22:.1f}" x2="{ox+fw:.1f}" y2="{oy+fh+22:.1f}" stroke="#000" stroke-width=".8"/>'); g.append(_t(ox+fw/2,oy+fh+36,'24U = 480',7,'middle',BLACK))
    g.append(f'<line x1="{ox+fw+22:.1f}" y1="{oy}" x2="{ox+fw+22:.1f}" y2="{oy+fh:.1f}" stroke="#000" stroke-width=".8"/>'); g.append(_t(ox+fw+30,oy+fh/2,'35U = 700',7,'start',BLACK))
    return f'<svg width="{w}" height="{h}" style="display:block;border-radius:0 0 22px 22px">{"".join(g)}</svg>'

def lockup_lines(w,h):
    L=A['3blaze_logo_horizontal']
    x0,x1=900,3500; k=(w-60)/(x1-x0); base=h/2+90; oy=base-700*k; ox=30-x0*k
    g=[f'<defs><clipPath id="cl"><rect x="0" y="0" width="{w}" height="{h}" rx="0"/></clipPath></defs><rect width="{w}" height="{h}" fill="#F2E8CC"/>']
    g.append(f'<rect x="{ox+1840*k:.1f}" y="{oy:.1f}" width="{200*k:.1f}" height="{700*k:.1f}" fill="{OR}" fill-opacity=".22"/>')
    g.append(f'<rect x="{ox+1160*k:.1f}" y="{oy:.1f}" width="{200*k:.1f}" height="{700*k:.1f}" fill="{OR}" fill-opacity=".22"/>')
    g.append(f'<g clip-path="url(#cl)"><g transform="translate({ox:.1f} {oy:.1f}) scale({k})"><path d="{L["d"]}" fill="#000"/></g></g>')
    for yy,lab in [(-60,'ASCENDENTI +3U · 760'),(0,'CAP-HEIGHT = ALTEZZA FIAMMA · 700'),(200,'X-HEIGHT · 500'),(700,'LINEA DI BASE = FONDO ARCO · 0')]:
        y=oy+yy*k; g.append(f'<line x1="14" y1="{y:.1f}" x2="{w-14}" y2="{y:.1f}" stroke="{OR}" stroke-width=".8" stroke-dasharray="5 4"/>')
        g.append(_t(w-16,y-(5 if yy!=0 else -11),lab,6.2,'end'))
    g.append(_t(ox+1260*k,oy+700*k+18,'10U',6.4,'middle')); g.append(_t(ox+1940*k,oy+700*k+18,'10U',6.4,'middle'))
    return f'<svg width="{w}" height="{h}" style="display:block;border-radius:0 0 22px 22px">{"".join(g)}</svg>'

def clearspace(w,h):
    L=A['3blaze_logo_horizontal']; vx,vy,vw,vh=L['viewBox']
    k=(w-200)/(vw+960); X=480*k
    lw=vw*k; lh=vh*k; ox=(w-lw)/2; oy=(h-lh)/2
    g=[f'<rect width="{w}" height="{h}" fill="#F2E8CC"/>']
    g.append(f'<rect x="{ox-X:.1f}" y="{oy-X:.1f}" width="{lw+2*X:.1f}" height="{lh+2*X:.1f}" fill="{OR}" fill-opacity=".10" stroke="{OR}" stroke-dasharray="5 4" stroke-width=".9"/>')
    g.append(f'<g transform="translate({ox} {oy-vy*k}) scale({k})"><path d="{L["d"]}" fill="#000"/></g>')
    for (x,y) in [(ox-X,oy+lh/2-350*k),(ox+lw,oy+lh/2-350*k)]:
        g.append(f'<g transform="translate({x:.1f} {y:.1f}) scale({k})"><path d="{FLAME}" fill="{OR}" fill-opacity=".45"/></g>')
    g.append(_t(ox-X+6,oy-X-8,'AREA DI RISPETTO = 1 FIAMMA (24U)',6.4))
    return f'<svg width="{w}" height="{h}" style="display:block;border-radius:0 0 22px 22px">{"".join(g)}</svg>'
