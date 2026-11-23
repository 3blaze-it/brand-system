"""Trama Vetro 2027 (scelta C): '3blaze' ripetuto in vetro gigante su Nero, colori del brand solo sui bordi (dispersione)."""
import numpy as np, sys
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as nd
def hx(c): return np.array([int(c[i:i+2],16) for i in (1,3,5)],np.float32)/255
STOPS=[hx(c) for c in ['#FB4F31','#D98C99','#FDF6E2','#3FA9BA','#1C8FA3','#FB4F31']]
def ramp(t):
    St=np.array(STOPS); n=len(St)-1; t=np.clip(t,0,1)*n; i=np.minimum(t.astype(int),n-1); f=(t-i)[...,None]
    return St[i]*(1-f)+St[i+1]*f
def tiled(W,H,S,k,size=1000,rowgap=.66,rot=-28,bold=16):
    F=ImageFont.truetype('/home/claude/brand/out/fonts/3blazeSans-Regular.ttf',int(size*k*S))
    BW,BH=int(max(W,H)*S*2.0),int(max(W,H)*S*2.0); im=Image.new('L',(BW,BH),0); d=ImageDraw.Draw(im)
    sw=int(bold*k*S); bb=d.textbbox((0,0),'3blaze',font=F,stroke_width=sw); tw=bb[2]-bb[0]; th=int(size*k*S*rowgap)
    for r in range(BH//th+2):
        off=(r%2)*tw*0.5
        for c in range(-1,BW//tw+2): d.text((c*tw-off-bb[0],r*th-bb[1]),'3blaze',font=F,fill=255,stroke_width=sw,stroke_fill=255)
    im=im.rotate(rot,resample=Image.BICUBIC); l=(BW-W*S)//2; t=(BH-H*S)//2
    return np.array(im.crop((l,t,l+W*S,t+H*S)))>127
def trama(W,H,out,S=2,seed=2.1,light=(-.5,-.86)):
    k=max(W,H)/1600; m=tiled(W,H,S,k); WS,HS=W*S,H*S; px=S*k   # 1 "px di progetto" in pixel reali
    sd=(nd.distance_transform_edt(m).astype(np.float32)-nd.distance_transform_edt(~m).astype(np.float32))
    sd=nd.gaussian_filter(sd,2*px)/px; del m
    gy,gx=np.gradient(nd.gaussian_filter(sd,3*px)); g=np.sqrt(gx**2+gy**2)+1e-6; nx,ny=-gx/g,-gy/g; del gx,gy,g
    facing=np.clip(nx*light[0]+ny*light[1],0,1); back=np.clip(-(nx*light[0]+ny*light[1]),0,1); del nx,ny
    yy,xx=np.mgrid[0:HS,0:WS].astype(np.float32); xx/=WS; yy/=HS
    f=0.5+0.5*np.sin(xx*2.2+yy*1.3+seed)*np.cos(yy*1.9-xx*.7+seed*.5); del xx,yy
    rim=4.0; img=np.zeros((HS,WS,3),np.float32)+0.01
    for c,(off,dt) in enumerate(((0.9,-.06),(0,0),(-0.9,.06))):
        col=ramp(np.clip(f+dt,0,1))[...,c]
        ring=np.exp(-((sd-off-0.6)/(rim*.5))**2); inner=np.exp(-((sd-rim*2.2)/(rim*1.6))**2)*0.30
        img[...,c]+=col*(ring*(0.12+1.25*facing**1.4+0.35*back**2)+inner*(0.25+0.6*back))*2.6
    img+=(np.clip(sd/1.5,0,1)*0.06)[...,None]*ramp(f)
    img+=(np.exp(-((sd-1.2)/0.9)**2)*facing**8*0.9)[...,None]
    im=Image.fromarray((np.clip(img,0,1)**0.95*255).astype(np.uint8)).resize((W,H),Image.LANCZOS)
    im.save(out, quality=92) if out.endswith('.jpg') else im.save(out); print(out)
if __name__=='__main__':
    O='/home/claude/brand/out/trama/'
    for W,H,n in [(2560,1440,'16x9'),(1440,2560,'9x16'),(2000,2000,'1x1'),(1754,2480,'A4_verticale'),(2480,1754,'A4_orizzontale')]:
        trama(W,H,O+f'3blaze_trama_vetro_{n}.jpg')
