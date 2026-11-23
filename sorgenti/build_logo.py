"""3blaze 2027 — ricostruzione geometrica del marchio.
Unità: 1u = 20 unità-font (UPM 1000). Fiamma = 24u x 35u. Altezza fiamma = cap-height 3blaze Sans (700).
"""
import math, json, os
import pathops
from fontTools.ttLib import TTFont
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.svgPathPen import SVGPathPen

U = 20.0
S3 = math.sqrt(3)
FW, FH = 24*U, 35*U            # 480 x 700
GAP = 10*U                     # 200: spazio tra fiamme e tra simbolo e wordmark
KO = 2*U                       # 40: canale di knockout tra lettere sovrapposte
FONT = '/mnt/user-data/uploads/3blaze-nextgen/3blaze_Sans_v0.2/3blazeSans-Italic.ttf'
OUT = '/home/claude/brand/out/logo'
os.makedirs(OUT, exist_ok=True)

# ---------- fiamma ----------
def flame_points():
    d = 6*S3*U          # profondita' incavo (60deg verso il picco)
    t = (6*S3-6)*U      # quota punte laterali (45deg verso l'incavo)
    return d, t

def flame_d(x0=0.0, y0=0.0, w=FW, h=FH, prec=2):
    s = w/FW
    d, t = flame_points(); d*=s; t*=s
    r = w/2; cy = h - r
    f = lambda v: f"{round(v,prec):g}"
    P = [(x0, y0+t), (x0+w/4, y0+d), (x0+w/2, y0), (x0+3*w/4, y0+d), (x0+w, y0+t), (x0+w, y0+cy)]
    s_ = "M" + " L".join(f"{f(x)} {f(y)}" for x, y in P)
    s_ += f" A{f(r)} {f(r)} 0 0 1 {f(x0)} {f(y0+cy)} Z"
    return s_

def flame_path(x0=0.0, y0=0.0, w=FW):
    s = w/FW; d, t = flame_points(); d*=s; t*=s; h = FH*s
    r = w/2; cy = h - r
    p = pathops.Path(); pen = p.getPen()
    pen.moveTo((x0, y0+t)); pen.lineTo((x0+w/4, y0+d)); pen.lineTo((x0+w/2, y0))
    pen.lineTo((x0+3*w/4, y0+d)); pen.lineTo((x0+w, y0+t)); pen.lineTo((x0+w, y0+cy))
    k = 0.5522847498*r
    cx = x0 + r
    pen.curveTo((x0+w, y0+cy+k), (cx+k, y0+cy+r), (cx, y0+cy+r))
    pen.curveTo((cx-k, y0+cy+r), (x0, y0+cy+k), (x0, y0+cy))
    pen.closePath()
    return p

def symbol_d(x0=0, y0=0):
    return " ".join(flame_d(x0 + i*(FW+GAP), y0) for i in range(3))
SYM_W = 3*FW + 2*GAP   # 1840 = 92u

# ---------- wordmark ----------
font = TTFont(FONT); gs = font.getGlyphSet(); cmap = font.getBestCmap(); hmtx = font['hmtx']

def glyph_path(ch, penx, base):
    g = cmap[ord(ch)]
    p = pathops.Path()
    tp = TransformPen(p.getPen(), (1, 0, 0, -1, penx, base))
    gs[g].draw(tp)
    return p

def union(paths):
    out = pathops.Path()
    for p in paths:
        out = pathops.op(out, p, pathops.PathOp.UNION)
    return out

def knockout_word(text, start_ink_x, base, kern):
    pens = []; x = start_ink_x - glyph_bounds(text[0])[0]
    for i, ch in enumerate(text):
        pens.append(x)
        if i < len(text)-1:
            x += hmtx[cmap[ord(ch)]][0] + kern[i]
    glyphs = [glyph_path(ch, px, base) for ch, px in zip(text, pens)]
    res = []
    for i, g in enumerate(glyphs):
        later = glyphs[i+1:]
        if later:
            cover = union(later)
            st = pathops.Path(cover)
            st.stroke(2*KO, pathops.LineCap.BUTT_CAP, pathops.LineJoin.MITER_JOIN, 4)
            cutter = pathops.op(cover, st, pathops.PathOp.UNION)
            g = pathops.op(g, cutter, pathops.PathOp.DIFFERENCE)
        res.append(g)
    return res

def glyph_bounds(ch):
    from fontTools.pens.boundsPen import BoundsPen
    bp = BoundsPen(gs); gs[cmap[ord(ch)]].draw(bp); return bp.bounds

def path_d(p, prec=1):
    pen = SVGPathPen(None, ntos=lambda v: f"{round(v,prec):g}")
    p.draw(pen); return pen.getCommands()

def bounds(paths):
    xs=[];ys=[]
    for p in paths:
        b=p.bounds; xs+= [b[0],b[2]]; ys+=[b[1],b[3]]
    return min(xs),min(ys),max(xs),max(ys)

KERN_3BLAZE = [-200, -160, -160, -120, -100]   # su griglia 20 (1u)
BASE = FH  # baseline = fondo fiamma

def wordmark(text, start_x, kern=None):
    kern = kern or [-60]*(len(text)-1)
    return knockout_word(text, start_x, BASE, kern)

def svg(view, body, title, w=None):
    x,y,W,H = view
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:g} {y:g} {W:g} {H:g}"'
            + (f' width="{w}"' if w else '') + f' role="img" aria-label="{title}">\n'
            f'<title>{title}</title>\n{body}\n</svg>\n')

def write(name, view, d, title, fill='currentColor'):
    body = f'<path fill="{fill}" fill-rule="nonzero" d="{d}"/>'
    open(f'{OUT}/{name}.svg','w').write(svg(view, body, title))

if __name__ == '__main__':
    PAD = 0
    # simbolo
    sd = symbol_d()
    # wordmark principale
    WX = SYM_W + GAP
    wm = wordmark('3blaze', WX, KERN_3BLAZE)
    wd = " ".join(path_d(p) for p in wm)
    bx0,by0,bx1,by1 = bounds(wm)
    print('wordmark bounds', bx0,by0,bx1,by1)
    H_top = min(0, by0); H_bot = max(FH, by1)
    meta = {"unit_u": U, "flame": [FW, FH], "gap": GAP, "knockout": KO, "symbol_w": SYM_W,
            "wordmark_bounds": [bx0,by0,bx1,by1], "kern_3blaze": KERN_3BLAZE}
    json.dump(meta, open(f'{OUT}/_geometry.json','w'), indent=1)
    # salva parti per riuso
    json.dump({"symbol": sd, "wordmark": wd, "flame": flame_d(), "wm_x0": WX,
               "wm_bounds":[bx0,by0,bx1,by1]}, open('/home/claude/brand/parts.json','w'))
