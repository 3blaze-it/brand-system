from lib import *
from build_logo_geo import *

DIV_WORDS=['MEDIA','ACADEMY','.NET','LUISA','HOLDING','2027','MEDIA','ACADEMY']

def tabbar(cur, y=40):
    """Barra di navigazione in vetro (livello funzionale) con le sezioni; la corrente è una capsula tinta concentrica."""
    labels=['Marchio','Architettura','Colore','Tipografia','Glass','Grafica','Applicazioni','Voce']
    w=8*84+16; x=(W-w)//2
    items=''
    for i,l in enumerate(labels):
        on = (i+1)==cur
        items+=(f'<div style="position:absolute;left:{8+i*84}px;top:6px;width:84px;height:32px;border-radius:16px;display:flex;align-items:center;justify-content:center;'
                f'{"background:#FB4F31;color:#000;" if on else ""}font-size:10px">{l}</div>')
    return glass(x,y,w,44,r=22,variant='regular',bezel=14,scale=34,inner=f'<div style="position:absolute;inset:0">{items}</div>')

def cover(d):
    b = rows(DIV_WORDS[:7], 118, top=0, height=H)
    b += glass(56, 420, 600, 300, r=40, variant='regular', bezel=44, scale=80, extra_style='background-color:#0A0908B8 !important;', inner=f'''
      <div style="position:absolute;left:36px;top:34px;width:230px">{logo('3blaze_logo_horizontal',CREAM)}</div>
      <div class="mono" style="position:absolute;left:36px;top:104px;font-size:7.5px;color:{MUTED_D}">Corporate Brand Guidelines</div>
      <div style="position:absolute;left:34px;top:124px;font-size:38px;line-height:1.02;letter-spacing:-.01em">Il manuale<br>dell'identità 2027</div>
      <div class="it" style="position:absolute;left:36px;top:236px;font-size:12px;color:#D9D2C0">Spigoli in alto, curve in basso. Come il fuoco.</div>''')
    b += glass(56+600+16, 420+300-48, 150, 48, variant='tint', inner='<span class="gl-txt">Edizione 1.0</span>')
    b += glass(56+600+16+158, 420+300-48, 48, 48, variant='regular', inner=icon('arrow',20,CREAM))
    b += f'<div class="mono abs" style="right:48px;top:30px;font-size:7px;color:{MUTED_D}">Holding · Media · Academy · News · IA</div>'
    d.add(b, dark=True, chrome=False)

def toc(d, entries):
    b = f'<div class="abs" style="left:48px;top:88px;width:320px"><div class="code mono">Indice</div><div class="h1" style="margin-top:10px">Come è fatto<br>questo manuale</div>'
    b += f'<div class="p" style="margin-top:14px">Dieci capitoli, dal segno alle applicazioni. Ogni regola rimanda a un valore misurabile (unità di griglia, codice colore, token) così che designer, fornitori, sviluppatori e strumenti di intelligenza artificiale arrivino allo stesso risultato.</div></div>'
    col=[entries[:5],entries[5:]]
    for c,items in enumerate(col):
        for i,(num,title,pg,subs) in enumerate(items):
            x=420+c*330; y=96+i*126
            b+=f'<div class="rule" style="left:{x}px;top:{y}px;width:300px"></div>'
            b+=f'<div class="abs" style="left:{x}px;top:{y+10}px;width:300px"><div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:\'3blaze Display\';font-size:28px;color:{OR}">{num}</span><span class="mono" style="font-size:7px;color:{MUTED_L}">p. {pg:03d}</span></div><div class="h2" style="margin-top:4px">{title}</div><div class="p" style="margin-top:4px;font-size:8px;line-height:1.45;color:{MUTED_L}">{subs}</div></div>'
    d.add(b, sec=0)

def divider(d, num, title, desc, sec):
    b = rows(DIV_WORDS[(sec)%3:(sec)%3+7], 112, top=0, height=H)
    b += tabbar(sec)
    b += glass(56, 470, 560, 270, r=40, variant='regular', bezel=44, scale=80, extra_style='background-color:#0A0908CC !important;', inner=f'''
      <div style="position:absolute;left:34px;top:20px;font-family:'3blaze Display';font-size:110px;line-height:1;color:{OR}">{num}</div>
      <div style="position:absolute;left:36px;top:150px;font-size:34px;line-height:1.05">{title}</div>
      <div style="position:absolute;left:36px;top:200px;width:470px;font-size:10.5px;line-height:1.5;color:#D9D2C0">{desc}</div>''')
    d.add(b, dark=True, sec=sec)

def intro(d):
    b = text_col('0.1', 'Un gruppo,<br>quattro fuochi',
      '<p>3blaze nasce come agenzia di comunicazione e diventa nel 2027 una holding con quattro attività distinte: <b>3blaze media</b> (strategia, contenuti, video, brand management), <b>3blaze academy</b> (formazione), <b>3blaze .net</b> (informazione) e <b>luisa</b> (intelligenza artificiale proprietaria).</p>'
      '<p>Il nuovo sistema d\'identità tiene insieme queste anime senza appiattirle: un solo segno, la fiamma, ripetuta tre volte; un solo carattere, il 3blaze Sans; un colore per ogni divisione; un materiale comune, il liquid glass, che dà forma a tutto ciò che si tocca.</p>'
      '<p>Questo manuale descrive le regole per usare il sistema con coerenza in ogni punto di contatto, fisico e digitale.</p>')
    b += f'<div class="box" style="left:420px;top:88px;width:655px;height:620px;background:{BLACK}">{rows(size=100,top=0,height=620)}</div>'
    b += glass(420+77,88+170,500,190,shape='symbol',bezel=30,scale=80,variant='clear')
    b += f'<div class="abs" style="left:{420+655-40-190}px;top:{88+620-40-26}px;width:190px">{logo("3blaze_claim",CREAM)}</div>'
    b += cap(420, 720, 'La scena del gruppo: il marchio in trasparenza, le tre fiamme di vetro, il claim come firma')
    d.add(b, sec=0)

def principles(d):
    b = text_col('0.2','Cinque principi','<p>Ogni scelta del sistema discende da cinque principi. Quando un caso non è previsto dal manuale, si torna qui.</p>')
    P=[('01','Un segno, tre fiamme','Il simbolo non si ridisegna, non si scompone, non si anima fuori dalle regole del capitolo 1.'),
       ('02','Una divisione, un colore','Ogni materiale ha un colore dominante e al massimo un accento: la Brace.'),
       ('03','Due caratteri, ruoli fissi','3blaze Sans per tutto; 3blaze Display solo per i titoli grandi; il mono per i dati.'),
       ('04','Il vetro è vero o non c\'è','Il liquid glass rifrange davvero e appartiene al livello funzionale: bottoni, barre, finestre.'),
       ('05','Spigoli in alto, curve in basso','La forma della fiamma diventa regola di impaginazione: tagli netti in alto, archi pieni in basso.')]
    for i,(n,t,s) in enumerate(P):
        x=420+(i%2)*330; y=88+(i//2)*210
        b+=f'''<div class="box" style="left:{x}px;top:{y}px;width:310px;height:190px;background:{"#000" if i==4 else "#F2E8CC"};{"color:"+CREAM if i==4 else ""}">
          <div style="position:absolute;left:22px;top:18px;font-family:'3blaze Display';font-size:40px;color:{OR}">{n}</div>
          <div class="h2" style="position:absolute;left:22px;top:84px;width:270px">{t}</div>
          <div class="p" style="position:absolute;left:22px;top:112px;width:262px;{"color:#D9D2C0" if i==4 else ""}">{s}</div></div>'''
    d.add(b, sec=0)

# ---------------- CAPITOLO 1: MARCHIO ----------------
def ch1(d):
    divider(d,'01','Il marchio','Il simbolo a tre fiamme e il logotipo in 3blaze Sans Italic, ricostruiti su una griglia modulare per il 2027: geometria, proporzioni, versioni, colori, usi corretti e scorretti.',1)
    # 1.1
    b = text_col('1.1','Il marchio','<p>Il marchio 3blaze è composto da due elementi in rapporto fisso: il <b>simbolo</b>, tre fiamme identiche, e il <b>logotipo</b>, la parola 3blaze composta in 3blaze Sans Italic.</p><p>La fiamma ha spigoli in alto e una curva piena in basso: è una corona e insieme un fuoco. Ripetuta tre volte esprime il numero del nome, il ritmo e l\'idea di gruppo.</p><p>La versione orizzontale è la versione primaria e va preferita ogni volta che lo spazio lo consente.</p>')
    b += f'<div class="box" style="left:420px;top:88px;width:655px;height:420px;background:#F2E8CC;border-radius:0 0 30px 30px"><div class="abs" style="left:90px;top:170px;width:475px">{logo("3blaze_logo_horizontal")}</div></div>'
    b += f'<div class="box" style="left:420px;top:524px;width:320px;height:184px;background:{BLACK}"><div class="abs" style="left:52px;top:68px;width:216px">{logo("3blaze_logo_horizontal",CREAM)}</div></div>'
    b += f'<div class="box" style="left:755px;top:524px;width:320px;height:184px;background:{OR}"><div class="abs" style="left:52px;top:68px;width:216px">{logo("3blaze_logo_horizontal",BLACK)}</div></div>'
    b += cap(420,720,'Versione primaria orizzontale — positivo su Crema, negativo su Nero, nero su Brace')
    d.add(b, sec=1)
    # 1.2 simbolo
    b = text_col('1.2','Il simbolo','<p>Tre fiamme identiche, alla stessa scala, nello stesso colore, separate da uno spazio costante di 10 moduli. Il simbolo da solo si usa dove il marchio è già noto o dove lo spazio è quadrato: avatar, icone, timbri, ricami, pattern.</p><p>Il simbolo non si scompone: le fiamme non si separano, non si contano diversamente, non si colorano una per divisione.</p>')
    b += f'<div class="box" style="left:420px;top:88px;width:655px;height:620px;background:{BLACK}"><div class="abs" style="left:96px;top:220px;width:463px">{logo("3blaze_symbol",CREAM)}</div>'
    b += f'<div class="mono abs" style="left:96px;top:420px;font-size:7px;color:{MUTED_D}">92u × 35u · passo 34u · spazio 10u</div></div>'
    d.add(b, sec=1)
    # 1.3 costruzione
    b = text_col('1.3','Costruzione della fiamma','<p>La fiamma è costruita su una griglia di <b>24 × 35 moduli</b> (1u = 20 unità-font del 3blaze Sans, UPM 1000).</p><p>Base: semicerchio di raggio 12u. Fianchi verticali. Sommità a corona: gli incavi cadono a 1/4 e 3/4 della larghezza; dalla punta laterale all\'incavo la linea sale a <b>45°</b>, dall\'incavo al picco a <b>60°</b>. Ne derivano quote esatte: punte a 6(√3−1)u, incavi a 6√3u.</p><p>La ricostruzione corregge lo scarto di simmetria dell\'1,1% del disegno precedente.</p>')
    b += f'<div class="abs" style="left:420px;top:88px;width:655px;height:620px">{flame_construction(655,620)}</div>'
    d.add(b, sec=1)
    # 1.4 logotipo
    b = text_col('1.4','Il logotipo','<p>Il logotipo è 3blaze Sans Italic (−9°) con una crenatura ottica disegnata su griglia di un modulo. Dove due lettere si toccano, la successiva taglia la precedente con un canale di knockout di 2u: è la firma "a fiamme accostate".</p><p>Per questo il logotipo si usa solo dai file ufficiali: riscritto con il font, perderebbe tagli e spaziature.</p><p>Il nome si scrive sempre minuscolo: 3blaze.</p>')
    b += f'<div class="box" style="left:420px;top:88px;width:655px;height:330px;background:#F2E8CC"><div class="abs" style="left:60px;top:90px;width:535px">{logo("3blaze_wordmark")}</div></div>'
    b += f'<div class="abs" style="left:420px;top:440px;width:655px"><table class="tbl"><tr><th>Coppia</th><th>3 · b</th><th>b · l</th><th>l · a</th><th>a · z</th><th>z · e</th></tr><tr><td>Crenatura</td><td>−10u</td><td>−8u</td><td>−8u</td><td>−6u</td><td>−5u</td></tr><tr><td>Unità-font</td><td>−200</td><td>−160</td><td>−160</td><td>−120</td><td>−100</td></tr></table>'
    b += f'<div class="p" style="margin-top:18px;width:520px">Canale di knockout: 2u (40 unità-font) attorno alla lettera successiva. Inclinazione: −9°. Ascendenti +3u oltre la cap-height (760 contro 700).</div></div>'
    d.add(b, sec=1)
    # 1.5 proporzioni
    b = text_col('1.5','Proporzioni e allineamenti','<p>L\'altezza della fiamma è uguale alla cap-height del 3blaze Sans (700/1000): simbolo e logotipo condividono la linea delle maiuscole e la linea di base, che coincide con il fondo dell\'arco.</p><p>Lo spazio tra simbolo e logotipo è uguale a quello tra le fiamme: 10u. Le ascendenti di b e l superano la cap-height di 3u.</p>')
    b += f'<div class="abs" style="left:420px;top:88px;width:655px;height:620px">{lockup_lines(655,620)}</div>'
    d.add(b, sec=1)
    # 1.6 area di rispetto
    b = text_col('1.6','Area di rispetto','<p>Attorno al marchio va lasciata libera un\'area pari alla <b>larghezza di una fiamma</b> (24u alla scala d\'uso) su tutti i lati. Nessun testo, immagine o bordo può entrare in quest\'area.</p><p>Per il simbolo da solo e per la fiamma singola l\'area si riduce a metà fiamma.</p>')
    b += f'<div class="abs" style="left:420px;top:88px;width:655px;height:620px">{clearspace(655,620)}</div>'
    d.add(b, sec=1)
    # 1.7 dimensioni minime
    b = text_col('1.7','Dimensioni minime','<p>Sotto queste misure i tagli del logotipo e le punte delle fiamme non si leggono più. In stampa la misura si intende come larghezza del marchio; sullo schermo in pixel CSS.</p><p>Per usi sotto i minimi (favicon, ricamo minuto) si usa la fiamma singola.</p>')
    sizes=[('3blaze_logo_horizontal','Orizzontale','30 mm · 140 px',140),('3blaze_logo_stacked','Verticale','18 mm · 90 px',90),('3blaze_symbol','Simbolo','8 mm · 32 px',32),('3blaze_flame','Fiamma','4 mm · 16 px',11)]
    x=420
    for k,lab,dim,wpx in sizes:
        b+=f'<div class="box" style="left:{x}px;top:88px;width:152px;height:330px;background:#F2E8CC"><div class="abs" style="left:{(152-wpx)/2}px;top:150px;width:{wpx}px">{logo(k)}</div></div>'
        b+=cap(x,432,lab); b+=f'<div class="abs" style="left:{x}px;top:446px;font-size:15px">{dim}</div>'
        x+=167
    b+=f'<div class="abs" style="left:420px;top:520px;width:655px"><table class="tbl"><tr><th>Supporto</th><th>Versione consigliata</th><th>Note</th></tr><tr><td>Penna, gadget, ricamo &lt; 30 mm</td><td>Simbolo o fiamma</td><td>Ricamo: minimo 12 mm per il simbolo</td></tr><tr><td>Favicon, app, avatar</td><td>Fiamma singola / simbolo</td><td>Vedi icone app, capitolo 7</td></tr><tr><td>Incisione laser</td><td>Orizzontale ≥ 40 mm</td><td>Il canale di knockout è 0,3 mm a 40 mm</td></tr></table></div>'
    d.add(b, sec=1)
    # 1.8 versioni
    b = text_col('1.8','Versioni del marchio','<p>Cinque configurazioni, tutte derivate dagli stessi elementi. Non esistono altre composizioni.</p><p><b>Orizzontale</b>: primaria. <b>Verticale</b>: formati quadrati o stretti. <b>Simbolo</b>: avatar e usi iconici. <b>Fiamma</b>: favicon, punto elenco, chiusura. <b>Logotipo</b>: quando il simbolo è già presente nella stessa vista.</p>')
    V=[('3blaze_logo_horizontal','Orizzontale',420,88,420,180,330),('3blaze_logo_stacked','Verticale',855,88,220,180,150),
       ('3blaze_symbol','Simbolo',420,282,300,190,160),('3blaze_flame','Fiamma',735,282,140,190,40),('3blaze_wordmark','Logotipo',890,282,185,190,130)]
    for k,lab,x,y,w,h,lw in V:
        b+=f'<div class="box" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:#F2E8CC"><div class="abs" style="left:{(w-lw)/2}px;top:50%;transform:translateY(-50%);width:{lw}px">{logo(k)}</div></div>'
        b+=cap(x+14,y+12,lab)
    b+=f'<div class="abs" style="left:420px;top:500px;width:655px"><table class="tbl"><tr><th>File</th><th>Formati</th><th>Colori</th></tr>'
    for f,fm in [('3blaze_logo_horizontal','SVG · PNG @2x · PDF'),('3blaze_logo_stacked','SVG · PNG @2x'),('3blaze_symbol','SVG · PNG @2x · ICO'),('3blaze_flame','SVG · PNG · ICO'),('3blaze_wordmark','SVG · PNG @2x')]:
        b+=f'<tr><td class="mono" style="font-size:7px">{f}</td><td>{fm}</td><td>_black · _cream · currentColor</td></tr>'
    b+='</table></div>'
    d.add(b, sec=1)
    # 1.9 colore
    b = text_col('1.9','Versioni cromatiche','<p>Il marchio esiste in due inchiostri: <b>Nero</b> e <b>Crema</b>. Sui fondi di divisione si usa l\'inchiostro che garantisce almeno 3:1 di contrasto. Il marchio non si stampa mai in bianco puro, in grigio, in sfumatura o in più colori.</p><p>Per la stampa a un colore e per l\'incisione si usa la versione al tratto, identica alla nera.</p>')
    combos=[(CREAM,BLACK,'Nero su Crema','Primaria'),(BLACK,CREAM,'Crema su Nero','Negativa'),(OR,BLACK,'Nero su Brace','academy'),(TEAL,CREAM,'Crema su Petrolio','.net'),(WINE,CREAM,'Crema su Vinaccia','luisa'),('#FFFFFF',BLACK,'Nero su carta bianca','Ufficio')]
    for i,(bg,ink,lab,sub) in enumerate(combos):
        x=420+(i%3)*222; y=88+(i//3)*300
        b+=f'<div class="box" style="left:{x}px;top:{y}px;width:210px;height:250px;background:{bg};{"box-shadow:inset 0 0 0 .75px #0000001F" if bg in (CREAM,"#FFFFFF") else ""}"><div class="abs" style="left:35px;top:110px;width:140px">{logo("3blaze_logo_horizontal",ink)}</div></div>'
        b+=cap(x,y+258,f'{lab} — {sub}')
    d.add(b, sec=1)
    # 1.10 su immagini / vetro
    b = text_col('1.10','Marchio su immagini','<p>Su fotografie e video il marchio va posizionato su una zona calma: Crema sulle zone scure, Nero sulle chiare.</p><p>Quando lo sfondo è troppo movimentato, il marchio si appoggia a una <b>superficie Liquid Glass regular</b>, che scurisce e rifrange lo sfondo garantendo il contrasto. Il vetro sta sotto il marchio, mai dentro le sue forme.</p>')
    b += f'<div class="box" style="left:420px;top:88px;width:655px;height:620px;background:{BLACK}">{rows(DIV_WORDS[:7],96,top=0,height=620)}</div>'
    b += glass(420+155, 88+250, 345, 120, r=30, variant='regular', bezel=30, scale=60, inner=f'<div style="width:240px">{logo("3blaze_logo_horizontal",CREAM)}</div>')
    b += f'<div class="abs" style="left:436px;top:104px"><span class="do mono" style="color:{CREAM}">Corretto: vetro regular sotto il marchio</span></div>'
    d.add(b, sec=1)
    # 1.12 marchio con claim
    b = text_col('1.11','Marchio con claim','<p>Il claim <b>Ignite Beyond.</b> si unisce al marchio come una firma, non come un titolo. Si compone in 3blaze Sans Italic, con la maiuscola iniziale di ogni parola e il punto finale.</p><p>Nel lockup ufficiale il claim è allineato all\'inizio del logotipo, sotto la linea di base: altezza delle maiuscole pari al 28% della fiamma, distanza dalla base pari a 10u. Il lockup si usa solo dai file ufficiali (3blaze_logo_claim).</p><p>Il claim non si traduce nei materiali, non si colora, non si compone in Display e non cresce oltre il logo.</p>')
    b += f'<div class="box" style="left:420px;top:88px;width:655px;height:340px;background:#F2E8CC"><div class="abs" style="left:110px;top:102px;width:435px">{logo("3blaze_logo_claim")}</div></div>'
    b += f'<div class="box" style="left:420px;top:444px;width:320px;height:180px;background:{BLACK}"><div class="abs" style="left:50px;top:52px;width:220px">{logo("3blaze_logo_claim",CREAM)}</div></div>'
    b += f'<div class="box" style="left:755px;top:444px;width:320px;height:180px;background:{OR}"><div class="abs" style="left:50px;top:52px;width:220px">{logo("3blaze_logo_claim",BLACK)}</div></div>'
    b += cap(420,634,'Lockup marchio + claim — positivo, negativo, su Brace')
    d.add(b, sec=1)
    # 1.11 usi scorretti
    b = text_col('1.12','Usi scorretti','<p>Ogni alterazione del marchio ne indebolisce il riconoscimento. Gli esempi qui accanto non sono un elenco chiuso: in generale, il marchio non si modifica in nessun modo.</p>')
    bad=[('rotate(-12deg)','','Non ruotare'),('scaleX(1.35)','','Non deformare'),('','filter:drop-shadow(4px 6px 0 #FB4F31)','Non aggiungere ombre'),('','opacity:.35','Non ridurre il contrasto'),
         ('','','Non cambiare carattere'),('','','Non colorare le fiamme'),('','','Non riordinare gli elementi'),('','','Non usare vetro dentro il segno')]
    for i,(tf,flt,lab) in enumerate(bad):
        x=420+(i%4)*166; y=88+(i//4)*310
        if lab=='Non cambiare carattere':
            inner=f'<div style="display:flex;align-items:center;gap:8px;justify-content:center;margin-top:120px"><div style="width:52px">{logo("3blaze_symbol")}</div><span style="font-family:Georgia,serif;font-size:21px">3Blaze</span></div>'
        elif lab=='Non colorare le fiamme':
            inner=f'<div style="display:flex;gap:4px;justify-content:center;margin-top:118px">'+''.join(f'<div style="width:20px">{flame(c)}</div>' for c in [OR,TEAL,WINE])+f'<div style="width:66px;margin-left:4px">{logo("3blaze_wordmark")}</div></div>'
        elif lab=='Non riordinare gli elementi':
            inner=f'<div style="display:flex;align-items:center;gap:6px;justify-content:center;margin-top:120px"><div style="width:80px">{logo("3blaze_wordmark")}</div><div style="width:44px">{logo("3blaze_symbol")}</div></div>'
        elif lab=='Non usare vetro dentro il segno':
            inner=f'<div style="width:126px;margin:118px auto 0;background:linear-gradient(90deg,#FF4F31,#FFD23F,#3DDC97,#2EC4FF,#7B61FF);-webkit-mask:url(\'data:image/svg+xml;utf8,<svg xmlns=&quot;http://www.w3.org/2000/svg&quot;/>\');">{logo("3blaze_logo_horizontal","#7B61FF")}</div>'
        else:
            inner=f'<div style="width:126px;margin:118px auto 0;transform:{tf or "none"};{flt}">{logo("3blaze_logo_horizontal")}</div>'
        b+=f'<div class="box" style="left:{x}px;top:{y}px;width:154px;height:262px;background:#F2E8CC">{inner}<svg class="abs" style="left:0;top:0" width="154" height="262"><line x1="10" y1="10" x2="144" y2="252" stroke="{OR}" stroke-width="1.2"/></svg></div>'
        b+=f'<div class="dont mono abs" style="left:{x}px;top:{y+272}px;color:{MUTED_L}">{lab}</div>'
    d.add(b, sec=1)

# ---------------- CAPITOLO 2: ARCHITETTURA ----------------
def ch2(d):
    divider(d,'02','Architettura di marca','Una holding e quattro divisioni con lo stesso segno: come si costruiscono i marchi di divisione, come convivono e come si firmano le collaborazioni.',2)
    b = text_col('2.1','Struttura del gruppo','<p>L\'architettura è a <b>marchio ombrello</b>: le divisioni condividono il simbolo e il carattere e si distinguono per nome e colore. Fa eccezione luisa, prodotto di intelligenza artificiale con un nome proprio, che porta la fiamma come punto della i.</p><p>Il marchio 3blaze senza specificazione rappresenta sia la holding sia la divisione media.</p>')
    b += f'<div class="box" style="left:420px;top:88px;width:655px;height:200px;background:{BLACK}"><div class="abs" style="left:207px;top:78px;width:240px">{logo("3blaze_logo_horizontal",CREAM)}</div><div class="mono abs" style="left:24px;top:20px;font-size:7px;color:{MUTED_D}">Holding · 3BLAZE S.R.L.S.</div></div>'
    b += '<svg class="abs" style="left:420px;top:288px" width="655" height="60"><path d="M327 0v30M82 30h491M82 30v30M245 30v30M409 30v30M573 30v30" stroke="#00000055" stroke-width=".9" fill="none"/></svg>'
    cols=[(BLACK,'3blaze_symbol',CREAM,'media','Strategia, contenuti, video, brand management'),(OR,'3blaze_academy',BLACK,'academy','Corsi, workshop, percorsi per aziende e scuole'),(TEAL,'3blaze_net',CREAM,'news','Informazione, rubriche, matchday e territorio'),(WINE,'luisa',CREAM,'IA','Assistente di intelligenza artificiale proprietaria')]
    for i,(bg,k,ink,lab,desc) in enumerate(cols):
        x=420+i*166
        lw={'3blaze_symbol':70,'3blaze_academy':120,'3blaze_net':100,'luisa':70}[k]
        b+=f'<div class="box" style="left:{x}px;top:348px;width:154px;height:240px;background:{bg};color:{ink}"><div class="mono abs" style="left:14px;top:14px;font-size:6.4px">{lab}</div><div class="abs" style="left:14px;top:110px;width:{lw}px">{logo(k,ink)}</div><div class="abs" style="left:14px;top:168px;width:126px;font-size:8.6px;line-height:1.45">{desc}</div></div>'
    b+=cap(420,600,'Marchio ombrello — il colore distingue, il segno unisce')
    d.add(b, sec=2)
    b = text_col('2.2','Marchi di divisione','<p>Ogni marchio di divisione si costruisce con la stessa regola del marchio principale: simbolo, spazio di 10u, nome della divisione in 3blaze Sans Italic con crenatura ottica, fondo delle fiamme sulla linea di base.</p><p>Il colore del marchio di divisione può essere quello della divisione (su Crema o Nero) oppure l\'inchiostro neutro sul fondo di divisione.</p>')
    for i,(k,bg,ink,lab) in enumerate([('3blaze_academy',CREAM,OR,'academy — Brace su Crema'),('3blaze_academy',OR,BLACK,'academy — Nero su Brace'),('3blaze_net',BLACK,TEAL_L,'.net — Petrolio chiaro su Nero'),('3blaze_net',TEAL,CREAM,'.net — Crema su Petrolio'),('luisa',BLACK,WINE_L,'luisa — Vinaccia chiaro su Nero'),('luisa',WINE,CREAM,'luisa — Crema su Vinaccia')]):
        x=420+(i%2)*332; y=88+(i//2)*208
        lw={'3blaze_academy':250,'3blaze_net':200,'luisa':110}[k]
        b+=f'<div class="box" style="left:{x}px;top:{y}px;width:322px;height:176px;background:{bg};{"box-shadow:inset 0 0 0 .75px #0000001F" if bg==CREAM else ""}"><div class="abs" style="left:{(322-lw)/2}px;top:50%;transform:translateY(-50%);width:{lw}px">{logo(k,ink)}</div></div>'
        b+=cap(x,y+182,lab)
    d.add(b, sec=2)
    b = text_col('2.3','Nuove divisioni','<p>Una nuova attività del gruppo riceve un marchio con la stessa costruzione: simbolo + nome. Il nome è una parola sola, minuscola, senza articoli. Il colore si sceglie fuori dalla palette esistente, con un contrasto ≥ 4,5:1 con il Crema, e si aggiunge ai token prima di qualunque uso.</p><p>Un prodotto con nome proprio (come luisa) può omettere il simbolo solo se porta la fiamma all\'interno del logotipo.</p>')
    b += f'<div class="box" style="left:420px;top:88px;width:655px;height:300px;background:#F2E8CC"><div class="abs" style="left:70px;top:118px;display:flex;align-items:flex-end;gap:0">'
    b += f'<div style="width:220px">{logo("3blaze_symbol")}</div><div style="width:48px;height:84px;background:#FB4F3133;margin:0 0 0 0"></div><div style="font-family:\'3blaze Sans\';font-style:italic !important;font-size:94px;line-height:.74;color:#0000004D;letter-spacing:-.02em">nome</div></div>'
    b += f'<div class="mono abs" style="left:290px;top:212px;font-size:6.4px;color:{OR_INK}">10u</div></div>'
    b += f'<div class="abs" style="left:420px;top:410px;width:655px"><table class="tbl"><tr><th>Passo</th><th>Regola</th></tr><tr><td>1. Nome</td><td>Una parola, minuscola, pronunciabile in italiano e in inglese</td></tr><tr><td>2. Composizione</td><td>3blaze Sans Italic, crenatura su griglia 1u, knockout 2u dove le lettere si toccano</td></tr><tr><td>3. Allineamento</td><td>Fondo fiamme = linea di base; cap-height = altezza fiamma; spazio 10u</td></tr><tr><td>4. Colore</td><td>Nuovo token di divisione + variante *-ink per il testo su Nero</td></tr><tr><td>5. Approvazione</td><td>Brand owner della holding, prima di qualsiasi stampa o pubblicazione</td></tr></table></div>'
    d.add(b, sec=2)
    b = text_col('2.4','Co-branding','<p>Con partner, clienti e istituzioni il marchio 3blaze si affianca all\'altro marchio separato da un filetto verticale. Le due altezze si bilanciano otticamente; lo spazio tra marchio e filetto è di una fiamma per lato.</p><p>Per le produzioni realizzate per conto di clienti si usa la firma di endorsement "una produzione 3blaze media", in mono, a fondo pagina o nei titoli di coda.</p>')
    b += f'''<div class="box" style="left:420px;top:88px;width:655px;height:300px;background:#F2E8CC"><div class="abs" style="left:96px;top:128px;width:210px">{logo("3blaze_logo_horizontal")}</div>
      <div class="abs" style="left:345px;top:104px;width:0;height:92px;border-left:.9px solid #000"></div>
      <div class="abs" style="left:384px;top:118px;width:170px;height:64px;border:1px dashed #00000066;border-radius:0 0 18px 18px;display:flex;align-items:center;justify-content:center" ><span class="mono" style="font-size:7px;color:{MUTED_L}">Marchio partner</span></div></div>'''
    b += f'''<div class="box" style="left:420px;top:408px;width:655px;height:300px;background:{BLACK}">{rows(["PARTNER","EVENTO","2027","PARTNER"],80,top=0,height=300)}</div>'''
    b += glass(420+140, 408+190, 375, 64, r=32, variant='regular', bezel=20, scale=42, inner=f'<span class="mono" style="font-size:8px;color:{CREAM};text-shadow:0 1px 2px #0008">Una produzione</span><div style="width:110px;margin-left:12px">{logo("3blaze_logo_horizontal",CREAM)}</div>')
    b += cap(436,424,'Endorsement su video e contenuti per clienti',color=MUTED_D)
    d.add(b, sec=2)
