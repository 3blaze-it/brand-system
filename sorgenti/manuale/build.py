import sys
from lib import Doc
import p1, p2, p3, p4
CH=[('01','Il marchio','Simbolo, logotipo, costruzione, versioni, usi',p1.ch1),('02','Architettura di marca','Holding, divisioni, nuove divisioni, co-branding',p1.ch2),
    ('03','Colore','Palette, divisioni, token digitali, contrasti',p2.ch3),('04','Tipografia','3blaze Sans, Display, mono, scala, regole',p2.ch4),
    ('05','Liquid Glass','Livelli, anatomia, varianti, componenti, codice',p3.ch5),('06','Elementi grafici','Scena Prisma, griglie, icone, fotografia',p4.ch6),
    ('07','Applicazioni','Cancelleria, slide, badge, insegne, social, video',p4.ch7),('08','Voce','Tono, manifesto, scrittura',p4.ch8),('09','Appendice','File, checklist, lettura automatica',p4.ch9)]
def make(pages):
    d=Doc(); p1.cover(d); p1.toc(d,[(a,b,pages.get(a,0),c) for a,b,c,_ in CH]); p1.intro(d); p1.principles(d)
    got={}
    for a,b,c,fn in CH:
        got[a]=len(d.pages)+1; fn(d)
    p4.back(d); return d,got
d,got=make({}); d,got=make(got)
open('guide.html','w').write(d.html()); print(len(d.pages), got)
