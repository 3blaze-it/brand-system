from lib import *
from p1 import divider, DIV_WORDS
from p3 import stage, glass, btn, circ
IMG=B+'/guide/img/'; P=B+'/out/print/'; E=B+'/out/extra/'; S=B+'/out/scene/'

def img(x,y,w,h,src,fit='cover',pos='center',r=0,bg='transparent',shadow=False):
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg} url(\'{src}\') {pos}/{fit} no-repeat;'
            f'border-radius:0 0 {r}px {r}px;{"box-shadow:0 18px 40px -18px #0007, 0 0 0 .5px #0000001A;" if shadow else ""}"></div>')

def spec(x,y,w,rows_):
    t='<table class="tbl"><tr><th>Elemento</th><th>Specifica</th></tr>'+''.join(f'<tr><td style="width:34%">{a}</td><td>{b}</td></tr>' for a,b in rows_)+'</table>'
    return f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px">{t}</div>'

def ch6(d):
    divider(d,'06','Elementi grafici','La scena Prisma, il motivo spigoli/curve, le griglie di impaginazione, l\'iconografia e la direzione fotografica.',6)
    b = text_col('6.1','La scena Prisma · Trama Vetro','<p>È lo sfondo-firma del gruppo. La parola <b>3blaze</b> è fatta di vetro scuro, fuori scala, ruotata di 28° e ripetuta in righe che si incastrano, su Nero. Come negli sfondi Apple la scritta non si dichiara: la si scopre. Le lettere sono così grandi che restano solo frammenti.</p><p>I colori del brand vivono <b>solo sul filo dei bordi</b>, come dispersione del vetro: Brace, rosa vinaccia, Crema e Petrolio sfumano lentamente da una zona all\'altra. Il corpo del vetro resta quasi nero.</p><p>Sopra la trama vive un solo oggetto di vetro funzionale (le tre fiamme, un pannello con il marchio, i controlli di un\'interfaccia), che la rifrange. La trama non sostituisce mai il marchio: dove compare, il marchio pieno c\'è una volta. Si usa solo su Nero, mai sul tema Crema. File pronti in out/trama (16:9, 9:16, 1:1, A4).</p>')
    b += stage(420,88,655,620,size=104)
    b += glass(420+77,88+230,500,190,shape='symbol',bezel=30,scale=80,variant='clear')
    b += f'<div class="mono abs" style="left:436px;top:672px;font-size:6.4px;color:{MUTED_D}">Trama Vetro · 3blaze in vetro, ruotato 28°, righe incastrate · colori solo sui bordi · tre fiamme di vetro</div>'
    d.add(b, sec=6)
    b = text_col('6.2','Griglie e motivo','<p><b>Stampa A4</b>: 12 colonne su 170 mm, margini 20 mm laterali e 17 mm in testa, canale 4 mm. <b>Schermo</b>: 12 colonne con margine 96 px e canale 32 px su desktop; 4 colonne con margine 24 px su mobile.</p><p><b>Spigoli in alto, curve in basso</b>: card, immagini, etichette e campioni colore hanno angoli vivi in alto e raggio pieno solo in basso. È il motivo che rende riconoscibile un layout 3blaze anche senza marchio.</p>')
    cols=''.join(f'<div style="position:absolute;left:{20+i*(27.6+4)}px;top:0;width:27.6px;height:100%;background:#FB4F311A"></div>' for i in range(12))
    b += f'<div class="abs" style="left:420px;top:88px;width:300px;height:424px;background:#FFFFFF;box-shadow:0 0 0 .5px #0002"><div style="position:absolute;left:0;right:0;top:17px;bottom:14px">{cols}</div><div style="position:absolute;left:20px;top:17px;width:62px">{logo("3blaze_logo_horizontal")}</div><div style="position:absolute;left:20px;top:80px;width:200px;height:6px;background:#0002"></div><div style="position:absolute;left:20px;top:94px;width:170px;height:6px;background:#0002"></div></div>'
    b += cap(420,522,'A4 · 12 colonne · margini 20/17 mm · canale 4 mm')
    for i,(r,lab) in enumerate([(0,'Rettangolo: no'),(22,'Spigoli in alto, curve in basso: sì')]):
        x=755+i*165
        b+=f'<div class="abs" style="left:{x}px;top:88px;width:150px;height:200px;background:{BLACK};border-radius:0 0 {r}px {r}px"></div>'
        b+=f'<div class="{"dont" if i==0 else "do"} mono abs" style="left:{x}px;top:298px;color:{MUTED_L}">{lab}</div>'
    b += f'<div class="abs" style="left:755px;top:330px;display:flex;gap:10px"><span class="mono" style="font-size:7px;padding:6px 10px 7px;border-radius:0 0 10px 10px;background:{OR};color:#000">academy</span><span class="mono" style="font-size:7px;padding:6px 10px 7px;border-radius:0 0 10px 10px;background:{TEAL};color:{CREAM}">.net · live</span><span class="mono" style="font-size:7px;padding:6px 10px 7px;border-radius:0 0 10px 10px;background:{WINE};color:{CREAM}">luisa</span></div>'
    b += cap(755,362,'Etichette di divisione: linguette appese al bordo superiore')
    b += spec(755,400,320,[('Raggio card','20 px · 6 mm'),('Raggio immagini','32 px · 8 mm'),('Raggio etichette','10–12 px · 3 mm'),('Filetti','1 px · 0,25 pt al 12%')])
    d.add(b, sec=6)
    b = text_col('6.3','Iconografia','<p>Icone lineari su griglia 24 px, tratto 1,7 px, terminali squadrati e angoli vivi: lo stesso linguaggio delle sommità della fiamma. Nelle app Apple si usano i SF Symbols di sistema con peso Medium, che restano coerenti.</p><p>Le icone sono monocromatiche (Crema o Nero), mai colorate e mai in cerchi colorati. La fiamma singola sostituisce il punto elenco nelle liste di brand.</p>')
    names=list(ICONS.keys())
    for i,n in enumerate(names):
        x=420+(i%6)*110; y=88+(i//6)*110
        b+=f'<div class="box" style="left:{x}px;top:{y}px;width:100px;height:100px;background:#F2E8CC;border-radius:0 0 18px 18px"><div style="position:absolute;left:34px;top:26px">{icon(n,32,BLACK,1.6)}</div><div class="mono" style="position:absolute;left:0;right:0;bottom:10px;text-align:center;font-size:5.8px;color:{MUTED_L}">{n}</div></div>'
    d.add(b, sec=6)
    b = text_col('6.4','Fotografia','<p>Luce vera, neri profondi, contrasto alto: le immagini devono reggere il fondo Nero. Persone al lavoro, mani, set, aule, campi da gioco; mai foto di repertorio in posa.</p><p>Tagli decisi e soggetto decentrato per lasciare spazio al livello funzionale (titoli, controlli in vetro). Nessun filtro colorato di divisione sopra le immagini: il colore sta intorno, non sopra.</p><p>Quando un\'immagine è un riquadro, prende la base arrotondata del motivo.</p>')
    shots=[('Backstage di produzione','Luce di set, persone al lavoro, nessuna posa'),('Aula academy','Mani, schermi, lavagne: il gesto di imparare'),('Matchday .net','Movimento, grana, notte, colore della città'),('Ritratto','Fondo scuro, luce laterale, sguardo fuori campo')]
    for i,(t,s_) in enumerate(shots):
        x=420+(i%2)*332; y=88+(i//2)*312
        b+=f'<div class="box" style="left:{x}px;top:{y}px;width:322px;height:250px;border-radius:0 0 32px 32px;background:#1A1A1A"><div style="position:absolute;inset:0;background:repeating-linear-gradient(135deg,#ffffff07 0 2px,transparent 2px 14px)"></div><div class="mono" style="position:absolute;left:18px;top:16px;font-size:6.4px;color:{MUTED_D}">Area immagine</div><div style="position:absolute;left:18px;bottom:44px;font-size:15px;color:{CREAM}">{t}</div><div style="position:absolute;left:18px;bottom:22px;font-size:9px;font-style:italic;color:{MUTED_D}">{s_}</div></div>'
    b+=cap(420,690,'Schema di direzione fotografica — sostituire con lo scatto reale')
    d.add(b, sec=6)

def ch7(d):
    divider(d,'07','Applicazioni','Cancelleria, presentazioni, badge, insegne, affissioni, social e video. Tutti i file esecutivi sono nella cartella brand-2027.',7)
    b = text_col('7.1','Carta intestata','<p>Due versioni: <b>bianco</b> per la stampa da ufficio e <b>crema</b> per i PDF digitali o la carta tinta. La seconda pagina riduce l\'intestazione al simbolo.</p><p>Il testo si compone in 3blaze Sans 10/16 pt (in Word: Futura o Century Gothic 10/15 pt).</p>')
    b += img(420,88,300,424,IMG+'lh_1.jpg',shadow=True)
    b += spec(745,88,330,[('Formato','A4 · 210 × 297 mm'),('Logo','Orizzontale nero, 52 mm, a 20/17 mm'),('Intestazione','Mono 6,6 pt, allineata a destra'),('Testo','Sans 10/16 pt, margini 30 mm'),('Destinatario','A 125 mm dal bordo, per busta a finestra'),('Piede','Mono 5,9 pt su 4 colonne + fiamme divisioni'),('Segni','Piega 99 / 198 mm, foro 148,5 mm'),('Carta','Uncoated 100–120 g/m², bianca o crema')])
    b += cap(420,522,'File: stampati/carta_intestata_A4_bianco.pdf · _crema.pdf')
    d.add(b, sec=7)
    b = text_col('7.2','Biglietti da visita','<p>Fronte nel colore della divisione, retro comune con la scena Prisma e le tre fiamme di vetro. Il fronte di academy usa l\'inchiostro nero sulla Brace per garantire il contrasto dei testi piccoli.</p><p>Stampa consigliata: cartoncino uncoated 400–600 g/m²; per la holding, fronte a caldo Crema su cartoncino nero colorato in pasta.</p>')
    for i in range(5):
        x=420+(i%3)*222; y=88+(i//3)*170
        b+=img(x,y,210,141,IMG+f'bc_{i+1}.jpg',shadow=True)
    b += spec(420,440,655,[('Formato','85 × 55 mm + 3 mm di abbondanza per lato; area sicura 4 mm'),('Fronte','Simbolo 15 mm; nome Sans 10 pt; ruolo corsivo 7 pt; contatti mono 5,4 pt'),('Retro','Render Liquid Glass ad alta risoluzione + logotipo Crema 20 mm')])
    d.add(b, sec=7)
    b = text_col('7.3','Busta, cartellina, documenti','<p>La <b>busta DL</b> è bianca con finestra allineata al destinatario della carta intestata. La <b>cartellina</b> A4 è nera con il simbolo in Crema sul fronte e la scena Prisma all\'interno. La <b>copertina dei documenti</b> (offerte, report, piani) usa la scena con le tre fiamme di vetro nella metà superiore e il titolo in Sans 30 pt.</p>')
    b += img(420,88,330,165,P+'busta_DL_220x110.png',fit='contain',shadow=True,bg='#fff')
    b += img(420,276,210,296,IMG+'folder_1.jpg',shadow=True)
    b += img(640,276,210,296,IMG+'folder_2.jpg',shadow=True)
    b += img(870,88,205,290,E+'copertina_documento_A4.png',shadow=True)
    b += cap(420,582,'Busta DL 220 × 110 · cartellina A4 (fronte, interno) · copertina documento A4')
    d.add(b, sec=7)
    b = text_col('7.4','Firma email','<p>La firma è testo vivo, non un\'immagine: logo PNG @2x largo 132 px, nome in Sans 14 px, ruolo in corsivo, contatti in mono. I link al sito sono in Brace testo (#C93A20). Niente banner, citazioni o immagini di sfondo.</p><p>File: stampati/firma_email.html.</p>')
    b += f'''<div class="box" style="left:420px;top:88px;width:655px;height:330px;background:#FFFFFF;box-shadow:0 0 0 .5px #0002">
      <div style="position:absolute;left:0;right:0;top:0;height:34px;background:#F4F4F4;border-bottom:1px solid #E4E4E4"></div>
      <div style="position:absolute;left:32px;top:60px;font-size:11px;color:#333;font-family:Arial">Buongiorno,<br><br>in allegato la proposta per il piano 2027. Restiamo a disposizione.</div>
      <div style="position:absolute;left:32px;top:150px;width:132px">{logo('3blaze_logo_horizontal')}</div>
      <div style="position:absolute;left:32px;top:180px;font-size:14px">Nome Cognome</div>
      <div style="position:absolute;left:32px;top:200px;font-size:11px;font-style:italic;color:{MUTED_L}">Ruolo — 3blaze media</div>
      <div class="mono" style="position:absolute;left:32px;top:226px;font-size:8px;letter-spacing:.06em;color:{MUTED_L};text-transform:none">+39 000 000 0000 · nome@3blaze.it · <span style="color:{OR_INK}">3blaze.it</span></div>
      <div class="mono" style="position:absolute;left:32px;top:250px;font-size:7px;color:{MUTED_D}"><span style="color:#000">■</span> media &nbsp;<span style="color:{OR}">■</span> academy &nbsp;<span style="color:{TEAL}">■</span> news &nbsp;<span style="color:{WINE}">■</span> ia</div></div>'''
    b += spec(420,440,655,[('Logo','PNG @2x, 132 × 21 px, ospitato su 3blaze.it/brand'),('Font','3blaze Sans con alternative Futura, Century Gothic, Arial'),('Colori','Testo nero, secondario #6B665C, link #C93A20'),('Divieti','Immagini di sfondo, banner promozionali, citazioni, più di 6 righe')])
    d.add(b, sec=7)
    b = text_col('7.5','Presentazioni','<p>Il modello PowerPoint 16:9 contiene i layout del sistema: copertina con pannello di vetro, divisore di sezione con le tre fiamme di vetro, contenuto su Crema e su Nero, manifesto su Brace, chiusura. Si compila con i segnaposto: titoli, numeri di sezione e piè di pagina sono già nei layout.</p><p>File: presentazioni/3blaze_modello_presentazione_2027.pptx (installare prima i font del brand).</p>')
    for i,k in enumerate([1,3,4,5,6,7,8,10,13]):
        x=420+(i%3)*222; y=88+(i//3)*132
        b+=img(x,y,210,118,IMG+f'slide-{k:02d}.jpg',shadow=True)
    b += cap(420,490,'Copertina · divisore · divisioni · numeri · frase chiave · processo · vetro/contenuto · marchio · chiusura con claim')
    b += spec(420,520,655,[('Formato','16:9 · 33,87 × 19,05 cm (13,33 × 7,5 in)'),('Titoli','3blaze Sans 32 pt; divisori: numero in Display 150 pt'),('Testo','3blaze Sans 16–18 pt, mai sotto 14 pt'),('Layout','BZ_COPERTINA · BZ_DIVISORE · BZ_CONTENUTO · BZ_CONTENUTO_TESTO · BZ_CONTENUTO_NERO · BZ_MANIFESTO · BZ_CHIUSURA')])
    d.add(b, sec=7)
    b = text_col('7.6','Badge e accrediti','<p><b>Badge evento</b> 90 × 130 mm con asola per lanyard: il ruolo è scritto in Display su una fascia colorata con base arrotondata, il colore segue la divisione o la funzione (staff, speaker, ospite, stampa, luisa lab).</p><p><b>Badge dipendente</b> in formato carta CR80 con foto a base arrotondata. <b>Lanyard</b> 20 mm nero con simbolo Crema e logotipo Brace alternati.</p>')
    for i in range(5):
        b+=img(420+i*112,88,104,150,IMG+f'badge_{i+1}.jpg',shadow=True)
    b += img(420,262,104,150,IMG+'badge_6.jpg',shadow=True)
    b += img(540,262,95,150,IMG+'cr80_1.jpg',shadow=True)
    b += img(645,262,95,150,IMG+'cr80_2.jpg',shadow=True)
    b += f'<div class="abs" style="left:760px;top:262px;width:315px;height:40px;overflow:hidden;border-radius:0 0 8px 8px"><div style="width:40px;height:315px;transform:rotate(-90deg) translate(-315px,0);transform-origin:0 0;background:url(\'{E}lanyard_20x900mm.png\') top/100% auto"></div></div>'
    b += cap(760,312,'Lanyard 20 mm')
    b += spec(420,440,655,[('Badge evento','90 × 130 mm · asola 16 × 3,4 mm · nome Sans 21 pt · ruolo Display 25 pt'),('Badge dipendente','CR80 54 × 85,6 mm · foto 30 × 38 mm a base arrotondata · validità in mono'),('Lanyard','20 × 900 mm · fondo Nero · stampa a sublimazione'),('Colori ruolo','Staff Nero · Speaker Brace · Ospite Crema · Stampa Petrolio · Lab Vinaccia')])
    d.add(b, sec=7)
    b = text_col('7.7','Affissione e roll-up','<p>Affissione 6 × 3 m: le tre fiamme di vetro sulla scena occupano il formato; il marchio con il claim firma in basso a sinistra, il sito in basso a destra. Nessun titolo: il segno è il messaggio. Per le campagne di divisione si aggiunge un solo messaggio breve in 3blaze Sans.</p><p>Roll-up 85 × 200 cm: marchio con claim sempre sopra i 160 cm, scena con le tre fiamme, marchi delle divisioni, sito; fascia Brace di 8 cm a terra senza contenuti.</p>')
    b += img(420,88,470,235,P+'affissione_6x3m_scala1-10.png',shadow=True)
    b += img(905,88,170,400,P+'rollup_85x200cm_scala1-4.png',shadow=True)
    b += img(420,340,470,148,S+'prisma_hero.png',shadow=True)
    b += cap(420,500,'Affissione 6 × 3 m (file in scala 1:10) · roll-up 85 × 200 cm (1:4) · banner orizzontale da scena Prisma')
    d.add(b, sec=7)
    b = text_col('7.8','Insegne e segnaletica','<p>La <b>targa d\'ingresso</b> è in plexiglass nero lucido 8 mm con stampa UV Crema e distanziali in acciaio. L\'<b>insegna a cassonetto</b> è nera opaca con lettere retroilluminate a 3000 K, perché il Crema resti caldo di notte.</p><p>La <b>segnaletica interna</b> usa pannelli neri con numerazione mono, nome dell\'ambiente in Sans, freccia e una fascia nel colore della divisione che occupa lo spazio.</p>')
    b += img(420,88,320,160,P+'targa_ingresso_400x200mm.png',shadow=True)
    b += img(755,88,320,64,P+'insegna_cassonetto_300x60cm_scala1-10.png',shadow=True)
    for i,k in enumerate([1,2,3]):
        b+=img(755,168+i*72,320,107*0.6,IMG+f'wf_{k}.jpg',fit='cover',shadow=True)
    b += spec(420,400,655,[('Targa','400 × 200 mm · plexi nero 8 mm · stampa UV o incisione laccata'),('Insegna','300 × 60 cm · lettere scatolate retroilluminate 3000 K · fondo RAL 9005 opaco'),('Segnaletica','300 × 100 mm · alluminio composito nero · fascia divisione 8 mm'),('Altezze','Targhe a 160 cm dal suolo (asse) · insegne secondo regolamento comunale')])
    d.add(b, sec=7)
    b = text_col('7.9','Social media','<p>Avatar: simbolo (o logotipo luisa) centrato su fondo di divisione, con area di rispetto per il ritaglio circolare. Cover: scena Prisma con pannello di vetro nel terzo destro, perché a sinistra c\'è la foto profilo. Post 4:5: scena con le tre fiamme di vetro e marchio con claim in basso.</p><p>Nelle storie restano liberi 250 px in alto e 340 px in basso per l\'interfaccia della piattaforma.</p>')
    for i,k in enumerate(['3blaze','academy','net','luisa']):
        b+=f'<div class="abs" style="left:{420+i*86}px;top:88px;width:74px;height:74px;border-radius:50%;background:url(\'{E}avatar/avatar_{k}_1080.png\') center/cover"></div>'
    b += img(420,180,330,83,P+'social_linkedin_cover_1584x396.png',shadow=True)
    b += img(420,280,330,180,S+'slide_closing.png',shadow=True)
    b += img(775,88,300,375,P+'social_post_1080x1350.png',shadow=True)
    b += spec(420,490,655,[('Avatar','1080 × 1080 · simbolo al 62% della larghezza'),('Cover LinkedIn','1584 × 396 · vetro nel terzo destro'),('Post','1080 × 1350 · tre fiamme di vetro + marchio con claim'),('Story / Reel','1080 × 1920 · aree sicure 250 / 340 px')])
    d.add(b, sec=7)
    b = text_col('7.10','Video e videochiamate','<p><b>Sottopancia</b>: linguetta Brace a base arrotondata + nome in Sans e ruolo in corsivo su fondo Nero al 90%. <b>Bug</b>: logo Crema in alto a destra al 90%. <b>Chiusura</b>: scena Prisma con pannello di vetro, il claim Ignite Beyond. e il sito.</p><p><b>Sfondi per videochiamate</b> (Meet, Teams, Zoom) 1920 × 1080 in cinque versioni: quattro divisioni e la scena Prisma. Il marchio è in alto a destra perché la persona occupa il centro.</p>')
    b += f'<div class="abs" style="left:420px;top:88px;width:400px;height:225px;background:url(\'{S}prisma_hero.png\') center/cover;border-radius:0 0 20px 20px;overflow:hidden"><div style="position:absolute;inset:0;background:url(\'{E}video_lower_third_1920x1080.png\') center/cover"></div></div>'
    b += img(835,88,240,135,E+'video_end_card_1920x1080.png',shadow=True)
    for i,k in enumerate(['media','academy','news','ia','prisma']):
        b+=img(420+i*133,340,123,69,E+f'sfondo_call_{k}_1920x1080.png',shadow=True)
    b += cap(420,420,'Sfondi call: media · academy · news · ia · prisma')
    b += spec(420,450,655,[('Sottopancia','Linguetta Brace 28 px · nome Sans 44 px · ruolo corsivo 24 px (su 1920 × 1080)'),('Durata','Entrata 280 ms, permanenza minima 4 s'),('Chiusura','3 s · scena Prisma · claim · sito in mono'),('Sfondi call','PNG 1920 × 1080 · marchio in alto a destra')])
    d.add(b, sec=7)

def ch8(d):
    divider(d,'08','Voce','Come parla 3blaze: diretta, concreta, calda. Il claim Ignite Beyond e le regole di scrittura.',8)
    b = text_col('8.1','Tono di voce','<p>Il gruppo parla come una persona competente che non ha bisogno di alzare la voce.</p>')
    T=[('Diretta','Frasi brevi, verbi attivi, la cosa importante per prima.','"Consegniamo in tre settimane."','"Siamo in grado di garantire tempistiche rapide."'),
       ('Concreta','Numeri, tempi, nomi. Niente aggettivi vuoti.','"6 posti, 12 marzo, Terni."','"Un\'esperienza formativa unica."'),
       ('Calda','Il fuoco scalda prima di bruciare: niente urla.','"Ti aspettiamo in aula."','"Non perdere questa occasione!!!"'),
       ('Tecnica quando serve','I dati si mostrano in mono, ordinati.','"CPM −18% · CTR 2,4%"','"Risultati incredibili."')]
    for i,(t,s_,ok,ko) in enumerate(T):
        x=420+(i%2)*332; y=88+(i//2)*300
        b+=f'<div class="box" style="left:{x}px;top:{y}px;width:322px;height:270px;background:#F2E8CC"><div style="position:absolute;left:22px;top:18px;width:290px;font-family:\'3blaze Display\';font-size:{30 if len(t)<12 else 21}px;line-height:1;color:{OR}">{t.upper()}</div><div class="p" style="position:absolute;left:22px;top:66px;width:270px">{s_}</div><div class="do mono" style="position:absolute;left:22px;top:122px;color:{MUTED_L}">Sì</div><div class="it" style="position:absolute;left:22px;top:140px;width:270px;font-size:13px">{ok}</div><div class="dont mono" style="position:absolute;left:22px;top:192px;color:{MUTED_L}">No</div><div class="it" style="position:absolute;left:22px;top:210px;width:270px;font-size:13px;color:{MUTED_L};text-decoration:line-through">{ko}</div></div>'
    d.add(b, sec=8)
    b = text_col('8.2','Il claim: Ignite Beyond','<p><b>Ignite Beyond.</b> — accendi l\'oltre. Dice cosa fa il gruppo per chi lavora con lui: accendere un\'idea e portarla più in là di dove sarebbe arrivata da sola.</p><p>Il claim non è il protagonista. Come una firma, si legge per ultimo: sotto il marchio, in fondo a un video, in chiusura di una presentazione. Parla piano e resta.</p><p>Si scrive sempre in inglese, in 3blaze Sans Italic, con il punto finale. La traduzione italiana serve solo a spiegarlo, mai accanto al claim.</p>')
    b += f'<div class="box" style="left:420px;top:88px;width:655px;height:300px;background:{BLACK}">{rows(size=80,top=0,height=300,opacity=.12)}<div class="abs" style="left:228px;top:110px;width:200px">{logo("3blaze_logo_claim",CREAM)}</div></div>'
    b += cap(420,396,'Il claim vive accanto al marchio, mai al suo posto')
    R=[(True,'Firma sotto il marchio','<div style="width:150px;margin:70px auto 0">'+logo('3blaze_logo_claim',CREAM)+'</div>'),
       (True,'Chiusura di video e slide','<div style="width:120px;margin:84px auto 0">'+logo('3blaze_claim',CREAM)+'</div>'),
       (False,'Come titolo gigante','<div style="font-family:\'3blaze Display\';font-size:30px;line-height:.9;color:#FDF6E2;margin:56px 14px 0">IGNITE<br>BEYOND!</div>'),
       (False,'Tradotto o colorato','<div style="font-size:15px;font-style:italic;color:#FB4F31;margin:76px 14px 0">Accendi l\'oltre!</div>')]
    for i,(ok,lab,inner) in enumerate(R):
        x=420+i*166
        b+=f'<div class="box" style="left:{x}px;top:430px;width:154px;height:190px;background:{BLACK}">{inner}</div><div class="{"do" if ok else "dont"} mono abs" style="left:{x}px;top:628px;color:{MUTED_L}">{lab}</div>'
    d.add(b, sec=8)
    b = text_col('8.3','Regole di scrittura','<p>Il nome si scrive sempre minuscolo, anche a inizio frase: <b>3blaze</b>. Le divisioni: <b>3blaze academy</b>, <b>3blaze .net</b> (con lo spazio prima del punto), <b>luisa</b>. Nei testi legali: <b>3BLAZE S.R.L.S.</b></p><p>L\'italiano viene prima; l\'inglese solo per nomi propri e termini senza equivalente (reel, matchday).</p>')
    rows_=[('Scrivere','Non scrivere'),('3blaze','3Blaze · 3 Blaze · Treblaze · 3BLAZE (fuori dai testi legali)'),('3blaze .net','3blaze.net (è il dominio) · 3Blaze Net'),('luisa','Luisa · LUISA · L.U.I.S.A.'),('Ignite Beyond.','IGNITE BEYOND! · Ignite beyond · Accendi l\'oltre (nei materiali) · Make communication great again (ritirato)'),('Consegna in 3 settimane','Tempi rapidi'),('Costruiamo il sistema','Soluzioni innovative a 360 gradi'),('Ti spieghiamo come','Leader del settore · qualità garantita · eccellenza')]
    t='<table class="tbl" style="font-size:10px"><tr><th>Sì</th><th>No</th></tr>'+''.join(f'<tr><td>{a}</td><td style="color:{MUTED_L}">{c}</td></tr>' for a,c in rows_[1:])+'</table>'
    b += f'<div class="abs" style="left:420px;top:88px;width:655px">{t}</div>'
    d.add(b, sec=8)

def ch9(d):
    b = text_col('9.1','File del sistema','<p>Tutti gli esecutivi sono nella cartella <b>3blaze-nextgen/brand-2027</b>. Il manuale descrive le regole; i file sono la fonte. In caso di dubbio vale il file vettoriale.</p><p>Prima di andare in stampa: inserire P.IVA, PEC e telefono (oggi segnaposto), convertire i colori con lo stampatore, chiedere una prova colore della Brace.</p>')
    F=[('logo/svg','Tutti i marchi in SVG: nero, crema, colori di divisione, currentColor'),('logo/png','PNG @2x e ad alta risoluzione per Office e social'),('logo/3blaze_tavola_costruttiva.pdf','Tavola costruttiva A3'),('fonts','3blaze Sans, 3blaze Display, JetBrains Mono (woff2 / ttf)'),('codice','tokens.css · tokens.json · DTCG · liquid-glass.js / .css · componenti'),('stampati','Carta intestata, biglietti, busta, firma email'),('presentazioni','Modello PowerPoint 16:9'),('badge-eventi','Badge evento, badge dipendente, lanyard'),('cartellonistica','Affissione, roll-up, targa, insegna, segnaletica interna'),('social · video · call','Avatar, cover, post, sottopancia, chiusura, sfondi videochiamata'),('icone','Favicon e icone app per divisione (16–1024 px, ICO, SVG)'),('manuale','Questo documento (PDF) e la versione testuale per le IA')]
    t='<table class="tbl"><tr><th>Cartella</th><th>Contenuto</th></tr>'+''.join(f'<tr><td class="mono" style="font-size:7px;text-transform:none;letter-spacing:.04em">{a}</td><td>{c}</td></tr>' for a,c in F)+'</table>'
    b += f'<div class="abs" style="left:420px;top:88px;width:655px">{t}</div>'
    d.add(b, sec=9)
    b = text_col('9.2','Checklist e lettura automatica','<p>Il sistema è descritto anche in forma leggibile dalle intelligenze artificiali (BRAND_GUIDELINES_3blaze_2027.md e tokens.json): agenti di sviluppo, generatori di immagini e assistenti di scrittura devono leggerli prima di produrre materiali 3blaze.</p><p>Il logo non va mai generato da un\'IA: si sovrappone dopo, dai file ufficiali.</p>')
    chk=['Il marchio è un file ufficiale, non ritoccato, con area di rispetto e sopra la misura minima?','Un solo colore di divisione domina e la Brace resta sotto il 10%?','Ogni testo ha contrasto ≥ 4,5:1 (≥ 3:1 da 24 px)?','Il Display è usato solo da 48 px e per massimo 4 parole?','Il vetro è vero (o un render), appartiene al livello funzionale, è uno solo per vista?','Nessun vetro su vetro, nessun vetro su fondo piatto?','Il copy evita le parole bandite e scrive 3blaze minuscolo?','Il claim Ignite Beyond. compare al massimo una volta, come firma e mai come titolo?','I dati societari segnaposto sono stati sostituiti?']
    b += ''.join(f'<div class="abs" style="left:420px;top:{88+i*40}px;width:655px;display:flex;gap:14px;align-items:flex-start"><div style="width:16px;height:16px;border:1px solid #000;border-radius:0 0 8px 8px;flex:none;margin-top:1px"></div><div style="font-size:11.5px;line-height:1.4">{c}</div></div>' for i,c in enumerate(chk))
    yaml='brand: 3blaze\nfonts: {primary: "3blaze Sans", display: "3blaze Display ≥48px", mono: "JetBrains Mono"}\ncolors: {nero: "#000000", crema: "#FDF6E2", academy: "#FB4F31", news: "#006172", ia: "#4D1821"}\nglass: {layer: functional, variants: [regular, clear, tinted], shape: capsule, concentric: true}\nmotif: "spigoli in alto, curve in basso"\nclaim: {text: "Ignite Beyond.", role: firma, font: "3blaze Sans Italic", never: [titolo, Display, maiuscolo, traduzione]}'
    b += f'<div class="box" style="left:420px;top:460px;width:655px;height:150px;background:#0E0E0E"><pre style="position:absolute;left:20px;top:18px;font-family:JetBrains Mono;font-weight:400;font-size:8.4px;line-height:1.7;color:#E8E1CF;white-space:pre">{yaml}</pre></div>'
    d.add(b, sec=9)

def back(d):
    b = rows(size=118,top=0,height=H)
    b += glass(W/2-230,H/2-90,460,180,r=44,variant='regular',bezel=44,scale=80,inner=f'<div style="width:330px">{logo("3blaze_logo_horizontal",CREAM)}</div>')
    b += f'<div class="abs" style="left:{W/2-70}px;top:{H/2+110}px;width:140px">{logo("3blaze_claim",CREAM)}</div>'
    b += f'<div class="mono abs" style="left:0;right:0;bottom:34px;text-align:center;font-size:7px;color:{CREAM};text-transform:none;letter-spacing:.12em"><span style="background:#000C;padding:6px 14px;border-radius:99px">3BLAZE S.R.L.S. · Strada Valle Verde 6, 05100 Terni · ciao@3blaze.it · 3blaze.it</span></div>'
    d.add(b, dark=True, chrome=False)
