import json, math
from build_logo import *
C = {'black':'#000000','cream':'#FDF6E2','orange':'#FB4F31','teal':'#006172','wine':'#4D1821'}
KERNS = {'3blaze':[-200,-160,-160,-120,-100], 'academy':[-100,-100,-100,-140,-120,-140],
         '.net':[-40,-40,-40], 'luisa':[-160,-160,-120,-180]}
assets = {}
def emit(name, view, d, title, colors=('mono','black','cream')):
    for c in colors:
        fill = 'currentColor' if c=='mono' else C[c]
        fn = f'{name}' + ('' if c=='mono' else f'_{c}')
        write(fn, view, d, title, fill)
    assets[name] = {"viewBox": view, "d": d, "title": title}

def vb(b, pad=0):
    x0,y0,x1,y1 = b
    return (x0-pad, y0-pad, x1-x0+2*pad, y1-y0+2*pad)

sym = symbol_d()
emit('3blaze_symbol', vb((0,0,SYM_W,FH)), sym, '3blaze — simbolo (tre fiamme)')
emit('3blaze_flame', vb((0,0,FW,FH)), flame_d(), '3blaze — fiamma singola')

def word_parts(word, x0):
    ps = wordmark(word, x0, KERNS[word]); b = bounds(ps)
    return " ".join(path_d(p) for p in ps), b

# wordmark solo
wd, wb = word_parts('3blaze', 0)
emit('3blaze_wordmark', vb((wb[0], min(wb[1],0), wb[2], max(wb[3],FH))), wd, '3blaze — logotipo')

# lockup orizzontale (primario)
wd2, wb2 = word_parts('3blaze', SYM_W+GAP)
H0 = min(0, wb2[1]); H1 = max(FH, wb2[3])
emit('3blaze_logo_horizontal', vb((0,H0,wb2[2],H1)), sym+" "+wd2, '3blaze — logo orizzontale')

# lockup verticale
ww = wb[2]-wb[0]; total_w = max(ww, SYM_W)
sx = (total_w - SYM_W)/2
asc_top = wb[1]  # -60
wy = FH + GAP - asc_top   # traslazione verticale del wordmark
wx = (total_w - ww)/2 - wb[0]
ps = wordmark('3blaze', 0, KERNS['3blaze'])
ps = [p.transform(1,0,0,1,wx,wy) for p in ps]
wds = " ".join(path_d(p) for p in ps); bs = bounds(ps)
emit('3blaze_logo_stacked', vb((0,0,total_w,bs[3])), symbol_d(sx,0)+" "+wds, '3blaze — logo verticale')

# sub-brand
for key, word in [('academy','academy'), ('net','.net')]:
    d_, b_ = word_parts(word, SYM_W+GAP)
    emit(f'3blaze_{key}', vb((0,min(0,b_[1]),b_[2],max(FH,b_[3]))), sym+" "+d_, f'3blaze {word}',
         colors=('mono','black','cream','orange' if key=='academy' else 'teal'))
d_, b_ = word_parts('luisa', 0)
emit('luisa', vb((b_[0],min(0,b_[1]),b_[2],max(FH,b_[3]))), d_, 'luisa — IA by 3blaze', colors=('mono','black','cream','wine'))
json.dump(assets, open('/home/claude/brand/logo_assets.json','w'))
print({k:v['viewBox'] for k,v in assets.items()})
