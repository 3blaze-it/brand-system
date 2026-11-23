from lib import *
from p1 import divider

def swatch(x,y,w,h,bg,name,codes,ink=CREAM,big=False,border=False):
    lines=''.join(f'<div>{c}</div>' for c in codes)
    return (f'<div class="box" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};color:{ink};{"box-shadow:inset 0 0 0 .75px #0000001F;" if border else ""}">'
            f'<div style="position:absolute;left:18px;top:16px;font-size:{22 if big else 15}px">{name}</div>'
            f'<div class="mono" style="position:absolute;left:18px;bottom:18px;font-size:6.6px;line-height:1.7;letter-spacing:.1em">{lines}</div></div>')

def ch3(d):
    divider(d,'03','Colore','Due fondi, quattro colori di divisione, una sola Brace. Valori per stampa e schermo, abbinamenti per settore, proporzioni e contrasti verificati.',3)
    b = text_col('3.1','Palette istituzionale','<p>Il gruppo vive su due fondi: <b>Nero</b> e <b>Crema</b>. Il Crema sostituisce il bianco: è il colore della carta, del logo in negativo e del testo su fondo scuro.</p><p>La <b>Brace</b> è il colore della fiamma: colore della divisione academy e unico accento di tutto il gruppo.</p><p>I valori CMYK e Pantone sono punti di partenza da validare con prova colore sulla carta scelta.</p>')
    b += swatch(420,88,320,420,BLACK,'Nero',['HEX #000000','RGB 0 0 0','CMYK 60 40 40 100','PANTONE Black 6 C','RAL 9005'],big=True)
    b += swatch(755,88,320,420,CREAM,'Crema',['HEX #FDF6E2','RGB 253 246 226','CMYK 0 2 10 0','PANTONE 9224 C','RAL 9001'],ink=BLACK,big=True,border=True)
    b += swatch(420,524,655,184,OR,'Brace',['HEX #FB4F31 · RGB 251 79 49','CMYK 0 80 85 0 · PANTONE 172 C','RAL 2004'],ink=BLACK,big=True)
    d.add(b, sec=3)
    b = text_col('3.2','Colori di divisione','<p>Ogni divisione possiede un colore pieno, usato come fondo dei suoi materiali e come colore del suo marchio. Il colore di una divisione non si usa per un\'altra.</p><p>Su fondo Nero, Petrolio e Vinaccia non hanno contrasto sufficiente come testo: si usano le loro varianti chiare (Petrolio chiaro, Vinaccia chiaro), previste solo per testi e marchi in negativo.</p>')
    data=[(BLACK,'media','Nero',['#000000'],CREAM,None),(OR,'academy','Brace',['#FB4F31','CMYK 0 80 85 0','PANTONE 172 C'],BLACK,('#C93A20','Brace testo')),
          (TEAL,'.net','Petrolio',['#006172','CMYK 95 40 35 25','PANTONE 3155 C'],CREAM,(TEAL_L,'Petrolio chiaro')),(WINE,'luisa','Vinaccia',['#4D1821','CMYK 35 90 65 60','PANTONE 4975 C'],CREAM,(WINE_L,'Vinaccia chiaro'))]
    for i,(bg,div,nm,codes,ink,var) in enumerate(data):
        x=420+i*166
        b+=f'<div class="box" style="left:{x}px;top:88px;width:154px;height:440px;background:{bg};color:{ink}"><div class="mono" style="position:absolute;left:14px;top:14px;font-size:6.4px">{div}</div><div style="position:absolute;left:14px;top:40px;font-size:16px">{nm}</div><div class="mono" style="position:absolute;left:14px;bottom:16px;font-size:6.2px;line-height:1.75">{"<br>".join(codes)}</div></div>'
        if var:
            vb=var[0]; vi=BLACK
            b+=f'<div class="box" style="left:{x}px;top:540px;width:154px;height:120px;background:{vb};color:{vi}"><div style="position:absolute;left:14px;top:14px;font-size:11px">{var[1]}</div><div class="mono" style="position:absolute;left:14px;bottom:14px;font-size:6.2px">{vb}</div></div>'
        else:
            b+=f'<div class="box" style="left:{x}px;top:540px;width:154px;height:120px;background:#1A1A1A;color:{CREAM}"><div style="position:absolute;left:14px;top:14px;font-size:11px">Superficie</div><div class="mono" style="position:absolute;left:14px;bottom:14px;font-size:6.2px">#1A1A1A</div></div>'
    b+=cap(420,672,'Riga inferiore: varianti per il testo e i marchi in negativo — mai come fondi')
    d.add(b, sec=3)
    b = text_col('3.3','Colori digitali e funzionali','<p>Sugli schermi il sistema ha due temi: <b>Nero</b> (primario) e <b>Crema</b>. I token cambiano valore in base al tema; i colori di divisione restano fissi.</p><p>I sei colori Prisma esistono solo come dispersione del Liquid Glass: non sono colori del brand e non si usano per fondi, testi o icone.</p>')
    rowsd=[('ground','#000000','#FDF6E2','Fondo pagina'),('surface-1','#0E0E0E','#F6EDD3','Sezioni'),('surface-2','#1A1A1A','#EDE3C6','Card, campi'),('ink','#FDF6E2','#000000','Testo'),('ink-muted','#A8A294','#6B665C','Testo secondario'),('hairline','#FDF6E2 · 14%','#000000 · 12%','Filetti'),('accent','#FB4F31','#C93A20','Accento / CTA'),('focus','#2EC4FF','#2EC4FF','Focus tastiera')]
    t='<table class="tbl"><tr><th>Token</th><th>Tema Nero</th><th>Tema Crema</th><th>Uso</th></tr>'
    for n,a,c,u in rowsd:
        ca=a.split(' ')[0]; cc=c.split(' ')[0]
        t+=f'<tr><td class="mono" style="font-size:7px">--{n}</td><td><span style="display:inline-block;width:11px;height:11px;border-radius:0 0 6px 6px;background:{ca};vertical-align:-2px;margin-right:6px;box-shadow:inset 0 0 0 .6px #0003"></span>{a}</td><td><span style="display:inline-block;width:11px;height:11px;border-radius:0 0 6px 6px;background:{cc};vertical-align:-2px;margin-right:6px;box-shadow:inset 0 0 0 .6px #0003"></span>{c}</td><td>{u}</td></tr>'
    t+='</table>'
    b+=f'<div class="abs" style="left:420px;top:88px;width:655px">{t}</div>'
    pr=['#FF4F31','#FFD23F','#3DDC97','#2EC4FF','#7B61FF','#FF5FA2']
    b+='<div class="abs" style="left:420px;top:470px;width:655px;height:150px;display:flex;border-radius:0 0 22px 22px;overflow:hidden">'+''.join(f'<div style="flex:1;background:{c};position:relative"><span class="mono" style="position:absolute;left:10px;bottom:10px;font-size:6.2px;color:#000">{c}</span></div>' for c in pr)+'</div>'
    b+=cap(420,632,'Prisma 1–6 — solo rifrazione del vetro, mai colori d\'uso')
    d.add(b, sec=3)
    b = text_col('3.4','Proporzioni e abbinamenti','<p>Su ogni superficie un colore domina: <b>70% fondo</b> (Nero o Crema), <b>20% colore di divisione</b>, <b>al massimo 10% Brace</b>.</p><p>La Brace non diventa mai il fondo di un materiale della holding: è un segnale, non un ambiente. Fanno eccezione i materiali di academy, dove la Brace è il colore di divisione.</p>')
    combos=[('3blaze media',[(BLACK,70),(CREAM,22),(OR,8)]),('3blaze academy',[(OR,62),(BLACK,30),(CREAM,8)]),('3blaze .net',[(TEAL,62),(CREAM,30),(OR,8)]),('luisa',[(WINE,66),(CREAM,34)])]
    for i,(nm,parts) in enumerate(combos):
        y=88+i*150
        b+=f'<div class="abs" style="left:420px;top:{y}px;width:655px;height:118px;display:flex;border-radius:0 0 20px 20px;overflow:hidden;box-shadow:inset 0 0 0 .75px #0000001A">'+''.join(f'<div style="width:{p}%;background:{c};position:relative"><span class="mono" style="position:absolute;left:10px;bottom:10px;font-size:6.2px;color:{BLACK if c in (CREAM,OR) else CREAM}">{p}%</span></div>' for c,p in parts)+'</div>'
        b+=cap(420,y+124,nm)
    d.add(b, sec=3)
    b = text_col('3.5','Contrasti verificati','<p>Tutte le coppie testo/fondo sono verificate secondo WCAG 2.2. Il testo corrente richiede almeno <b>4,5:1</b>; titoli da 24 px in su, logo e icone almeno <b>3:1</b>.</p><p>La matrice indica in verde le coppie valide per qualunque testo, in giallo quelle valide solo per testi grandi e marchi, in rosso quelle vietate.</p>')
    fg=[('Crema','#FDF6E2'),('Nero','#000000'),('Brace','#FB4F31'),('Brace testo','#C93A20'),('Petrolio','#006172'),('Petrolio ch.','#3FA9BA'),('Vinaccia','#4D1821'),('Vinaccia ch.','#D98C99')]
    bg=[('Nero','#000000'),('Crema','#FDF6E2'),('Brace','#FB4F31'),('Petrolio','#006172'),('Vinaccia','#4D1821')]
    def L(h):
        h=h.lstrip('#'); c=[int(h[i:i+2],16)/255 for i in (0,2,4)]; c=[x/12.92 if x<=0.03928 else ((x+0.055)/1.055)**2.4 for x in c]; return .2126*c[0]+.7152*c[1]+.0722*c[2]
    def cr(a,b_):
        la,lb=sorted([L(a),L(b_)],reverse=True); return (la+.05)/(lb+.05)
    t='<table class="tbl" style="font-size:8px"><tr><th>Testo \\ Fondo</th>'+''.join(f'<th>{n}</th>' for n,_ in bg)+'</tr>'
    for fn,fc in fg:
        t+=f'<tr><td>{fn}</td>'
        for bn,bc in bg:
            if fc==bc: t+='<td style="color:#0004">—</td>'; continue
            r=cr(fc,bc); col='#3DDC97' if r>=4.5 else ('#FFD23F' if r>=3 else '#FB4F31')
            t+=f'<td><span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:{col};margin-right:6px"></span>{r:.1f}:1</td>'
        t+='</tr>'
    t+='</table>'
    b+=f'<div class="abs" style="left:420px;top:88px;width:655px">{t}</div>'
    d.add(b, sec=3)

def ch4(d):
    divider(d,'04','Tipografia','Il 3blaze Sans diventa il carattere principale del gruppo; il 3blaze Display è riservato ai titoli grandi; un mono dà voce ai dati. Scala, regole e alternative di sistema.',4)
    b = text_col('4.1','3blaze Sans','<p>Disegnato per il gruppo: ogni lettera segue la fiamma del marchio. Base a semicerchio, fianchi dritti, sommità smussate a 45°. Le aste libere sono tagliate come le punte della corona, la M è la corona stessa, il punto della i è una fiamma.</p><p>Un peso (500) in tondo e corsivo. Il corsivo è la voce del marchio: occhielli, citazioni, oggetti, nomi delle divisioni.</p>')
    b += f'<div class="abs" style="left:420px;top:80px;font-size:150px;line-height:1">Aa Mi</div>'
    b += f'<div class="abs" style="left:420px;top:262px;width:655px;font-size:22px;line-height:1.35">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz<br>0123456789 àèéìòù ÀÈÉÌÒÙ<br>.,:;!?\'“”()[]/&amp;@€%#*+=…</div>'
    b += f'<div class="abs it" style="left:420px;top:460px;width:655px;font-size:22px;line-height:1.35">Spigoli in alto, curve in basso. Come il fuoco.<br>abcdefghijklmnopqrstuvwxyz 0123456789</div>'
    b += f'<div class="abs" style="left:420px;top:560px;width:655px"><table class="tbl"><tr><th>File</th><th>Stile</th><th>Uso</th></tr><tr><td class="mono" style="font-size:7px">3blazeSans-Regular · ttf / woff2</td><td>500 tondo</td><td>Tutto il testo</td></tr><tr><td class="mono" style="font-size:7px">3blazeSans-Italic · ttf / woff2</td><td>500 corsivo (−9°)</td><td>Voce, occhielli, logotipi</td></tr></table></div>'
    d.add(b, sec=4)
    b = text_col('4.2','3blaze Display','<p>Un carattere pesante e inclinato (−12°) con un retino a mezzatinta incorporato nel disegno: non è un effetto, è il font.</p><p>Si usa solo per titoli grandi, da <b>48 px / 18 pt</b> in su, per un massimo di quattro parole o un numero. In maiuscolo per numeri di sezione, cifre chiave e nomi di divisione.</p><p>Sul web può ricevere un leggero sfocato proporzionale (0,009em) che ne ammorbidisce il retino.</p>')
    b += f'<div class="box" style="left:420px;top:88px;width:655px;height:620px;background:{BLACK};color:{CREAM}"><div style="position:absolute;left:34px;top:30px;font-family:\'3blaze Display\';font-size:132px;line-height:.9">2027<br><span style="color:{OR}">ACADEMY</span></div><div style="position:absolute;left:34px;top:300px;font-family:\'3blaze Display\';font-size:44px;line-height:1.1">ABCDEFGHIJKLM<br>NOPQRSTUVWXYZ<br>0123456789 €%</div><div class="mono" style="position:absolute;left:34px;bottom:26px;font-size:7px;color:{MUTED_D}">3blazeDisplay-Regular · 400 · minimo 48 px / 18 pt</div></div>'
    d.add(b, sec=4)
    b = text_col('4.3','Mono e font di sistema','<p><b>JetBrains Mono</b> (licenza OFL) è lo strato "codice" del sistema: etichette in maiuscolo con spaziatura +0,12em, numerazioni, metadati, dati tecnici e snippet. Non si usa mai per frasi.</p><p>Dove i font del brand non possono essere installati (documenti condivisi, email, Office di terzi) si usano le alternative di sistema indicate a lato. I file di marchio restano sempre vettoriali.</p>')
    b += f'<div class="box" style="left:420px;top:88px;width:655px;height:250px;background:#F2E8CC"><div class="mono" style="position:absolute;left:28px;top:30px;font-size:24px;line-height:1.5">01 — MEDIA · TERNI<br>ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>0123456789 → × ≈</div><div class="mono" style="position:absolute;left:28px;bottom:22px;font-size:7px;color:{MUTED_L}">JetBrains Mono 500 · etichette 7–12 px · +0,12em · maiuscolo</div></div>'
    b += f'<div class="abs" style="left:420px;top:360px;width:655px"><table class="tbl"><tr><th>Ruolo</th><th>Brand</th><th>Alternativa di sistema</th><th>Dove</th></tr><tr><td>Testo</td><td>3blaze Sans</td><td>Futura, Century Gothic, Arial</td><td>Email, Office, Google Docs</td></tr><tr><td>Titoli grandi</td><td>3blaze Display</td><td>Arial Black corsivo</td><td>Solo se il PDF non è possibile</td></tr><tr><td>Etichette</td><td>JetBrains Mono</td><td>Menlo, Consolas, Courier New</td><td>Firme email, fogli di calcolo</td></tr></table></div>'
    d.add(b, sec=4)
    b = text_col('4.4','Scala tipografica','<p>La scala è la stessa per schermo e stampa (in stampa i px diventano pt con fattore 0,75). Il Display parte da 48: sotto, i titoli sono in Sans.</p><p>Interlinea stretta per i titoli (0,92–1,15), ampia per il testo (1,5–1,6). Misura ideale del testo corrente: 60–72 caratteri.</p>')
    sc=[('display-xl',"'3blaze Display'",'160/0,92','MEDIA',64),('display-m',"'3blaze Display'",'72/1,0','2027',40),('headline-l',"'3blaze Sans'",'48/1,05','Strategia e codice',30),('headline-m',"'3blaze Sans'",'32/1,15','Un sistema, quattro fuochi',22),('title',"'3blaze Sans'",'24/1,25','3blaze academy',17),('body-l',"'3blaze Sans'",'19/1,55','Ogni progetto parte da una domanda semplice.',13),('body',"'3blaze Sans'",'16/1,6','Strategia, contenuti e design lavorano come un unico sistema.',11),('caption',"'3blaze Sans'",'13/1,45','Foto: backstage matchday, Terni 2027.',9.5),('label',"'JetBrains Mono'",'12/1,3 · +0,12em','01 — MANIFESTO 2027',8)]
    y=88
    for n,f,v,s_,px in sc:
        it='font-style:italic;' if n=='caption' else ''
        b+=f'<div class="rule" style="left:420px;top:{y}px;width:655px"></div><div class="mono abs" style="left:420px;top:{y+8}px;font-size:6.4px;color:{MUTED_L};width:120px">{n}<br><span style="color:{OR_INK}">{v}</span></div><div class="abs" style="left:560px;top:{y+4}px;font-family:{f};font-size:{px}px;line-height:1.05;{it}white-space:nowrap;overflow:hidden;width:515px">{s_}</div>'
        y+=max(40,px*1.15+14)
    d.add(b, sec=4)
    b = text_col('4.5','Regole di composizione','<p>Un solo peso: la gerarchia si costruisce con corpo, corsivo, colore e spazio, mai con il grassetto sintetico. Testo allineato a sinistra, mai giustificato, mai centrato su più di due righe.</p><p>Nel CSS i nomi dei font vanno sempre tra virgolette: un nome che inizia con una cifra senza virgolette è ignorato dal browser.</p>')
    ex=[(True,f'<div style="font-size:24px;line-height:1.1">Una holding,<br>quattro fuochi.</div><div class="it" style="font-size:11px;margin-top:10px;color:{MUTED_L}">Occhiello in corsivo</div>','Gerarchia con corpo e corsivo'),
        (False,'<div style="font-size:24px;line-height:1.1;font-weight:900;-webkit-text-stroke:.8px #000">Una holding,<br>quattro fuochi.</div>','Grassetto sintetico'),
        (True,f'<div style="font-family:\'3blaze Display\';font-size:40px;line-height:.9">2027<span style="color:{OR}">.</span></div>','Display: un numero o 4 parole'),
        (False,'<div style="font-family:\'3blaze Display\';font-size:13px;line-height:1.3">Il Display usato per un paragrafo di testo corrente diventa illeggibile.</div>','Display per il testo corrente'),
        (True,'<div style="font-size:10px;line-height:1.6;text-align:left">Strategia, contenuti e design lavorano come un unico sistema, sullo schermo e nel mondo fisico.</div>','Testo a bandiera'),
        (False,'<div style="font-size:10px;line-height:1.6;text-align:justify;letter-spacing:.12em">Strategia, contenuti e design lavorano come un unico sistema, sullo schermo e nel mondo fisico.</div>','Giustificato e spaziato')]
    for i,(ok,inner,lab) in enumerate(ex):
        x=420+(i%2)*332; y=88+(i//2)*208
        b+=f'<div class="box" style="left:{x}px;top:{y}px;width:322px;height:170px;background:#F2E8CC"><div style="position:absolute;left:24px;top:30px;width:270px">{inner}</div></div><div class="{"do" if ok else "dont"} mono abs" style="left:{x}px;top:{y+178}px;color:{MUTED_L}">{lab}</div>'
    d.add(b, sec=4)
