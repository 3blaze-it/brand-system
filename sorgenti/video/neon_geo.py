import sys, json, numpy as np
sys.path.insert(0,'/home/claude/brand'); from build_trama import tiled
from skimage import measure
from PIL import Image
W,H=1080,1920
# stessa geometria del JPG 9x16 (1440x2560) mostrato a 1080x1920
m=tiled(1440,2560,1,2560/1600)
im=Image.fromarray((m*255).astype(np.uint8)).resize((W,H),Image.LANCZOS)
a=np.array(im)/255.
pad=np.pad(a,1)
cs=measure.find_contours(pad,0.5)
O=np.array([540.0,960.0])
out=[]
for c in cs:
    c=c[:,::-1]-1  # (x,y)
    if len(c)<40: continue
    c=measure.approximate_polygon(c,0.8)
    closed=np.allclose(c[0],c[-1])
    pts=c[:-1] if closed else c
    # parte dal punto più vicino al centro
    d=np.hypot(*(pts-O).T); i=int(d.argmin()); pts=np.roll(pts,-i,axis=0) if closed else pts
    on=((pts[:,0]>-200)&(pts[:,0]<W+200)&(pts[:,1]>-200)&(pts[:,1]<H+200)).any()
    if not on: continue
    dd='M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in pts)+(' Z' if closed else '')
    out.append({'d':dd,'sx':float(pts[0,0]),'sy':float(pts[0,1]),'dist':float(d.min()),'closed':bool(closed)})
out.sort(key=lambda o:o['dist'])
json.dump(out,open('neon.json','w')); print(len(out), [round(o['dist']) for o in out[:8]])
