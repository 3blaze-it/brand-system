from lib import *
from p1 import divider, DIV_WORDS

def stage(x,y,w,h,words=None,size=80,bg=BLACK,r=22):
    words=words or DIV_WORDS[:7]
    return f'<div class="box" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};border-radius:0 0 {r}px {r}px">{rows(words,size,top=0,height=h)}</div>'

def btn(x,y,label,variant='regular',w=None,h=44,ic=None):
    w = w or (len(label)*7.4+44 + (22 if ic else 0))
    inner = (icon(ic,16,BLACK if variant in ('tint','light') else CREAM) + '<span style="width:8px"></span>' if ic else '') + f'<span class="gl-txt">{label}</span>'
    return glass(x,y,w,h,variant=variant,inner=inner)

def circ(x,y,ic,variant='regular',s=44):
    return glass(x,y,s,s,variant=variant,inner=icon(ic,18,BLACK if variant in ('tint','light') else CREAM))

def tabbar(x,y,w,items,cur=0,variant='regular',h=62):
    n=len(items); iw=(w-12)/n; s=''
    for i,(ic,lab) in enumerate(items):
        on=i==cur
        s+=(f'<div style="position:absolute;left:{6+i*iw:.0f}px;top:6px;width:{iw:.0f}px;height:{h-12}px;border-radius:{(h-12)/2}px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;'
            f'{"background:#FDF6E22E;" if on else ""}color:{OR if on else CREAM}">{icon(ic,18,OR if on else CREAM)}<span style="font-size:8px">{lab}</span></div>')
    return glass(x,y,w,h,r=h/2,variant=variant,bezel=18,scale=40,inner=f'<div style="position:absolute;inset:0">{s}</div>')

def ann(x,y,txt,lx,ly,dark=True):
    """etichetta con linea guida: testo a (x,y), linea fino al punto (lx,ly)"""
    import math
    dx,dy=lx-x,ly-y; L=math.hypot(dx,dy); a=math.degrees(math.atan2(dy,dx))
    return (f'<div class="ann" style="left:{x}px;top:{y-4}px;transform:translateX(-100%);padding-right:6px">{txt}</div>'
            f'<div class="ann-l" style="left:{x}px;top:{y}px;width:{L:.0f}px;transform-origin:0 0;transform:rotate({a:.1f}deg)"></div>'
            f'<div class="abs" style="left:{lx-3}px;top:{ly-3}px;width:6px;height:6px;border-radius:50%;background:{OR}"></div>')

def ch5(d):
    divider(d,'05','Liquid Glass','Il materiale dell\'interfaccia 3blaze: vetro vero che rifrange e scompone la luce. Come in iOS, appartiene al livello funzionale (bottoni, barre, finestre) e lascia al contenuto tutta la superficie.',5)
    # 5.1 principio
    b = text_col('5.1','Due livelli','<p>Ogni schermata 3blaze è fatta di due livelli, come le interfacce di sistema di Apple.</p><p>Il <b>livello contenuto</b> (immagini, video, tipografia, testi) occupa tutta la superficie, da bordo a bordo, e scorre sotto i controlli.</p><p>Il <b>livello funzionale</b> galleggia sopra ed è fatto di Liquid Glass: barre di navigazione, barre degli strumenti, bottoni, finestre, menu. Il vetro rifrange il contenuto che passa sotto, così l\'utente percepisce profondità senza perdere il contesto.</p><p>Il vetro non si usa mai per il contenuto stesso.</p>')
    b += stage(420,88,320,560,size=70)
    b += f'<div class="mono abs" style="left:436px;top:102px;font-size:6.4px;color:{CREAM};background:#000A;padding:4px 7px;border-radius:0 0 7px 7px">1 — Livello contenuto</div>'
    b += stage(755,88,320,560,size=70)
    b += glass(770,104,44,44,variant='regular',inner=icon('back',18,CREAM))
    b += glass(1016,104,44,44,variant='regular',inner=icon('share',18,CREAM))
    b += glass(845,118,140,30,variant='regular',inner='<span class="gl-txt" style="font-size:10px">3blaze .net</span>')
    b += tabbar(770,570,290,[('home','Home'),('news','News'),('spark','luisa'),('user','Profilo')])
    b += f'<div class="mono abs" style="left:770px;top:160px;font-size:6.4px;color:{CREAM};background:#000A;padding:4px 7px;border-radius:0 0 7px 7px">2 — Livello funzionale in vetro</div>'
    b += cap(420,660,'Stesso contenuto, con e senza livello funzionale. Il vetro non copre: incornicia e rifrange.')
    d.add(b, sec=5)
    # 5.2 anatomia
    b = text_col('5.2','Anatomia del vetro','<p>Il Liquid Glass 3blaze è un pannello spesso a bordo convesso, simulato con una mappa di spostamento reale (feDisplacementMap) e non con una semplice sfocatura.</p><p>1 — <b>Lente</b>: la fascia del bordo (40 px) piega lo sfondo verso l\'interno.<br>2 — <b>Rifrazione</b>: al centro il contenuto resta leggibile, appena ammorbidito.<br>3 — <b>Dispersione</b>: i canali R, G, B si separano sul bordo; negli angoli nasce l\'arcobaleno.<br>4 — <b>Luce speculare</b>: un riflesso radente dall\'alto a sinistra.<br>5 — <b>Velo</b>: una tinta scura che garantisce la leggibilità (variante regular).<br>6 — <b>Ombra</b>: separa il pannello dal contenuto.</p>')
    b += stage(420,88,655,620,size=96)
    b += glass(560,250,380,250,r=44,variant='regular',bezel=46,scale=84,blur=1.2,extra_style='background-color:#0E0C0A70 !important;',inner=f'<div style="font-size:22px;text-shadow:0 1px 2px #0008">Pannello</div>')
    for n,lx,ly in [(1,578,375),(2,750,330),(3,925,262),(4,598,266),(5,840,450),(6,750,520)]:
        b+=f'<div class="abs" style="left:{lx-10}px;top:{ly-10}px;width:20px;height:20px;border-radius:50%;background:{OR};color:#000;font:500 10px/20px JetBrains Mono;text-align:center;box-shadow:0 0 0 2px #000">{n}</div>'
    d.add(b, sec=5)
    # 5.3 varianti
    b = text_col('5.3','Varianti','<p><b>Regular</b> — la variante di default per barre, bottoni e finestre. Velo scuro e micro-sfocatura: si adatta a qualunque contenuto e garantisce la leggibilità.</p><p><b>Clear</b> — più trasparente, senza velo. Solo sopra contenuti ricchi e stabili (foto, video) quando il controllo deve quasi sparire; se la leggibilità cala si aggiunge un velo al contenuto.</p><p><b>Tinted</b> — il vetro prende il colore della divisione. Solo per l\'azione principale: un elemento tinto per vista.</p><p><b>Light</b> — la versione per il tema Crema.</p>')
    V=[('regular','Regular',BLACK),('clear','Clear',BLACK),('tint','Tinted · Brace',BLACK),('light','Light · tema Crema',CREAM)]
    for i,(v,lab,bg) in enumerate(V):
        x=420+(i%2)*332; y=88+(i//2)*312
        if bg==CREAM:
            b+=f'<div class="box" style="left:{x}px;top:{y}px;width:322px;height:280px;background:#EDE3C6">{rows(["MEDIA","ACADEMY",".NET","LUISA","2027"],56,colors=[BLACK,OR_INK,TEAL,WINE,MUTED_L],top=0,height=280)}</div>'
        else:
            b+=stage(x,y,322,280,size=56)
        b+=btn(x+24,y+30,'Prenota una call',v,ic='calendar')
        b+=circ(x+254,y+30,'share',v)
        b+=tabbar(x+24,y+196,274,[('home','Home'),('grid','Lavori'),('book','Academy'),('user','Tu')],cur=1,variant=('light' if v=='light' else ('regular' if v=='tint' else v)))
        b+=cap(x,y+288,lab)
    d.add(b, sec=5)
    # 5.4 forme e concentricità
    b = text_col('5.4','Forme e concentricità','<p>La forma di default dei controlli è la <b>capsula</b> (raggio = metà altezza): è l\'arco della fiamma applicato all\'interazione. I pannelli usano raggi grandi (32–48 px).</p><p>Gli elementi annidati sono <b>concentrici</b>: il raggio interno è uguale al raggio esterno meno la distanza dal bordo.</p><p style="font-family:JetBrains Mono;font-size:9px;color:#C93A20">r interno = R esterno − padding</p><p>Così un bottone dentro una finestra, o la selezione dentro una barra, condividono lo stesso centro di curvatura.</p>')
    b += stage(420,88,655,620,size=96)
    b += glass(500,170,500,420,r=48,variant='regular',bezel=40,scale=70,inner=f'''
       <div style="position:absolute;left:16px;right:16px;bottom:16px;height:64px;border-radius:32px;background:#FB4F31;display:flex;align-items:center;justify-content:center;color:#000;font-size:14px">Iscriviti al corso</div>
       <div style="position:absolute;left:32px;top:30px;font-size:20px;text-shadow:0 1px 2px #0008">Finestra</div>
       <div style="position:absolute;left:32px;top:62px;width:400px;font-size:11px;line-height:1.5;color:#E8E1CF;text-shadow:0 1px 2px #0008">R esterno 48 px · padding 16 px · r interno 32 px. Il bottone in basso è una capsula alta 64 px, concentrica agli angoli della finestra.</div>''')
    b += f'<svg class="abs" style="left:500px;top:170px;overflow:visible" width="500" height="420"><circle cx="48" cy="372" r="48" fill="none" stroke="{OR}" stroke-dasharray="4 3"/><circle cx="48" cy="372" r="32" fill="none" stroke="#FFD23F" stroke-dasharray="4 3"/><circle cx="48" cy="372" r="2.5" fill="{OR}"/></svg>'
    b += f'<div class="ann" style="left:440px;top:604px;background:#000C;padding:3px 6px;border-radius:0 0 6px 6px">Centro comune · R 48 / r 32</div>'
    d.add(b, sec=5)
    # 5.5 componenti I
    b = text_col('5.5','Componenti — controlli','<p>Bottoni, controlli segmentati, interruttori, cursori e campi di ricerca usano il vetro regular in forma di capsula. L\'azione principale è l\'unica tinta.</p><p>Altezze: 44 px (standard, area di tocco minima), 36 px (compatto), 56 px (prominente). Icone 18 px, tratto 1,7 px. Etichette in 3blaze Sans 12–15 px, Crema con ombra di sicurezza.</p>')
    b += stage(420,88,655,620,size=88)
    b += btn(450,120,'Scopri i corsi','regular')
    b += btn(590,120,'Iscriviti','tint',ic='plus')
    b += circ(720,120,'heart'); b += circ(772,120,'share'); b += circ(824,120,'more')
    b += btn(450,184,'Showreel','clear',ic='play')
    b += cap(450,240,'Bottoni — regular · tinted · icona · clear',color=MUTED_D)
    # segmented
    seg=''.join(f'<div style="flex:1;height:32px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:11px;{"background:#FDF6E233;" if i==0 else ""}">{t}</div>' for i,t in enumerate(['Tutto','Media','Academy','News']))
    b += glass(450,280,360,44,variant='regular',inner=f'<div style="position:absolute;inset:6px;display:flex;gap:2px;text-shadow:0 1px 2px #0008">{seg}</div>')
    b += cap(450,332,'Controllo segmentato — selezione concentrica',color=MUTED_D)
    # toggle
    b += glass(450,370,72,36,variant='tint',inner=f'<div style="position:absolute;right:4px;top:4px;width:28px;height:28px;border-radius:14px;background:{CREAM};box-shadow:0 2px 6px #0006"></div>')
    b += glass(540,370,72,36,variant='regular',inner=f'<div style="position:absolute;left:4px;top:4px;width:28px;height:28px;border-radius:14px;background:{CREAM};box-shadow:0 2px 6px #0006"></div>')
    b += cap(630,384,'Interruttore — acceso tinto, spento regular',color=MUTED_D)
    # slider
    b += f'<div class="abs" style="left:450px;top:452px;width:330px;height:6px;border-radius:3px;background:#FDF6E240"><div style="width:58%;height:6px;border-radius:3px;background:{OR}"></div></div>'
    b += glass(620,436,58,38,variant='clear',inner='')
    b += cap(450,488,'Cursore — binario opaco, manopola in vetro clear',color=MUTED_D)
    # search
    b += glass(450,530,420,48,variant='regular',inner=f'<div style="position:absolute;left:16px;top:15px">{icon("search",18,CREAM)}</div><span class="gl-txt" style="position:absolute;left:46px;top:16px;color:#D9D2C0">Cerca su 3blaze</span><div style="position:absolute;right:6px;top:6px;width:36px;height:36px;border-radius:18px;background:#FDF6E22A;display:flex;align-items:center;justify-content:center">{icon("mic",16,CREAM)}</div>')
    b += cap(450,588,'Campo di ricerca — capsula con azione interna concentrica',color=MUTED_D)
    d.add(b, sec=5)
    # 5.6 componenti II
    b = text_col('5.6','Componenti — barre e finestre','<p><b>Barra di navigazione</b>: bottoni circolari ai lati, titolo in capsula, nessuno sfondo a tutta larghezza: il contenuto scorre fino al bordo.</p><p><b>Tab bar</b>: capsula flottante staccata dal bordo inferiore; la sezione attiva è una capsula interna concentrica in Brace.</p><p><b>Menu</b>: si apre per trasformazione dal bottone che lo genera (morphing).</p><p><b>Finestra (sheet)</b>: raggio 34–48 px, attaccata al bordo inferiore o centrata; contiene controlli concentrici.</p>')
    b += stage(420,88,655,620,size=88)
    b += circ(440,108,'back'); b += glass(510,112,150,36,variant='regular',inner='<span class="gl-txt">Academy</span>'); b += circ(1011,108,'more')
    b += cap(440,160,'Barra di navigazione',color=MUTED_D)
    b += glass(820,180,230,190,r=26,variant='regular',bezel=24,scale=50,inner=''.join(f'<div style="position:absolute;left:10px;right:10px;top:{10+i*42}px;height:38px;border-radius:16px;display:flex;align-items:center;gap:10px;padding-left:12px;font-size:12px;{"background:#FDF6E226;" if i==0 else ""};text-shadow:0 1px 2px #0008">{icon(ic,16,CREAM)}{t}</div>' for i,(ic,t) in enumerate([('share','Condividi'),('calendar','Aggiungi al calendario'),('mail','Invia per email'),('heart','Salva')])))
    b += cap(820,378,'Menu — nasce dal bottone ⋯',color=MUTED_D)
    b += glass(440,250,340,250,r=40,variant='regular',bezel=34,scale=64,inner=f'''<div style="position:absolute;left:50%;top:8px;width:36px;height:5px;margin-left:-18px;border-radius:3px;background:#FDF6E266"></div>
      <div style="position:absolute;left:24px;top:30px;font-size:18px;text-shadow:0 1px 2px #0008">Workshop Brand 2027</div>
      <div class="mono" style="position:absolute;left:24px;top:60px;font-size:7px;color:#D9D2C0">12 MARZO · TERNI · 6 POSTI</div>
      <div style="position:absolute;left:24px;top:84px;width:290px;font-size:11px;line-height:1.5;color:#E8E1CF;text-shadow:0 1px 2px #0008">Una giornata per costruire il sistema d'identità della tua attività, dal segno alle applicazioni.</div>
      <div style="position:absolute;left:16px;right:16px;bottom:16px;height:52px;border-radius:26px;background:#FB4F31;color:#000;display:flex;align-items:center;justify-content:center;font-size:14px">Prenota il posto</div>''')
    b += cap(440,508,'Finestra (sheet) — controlli concentrici',color=MUTED_D)
    b += tabbar(560,620,400,[('home','Home'),('grid','Lavori'),('book','Academy'),('news','News'),('spark','luisa')],cur=2)
    d.add(b, sec=5)
    # 5.7 mobile
    b = text_col('5.7','In applicazione — mobile','<p>Due esempi di app del gruppo. Il contenuto (articoli, immagini, conversazione) arriva fino ai bordi dello schermo; il vetro resta confinato a ciò che si tocca.</p><p><b>3blaze .net</b>: barra di navigazione in vetro, tab bar flottante, bottone di condivisione circolare.</p><p><b>luisa</b>: il campo di scrittura è una capsula di vetro; il bottone di invio è l\'unico elemento tinto (Vinaccia).</p>')
    b += phone_news(430,88)
    b += phone_luisa(760,88)
    d.add(b, sec=5)
    # 5.8 web
    b = text_col('5.8','In applicazione — web','<p>Sul sito 3blaze.it la navigazione è una capsula di vetro flottante, staccata dal bordo superiore; resta visibile durante lo scorrimento e rifrange la scena Prisma e le immagini che le passano sotto.</p><p>L\'azione principale ("Parliamone") è l\'unico elemento tinto. Le card dei servizi sono contenuto opaco, non vetro.</p>')
    b += web_mock(420,100,655,560)
    d.add(b, sec=5)
    # 5.9 regole
    b = text_col('5.9','Regole d\'uso','<p>Il vetro funziona solo se resta raro e funzionale. Le regole qui accanto valgono su schermo, in video e nelle immagini renderizzate per la stampa.</p>')
    R=[(True,'Vetro su contenuto ricco','ok1'),(False,'Vetro su vetro','glassonglass'),(True,'Una sola tinta per vista','ok2'),(False,'Tinte ovunque','tints'),(True,'Testo corto sul vetro','ok3'),(False,'Vetro su fondo piatto','flat')]
    for i,(ok,lab,k) in enumerate(R):
        x=420+(i%3)*222; y=88+(i//3)*312
        bg = f'<div class="box" style="left:{x}px;top:{y}px;width:210px;height:270px;background:{"#1A1A1A" if k=="flat" else BLACK}">' + ('' if k=='flat' else rows(DIV_WORDS[:5],44,top=0,height=270)) + '</div>'
        b+=bg
        if k=='ok1': b+=btn(x+40,y+110,'Guarda','regular',ic='play')
        if k=='glassonglass':
            b+=glass(x+20,y+70,170,130,r=28,variant='regular',inner='')
            b+=f'<div class="abs" style="left:{x+50}px;top:{y+113}px;width:110px;height:44px;border-radius:22px;background:#FDF6E22E;box-shadow:inset 0 0 0 1px #FDF6E255,0 6px 14px #0006;display:flex;align-items:center;justify-content:center;font-size:12px;color:{CREAM}">Annidato</div>'
        if k=='ok2': b+=btn(x+30,y+110,'Iscriviti','tint'); b+=circ(x+136,y+110,'share')
        if k=='tints':
            b+=glass(x+20,y+90,80,44,variant='tint',inner='<span class="gl-txt">Uno</span>'); b+=glass(x+110,y+90,80,44,variant='tint-teal',inner='<span class="gl-txt">Due</span>'); b+=glass(x+65,y+150,80,44,variant='tint-wine',inner='<span class="gl-txt">Tre</span>')
        if k=='ok3': b+=glass(x+20,y+100,170,64,r=32,variant='regular',inner='<span class="gl-txt">Nuovo episodio</span>')
        if k=='flat': b+=glass(x+40,y+110,130,44,variant='regular',inner='<span class="gl-txt">Bottone</span>')
        b+=f'<div class="{"do" if ok else "dont"} mono abs" style="left:{x}px;top:{y+278}px;color:{MUTED_L}">{lab}</div>'
    d.add(b, sec=5)
    # 5.10 accessibilità e movimento
    b = text_col('5.10','Accessibilità e movimento','<p>Il vetro rispetta le impostazioni di sistema dell\'utente.</p><p><b>Riduci trasparenza</b>: il pannello diventa opaco (Superficie 2, #1A1A1A) e perde rifrazione e dispersione.<br><b>Aumenta contrasto</b>: velo più scuro e bordo Crema 1 px al 60%.<br><b>Riduci movimento</b>: niente morphing, transizioni a dissolvenza da 160 ms.</p><p>Testo sul vetro: contrasto ≥ 4,5:1 misurato sul punto peggiore dello sfondo, non sulla media. Area di tocco minima 44 × 44 px.</p><p>Movimento: 160 ms per i passaggi di stato, 280 ms per l\'apertura di menu e finestre, curva cubic-bezier(.2,.8,.2,1). Gli elementi vicini si fondono e si separano come gocce.</p>')
    b += stage(420,88,320,300,size=56)
    b += glass(450,160,260,150,r=34,variant='regular',inner='<span class="gl-txt" style="font-size:14px">Standard</span>')
    b += stage(755,88,320,300,size=56)
    b += f'<div class="abs" style="left:785px;top:160px;width:260px;height:150px;border-radius:34px;background:#1A1A1A;display:flex;align-items:center;justify-content:center;color:{CREAM};font-size:14px;box-shadow:0 0 0 1px #FDF6E299">Riduci trasparenza</div>'
    b += cap(420,398,'Stesso pannello: impostazione standard e "Riduci trasparenza"')
    # morph sequence
    for i in range(4):
        x=420+i*166
        b+=stage(x,440,154,200,words=['MEDIA','ACADEMY','.NET','LUISA'],size=34)
        ww=[44,80,130,140][i]; hh=[44,44,90,140][i]
        b+=glass(x+77-ww/2,440+100-hh/2,ww,hh,r=min(22,hh/2) if i<2 else 24,variant='regular',inner=icon('more',16,CREAM) if i==0 else '')
    b += cap(420,650,'Morphing: il bottone ⋯ si espande nel menu in 280 ms')
    d.add(b, sec=5)
    # 5.11 codice
    code_web='''&lt;link rel="stylesheet" href="liquid-glass.css"&gt;
&lt;script src="liquid-glass.js"&gt;&lt;/script&gt;

&lt;!-- bottone in vetro, capsula --&gt;
&lt;button class="btn btn--glass"
  data-lg data-lg-radius="22"
  data-lg-bezel="14" data-lg-scale="34"&gt;
  Prenota una call&lt;/button&gt;

&lt;!-- finestra --&gt;
&lt;div data-lg data-lg-radius="40"
  data-lg-bezel="40" data-lg-scale="70"&gt;…&lt;/div&gt;

LiquidGlass.attach(el, { radius: 32,
  bezel: 40, scale: 70, dispersion: .22 });'''
    code_swift='''// iOS / iPadOS / macOS 26+
Button("Iscriviti") { }
  .buttonStyle(.glassProminent)
  .tint(Color("Brace"))        // #FB4F31

Text("3blaze .net")
  .padding()
  .glassEffect(.regular, in: .capsule)

GlassEffectContainer(spacing: 16) {
  HStack { … }                 // si fondono nel morphing
}'''
    b = text_col('5.11','Implementazione','<p><b>Web</b>: la libreria liquid-glass.js genera la mappa di rifrazione per ogni elemento con attributo data-lg e la applica con backdrop-filter. Rifrazione completa su Chromium; su Safari e Firefox passa da sola a un vetro sfocato di riserva.</p><p><b>App native Apple</b>: si usano i materiali di sistema (glassEffect, stili .glass e .glassProminent) con la tinta Brace per l\'azione principale.</p><p><b>Stampa e video</b>: il vetro si inserisce come immagine renderizzata dalla stessa libreria, mai con effetti "vetro" dei programmi di grafica.</p>')
    b += f'<div class="box" style="left:420px;top:88px;width:320px;height:560px;background:#0E0E0E;color:{CREAM}"><div class="mono" style="position:absolute;left:20px;top:18px;font-size:6.4px;color:{MUTED_D}">Web · HTML / JS</div><pre style="position:absolute;left:20px;top:42px;font-family:JetBrains Mono;font-weight:400;font-size:8.2px;line-height:1.6;white-space:pre;color:#E8E1CF">{code_web}</pre></div>'
    b += f'<div class="box" style="left:755px;top:88px;width:320px;height:560px;background:#0E0E0E;color:{CREAM}"><div class="mono" style="position:absolute;left:20px;top:18px;font-size:6.4px;color:{MUTED_D}">Apple · SwiftUI (sistema)</div><pre style="position:absolute;left:20px;top:42px;font-family:JetBrains Mono;font-weight:400;font-size:8.2px;line-height:1.6;white-space:pre;color:#E8E1CF">{code_swift}</pre></div>'
    b += cap(420,660,'File: codice/liquid-glass.js · codice/liquid-glass.css · codice/tokens.css')
    d.add(b, sec=5)

def phone_news(x,y,w=300,h=620):
    sc=f'''<div class="phone" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><div class="scr">
      <div style="position:absolute;inset:0;background:{BLACK}"></div>
      <div style="position:absolute;left:0;right:0;top:0;height:300px;background:url({B}/out/scene/prisma_hero.png) 30% center/cover"></div>
      <div style="position:absolute;left:18px;top:250px"><span class="mono" style="font-size:6.5px;background:{TEAL};color:{CREAM};padding:4px 8px 5px;border-radius:0 0 8px 8px">Matchday · live</span></div>
      <div style="position:absolute;left:18px;right:18px;top:300px;color:{CREAM};font-size:19px;line-height:1.15">Terni, la notte in cui lo stadio ha cambiato voce</div>
      <div class="mono" style="position:absolute;left:18px;top:362px;font-size:6.4px;color:{MUTED_D}">di Nome Cognome · 4 min</div>
      <div style="position:absolute;left:18px;right:18px;top:384px;color:#D9D2C0;font-size:10px;line-height:1.55">Il racconto della serata, minuto per minuto, con le immagini della redazione di 3blaze .net e le voci dei tifosi raccolte a bordo campo.</div>
      <div style="position:absolute;left:18px;right:18px;top:470px;height:90px;border-radius:0 0 18px 18px;background:url({B}/out/scene/linkedin.png) center/cover"></div>
      <div class="island"></div></div></div>'''
    sc+=circ(x+20,y+50,'back')+glass(x+w/2-60,y+56,120,32,variant='regular',inner='<span class="gl-txt" style="font-size:10px">3blaze .net</span>')+circ(x+w-64,y+50,'share')
    sc+=tabbar(x+18,y+h-84,w-36,[('home','Home'),('news','Ultime'),('search','Cerca'),('user','Tu')],cur=1,h=60)
    return sc

def phone_luisa(x,y,w=300,h=620):
    msgs=[(False,'Ciao, sono luisa. Posso preparare il piano editoriale di marzo per 3blaze academy?'),(True,'Sì, tre post a settimana, tono diretto.'),(False,'Ecco una proposta in tre pilastri: Imparare facendo, Dietro le quinte, Storie degli allievi.')]
    m=''; yy=110
    for me,t in msgs:
        hh=18+len(t)//30*15+15
        m+=f'<div style="position:absolute;{"right:14px;background:"+WINE+";color:"+CREAM if me else "left:14px;background:#1A1A1A;color:#E8E1CF"};top:{yy}px;max-width:200px;padding:10px 13px;border-radius:{"18px 18px 4px 18px" if me else "18px 18px 18px 4px"};font-size:10px;line-height:1.45">{t}</div>'
        yy+=hh+16
    sc=f'''<div class="phone" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><div class="scr">
      <div style="position:absolute;inset:0;background:{BLACK}">{rows(['LUISA','LUISA','LUISA','LUISA','LUISA','LUISA','LUISA'],62,colors=['#2A1418'],top=0,height=600)}</div>
      {m}<div class="island"></div></div></div>'''
    sc+=glass(x+w/2-38,y+52,76,32,variant='regular',inner=f'<div style="width:40px">{logo("luisa",CREAM)}</div>')+circ(x+20,y+46,'back')+circ(x+w-64,y+46,'settings')
    sc+=glass(x+18,y+h-80,w-36,52,variant='regular',inner=f'<span class="gl-txt" style="position:absolute;left:20px;top:18px;color:#BDB6A5;font-size:11px">Scrivi a luisa…</span>')
    sc+=glass(x+w-18-48,y+h-78,48,48,variant='tint-wine',inner=icon('arrow',18,CREAM))
    return sc

def web_mock(x,y,w,h):
    s=f'''<div class="win" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">
      <div style="position:absolute;left:0;right:0;top:0;height:{h*0.62:.0f}px;background:{BLACK}">{rows(size=70,top=0,height=int(h*0.62))}</div>
      <div style="position:absolute;left:36px;top:{h*0.62-58:.0f}px;width:150px">{logo('3blaze_claim',CREAM)}</div>
      <div style="position:absolute;left:0;right:0;top:{h*0.62:.0f}px;bottom:0;background:{CREAM}">
        {''.join(f'<div style="position:absolute;left:{24+i*203}px;top:22px;width:190px;height:150px;border-radius:0 0 20px 20px;background:{c};color:{ink}"><div class="mono" style="position:absolute;left:14px;top:12px;font-size:6px">{lab}</div><div style="position:absolute;left:14px;bottom:14px;font-size:14px;font-style:italic">{t}</div></div>' for i,(c,ink,lab,t) in enumerate([(BLACK,CREAM,"01 — media","Contenuti che restano accesi"),(OR,BLACK,"02 — academy","Si impara facendo fuoco"),(TEAL,CREAM,"03 — .net","Notizie dal campo")]))}
      </div>
      <div style="position:absolute;left:0;right:0;top:0;height:26px;background:#0000;display:flex;gap:6px;align-items:center;padding-left:12px">{''.join(f'<span style="width:9px;height:9px;border-radius:50%;background:{c}"></span>' for c in ['#FF5F57','#FEBC2E','#28C840'])}</div></div>'''
    s+=glass(x+w/2-170,y+105,340,128,shape='symbol',bezel=20,scale=60,variant='clear')
    s+=glass(x+w/2-270,y+40,410,48,variant='regular',inner=f'''<div style="position:absolute;left:18px;top:15px;width:96px">{logo("3blaze_logo_horizontal",CREAM)}</div>
        <div style="position:absolute;left:150px;top:17px;display:flex;gap:22px;font-size:11px;text-shadow:0 1px 2px #0008">{''.join(f"<span>{t}</span>" for t in ["Lavori","Academy","News","luisa"])}</div>''')
    s+=glass(x+w/2+152,y+40,118,48,variant='tint',inner='<span class="gl-txt" style="font-size:11px">Parliamone</span>')
    return s
