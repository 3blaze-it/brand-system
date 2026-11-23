const pptxgen = require('pptxgenjs');
const { applyTheme } = require('/root/.claude/skills/synced/ce672295-89af-4c1a-948d-ce383954a10b_8b93c3b0-d51a-498b-a609-146f52500385/pptx/scripts/apply_theme.js');
const S = '/home/claude/brand/out/scene/', LG = '/home/claude/brand/out/logo/png/';
const THEME = { name: '3blaze 2027', headFontFace: '3blaze Sans', bodyFontFace: '3blaze Sans',
  colors: { dk1: '000000', lt1: 'FDF6E2', dk2: '1A1A1A', lt2: 'EDE3C6', accent1: 'FB4F31', accent2: '006172', accent3: '4D1821',
            accent4: '3FA9BA', accent5: 'D98C99', accent6: 'A8A294', hlink: 'C93A20', folHlink: '6B665C' } };
const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE'; pres.author = '3blaze'; pres.company = '3BLAZE S.R.L.S.'; pres.title = '3blaze — Modello presentazione 2027';
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
const C = pres.SchemeColor;
const MONO = 'JetBrains Mono';
const foot = (dark) => ([
  { image: { x: 0.6, y: 6.92, w: 0.62, h: 0.236, path: LG + (dark ? '3blaze_symbol_cream_hi.png' : '3blaze_symbol_black_hi.png') } },
  { text: { text: '3BLAZE · 2027', options: { x: 1.4, y: 6.86, w: 4, h: 0.34, fontFace: MONO, fontSize: 9, charSpacing: 2, color: dark ? 'A8A294' : '6B665C', margin: 0, valign: 'middle' } } },
]);
const num = (dark) => ({ x: 11.73, y: 6.86, w: 1, h: 0.34, fontFace: MONO, fontSize: 9, color: dark ? 'A8A294' : '6B665C', align: 'right', valign: 'middle' });

pres.defineSlideMaster({ title: 'BZ_COPERTINA', background: { path: S + 'slide_cover.png' },
  objects: [ { image: { x: 0.95, y: 4.25, w: 2.8, h: 0.445, path: LG + '3blaze_logo_horizontal_cream_hi.png' } },
    { placeholder: { options: { name: 'title', type: 'title', x: 0.95, y: 4.95, w: 7.2, h: 0.95, fontSize: 36, color: C.background1, valign: 'top', align: 'left', margin: 0 }, text: 'Titolo della presentazione' } },
    { placeholder: { options: { name: 'body', type: 'body', x: 0.95, y: 6.0, w: 7.2, h: 0.4, fontSize: 14, align: 'left', italic: true, color: 'C9C2B0', margin: 0 }, text: 'Sottotitolo · data' } } ] });
pres.defineSlideMaster({ title: 'BZ_DIVISORE', background: { path: S + 'slide_section.png' },
  objects: [ { placeholder: { options: { name: 'number', type: 'body', x: 0.85, y: 1.3, w: 6, h: 2.2, fontFace: '3blaze Display', fontSize: 150, color: C.accent1, margin: 0, valign: 'top' }, text: '01' } },
    { placeholder: { options: { name: 'title', type: 'title', x: 0.85, y: 4.1, w: 6.8, h: 1.7, fontSize: 40, color: C.background1, valign: 'top', align: 'left', margin: 0 }, text: 'Titolo della sezione' } },
    ...foot(true) ], slideNumber: num(true) });
pres.defineSlideMaster({ title: 'BZ_CONTENUTO', background: { color: C.background1 },
  objects: [ { placeholder: { options: { name: 'title', type: 'title', x: 0.6, y: 0.75, w: 11.6, h: 0.95, fontSize: 32, color: C.text1, valign: 'top', align: 'left', margin: 0 }, text: 'Titolo della slide' } },
    ...foot(false) ], slideNumber: num(false) });
pres.defineSlideMaster({ title: 'BZ_CONTENUTO_TESTO', background: { color: C.background1 },
  objects: [ { placeholder: { options: { name: 'title', type: 'title', x: 0.6, y: 0.75, w: 6.3, h: 0.95, fontSize: 32, color: C.text1, valign: 'top', align: 'left', margin: 0 }, text: 'Titolo della slide' } },
    { placeholder: { options: { name: 'body', type: 'body', x: 0.6, y: 2.45, w: 6.2, h: 4.0, fontSize: 18, color: C.text1, valign: 'top', align: 'left', margin: 0, paraSpaceAfter: 12 }, text: 'Testo' } },
    ...foot(false) ], slideNumber: num(false) });
pres.defineSlideMaster({ title: 'BZ_CONTENUTO_NERO', background: { color: C.text1 },
  objects: [ { placeholder: { options: { name: 'title', type: 'title', x: 0.6, y: 0.75, w: 11.6, h: 0.95, fontSize: 32, color: C.background1, valign: 'top', align: 'left', margin: 0 }, text: 'Titolo della slide' } },
    ...foot(true) ], slideNumber: num(true) });
pres.defineSlideMaster({ title: 'BZ_MANIFESTO', background: { color: C.accent1 },
  objects: [ { placeholder: { options: { name: 'body', type: 'body', x: 0.85, y: 1.6, w: 11.4, h: 3.6, fontSize: 44, color: C.text1, valign: 'top', align: 'left', margin: 0 }, text: 'Una frase che conta' } },
    { placeholder: { options: { name: 'caption', type: 'body', x: 0.85, y: 5.6, w: 8, h: 0.6, fontSize: 16, italic: true, align: 'left', color: C.text1, margin: 0 }, text: 'Firma o contesto' } },
    { image: { x: 0.6, y: 6.92, w: 0.62, h: 0.236, path: LG + '3blaze_symbol_black_hi.png' } } ], slideNumber: { ...num(false), color: '000000' } });
pres.defineSlideMaster({ title: 'BZ_CHIUSURA', background: { path: S + 'slide_closing.png' },
  objects: [ { image: { x: 5.67, y: 5.55, w: 2.0, h: 0.268, path: LG + '3blaze_claim_cream_hi.png' } },
    { placeholder: { options: { name: 'body', type: 'body', x: 2.0, y: 6.45, w: 9.33, h: 0.5, fontFace: MONO, fontSize: 12, charSpacing: 2, color: 'FDF6E2', align: 'center', margin: 0 }, text: 'ciao@3blaze.it · 3blaze.it' } } ] });

const SEC = (t) => pres.addSection({ title: t });
const label = (s, t, x, y, w, color) => s.addText(t, { x, y, w, h: 0.3, fontFace: MONO, fontSize: 10, charSpacing: 2, color, margin: 0, isTextBox: true });

// 1 copertina
SEC('Apertura');
let s = pres.addSlide({ masterName: 'BZ_COPERTINA', sectionTitle: 'Apertura' });
s.addText('Una holding, quattro fuochi', { placeholder: 'title' });
s.addText('Presentazione di gruppo · 2027', { placeholder: 'body' });
s.addNotes('Copertina: titolo massimo due righe, sottotitolo con contesto e data. Lo sfondo è il render della scena Prisma con pannello liquid glass.');

// 2 agenda
s = pres.addSlide({ masterName: 'BZ_CONTENUTO', sectionTitle: 'Apertura' });
s.addText('Di cosa parliamo', { placeholder: 'title' });
const ag = [['01', 'Chi siamo', 'Il gruppo e le sue divisioni'], ['02', 'Come lavoriamo', 'Metodo, tempi, strumenti'], ['03', 'Il marchio', 'Identità 2027'], ['04', 'Prossimi passi', 'Cosa ci serve da voi']];
ag.forEach((r, i) => { const y = 2.05 + i * 1.08;
  s.addShape(pres.shapes.LINE, { x: 0.6, y, w: 12.13, h: 0, line: { color: 'C9C2B0', width: 0.75 }, objectName: 'filetto ' + r[0] });
  s.addText(r[0], { x: 0.6, y: y + 0.18, w: 1.4, h: 0.7, fontFace: '3blaze Display', fontSize: 34, color: C.accent1, margin: 0, isTextBox: true, objectName: 'numero ' + r[0] });
  s.addText(r[1], { x: 2.2, y: y + 0.2, w: 5, h: 0.6, fontSize: 24, color: C.text1, margin: 0, isTextBox: true });
  s.addText(r[2], { x: 7.4, y: y + 0.26, w: 5.3, h: 0.5, fontSize: 16, italic: true, color: '6B665C', margin: 0, isTextBox: true }); });

// 3 divisore
SEC('Chi siamo');
s = pres.addSlide({ masterName: 'BZ_DIVISORE', sectionTitle: 'Chi siamo' });
s.addText('01', { placeholder: 'number' }); s.addText('Chi siamo', { placeholder: 'title' });

// 4 divisioni
s = pres.addSlide({ masterName: 'BZ_CONTENUTO', sectionTitle: 'Chi siamo' });
s.addText('Quattro divisioni, un solo sistema', { placeholder: 'title' });
const dv = [['3blaze', 'media', 'Strategia, contenuti, video e brand management.', '000000', 'FDF6E2'],
            ['3blaze academy', 'formazione', 'Corsi, workshop e percorsi per aziende e scuole.', 'FB4F31', '000000'],
            ['3blaze .net', 'news', 'Informazione, rubriche, matchday e territorio.', '006172', 'FDF6E2'],
            ['luisa', 'ia', "L'assistente IA proprietaria del gruppo.", '4D1821', 'FDF6E2']];
dv.forEach((d, i) => { const x = 0.6 + i * 3.08;
  s.addShape(pres.shapes.ROUND_2_SAME_RECTANGLE, { x, y: 2.0, w: 2.9, h: 4.4, fill: { color: d[3] }, flipV: true, rectRadius: 0.45, line: { type: 'none' }, objectName: 'card ' + d[0] });
  s.addText(d[1].toUpperCase(), { x: x + 0.3, y: 2.3, w: 2.4, h: 0.3, fontFace: MONO, fontSize: 9, charSpacing: 2, color: d[4], margin: 0, isTextBox: true });
  s.addText(d[0], { x: x + 0.3, y: 3.75, w: 2.5, h: 1.05, valign: 'bottom', fontSize: 20, fit: 'none', italic: true, color: d[4], margin: 0, isTextBox: true });
  s.addText(d[2], { x: x + 0.3, y: 4.95, w: 2.35, h: 1.2, fontSize: 13, color: d[4], margin: 0, valign: 'top', isTextBox: true }); });

// 5 numeri
s = pres.addSlide({ masterName: 'BZ_CONTENUTO_NERO', sectionTitle: 'Chi siamo' });
s.addText('I numeri che contano', { placeholder: 'title' });
[['00', 'Progetti consegnati nel 2026'], ['00', 'Persone formate in academy'], ['00', 'Articoli pubblicati su .net']].forEach((n, i) => { const x = 0.6 + i * 4.1;
  s.addText(n[0], { x, y: 2.3, w: 3.8, h: 2.0, fontFace: '3blaze Display', fontSize: 120, color: i === 0 ? C.accent1 : C.background1, margin: 0, isTextBox: true });
  s.addShape(pres.shapes.LINE, { x, y: 4.6, w: 3.6, h: 0, line: { color: '3A3A3A', width: 0.75 } });
  s.addText(n[1], { x, y: 4.75, w: 3.6, h: 0.9, fontSize: 16, color: 'A8A294', margin: 0, valign: 'top', isTextBox: true }); });
s.addNotes('Sostituire gli 00 con i dati reali. Un solo numero in Brace: il più importante.');

// 6 manifesto
SEC('Come lavoriamo');
s = pres.addSlide({ masterName: 'BZ_MANIFESTO', sectionTitle: 'Come lavoriamo' });
s.addText('Ogni progetto parte da una domanda: cosa rende un brand impossibile da confondere?', { placeholder: 'body' });
s.addText('Il metodo 3blaze', { placeholder: 'caption' });

// 7 processo
s = pres.addSlide({ masterName: 'BZ_CONTENUTO', sectionTitle: 'Come lavoriamo' });
s.addText('Tre fasi, tempi chiari', { placeholder: 'title' });
[['Diagnosi', 'Target, problema, differenziale. Una pagina, non un faldone.', 'SETTIMANA 1'],
 ['Concept', 'Un messaggio centrale e tre pilastri di contenuto.', 'SETTIMANA 2'],
 ['Produzione', 'Contenuti, sito, materiali fisici: un unico sistema.', 'SETTIMANE 3–6']].forEach((p, i) => { const x = 0.6 + i * 4.1;
  s.addShape(pres.shapes.OVAL, { x, y: 2.2, w: 0.7, h: 0.7, fill: { color: i === 0 ? 'FB4F31' : '000000' }, line: { type: 'none' } });
  s.addText(String(i + 1), { x, y: 2.2, w: 0.7, h: 0.7, fontSize: 18, color: i === 0 ? '000000' : 'FDF6E2', align: 'center', valign: 'middle', margin: 0, isTextBox: true });
  if (i < 2) s.addShape(pres.shapes.LINE, { x: x + 0.85, y: 2.55, w: 3.1, h: 0, line: { color: 'C9C2B0', width: 0.75, dashType: 'dash' } });
  label(s, p[2], x, 3.2, 3.6, '6B665C');
  s.addText(p[0], { x, y: 3.55, w: 3.6, h: 0.6, fontSize: 26, color: C.text1, margin: 0, isTextBox: true });
  s.addText(p[1], { x, y: 4.25, w: 3.5, h: 1.2, fontSize: 16, color: '3A3A3A', margin: 0, valign: 'top', isTextBox: true }); });

// 8 immagine + testo
s = pres.addSlide({ masterName: 'BZ_CONTENUTO_TESTO', sectionTitle: 'Come lavoriamo' });
s.addText('Il vetro sta sopra, il contenuto sotto', { placeholder: 'title' });
s.addText([{ text: 'Il liquid glass si usa per ciò che si tocca: bottoni, barre, finestre.', options: { breakLine: true } },
           { text: 'Le immagini e i testi restano il livello di contenuto, a tutta superficie.', options: { breakLine: true } },
           { text: 'Una sola superficie di vetro per vista, mai vetro su vetro.' }], { placeholder: 'body' });
s.addImage({ path: S + 'prisma_flame.png', x: 7.4, y: 0.75, w: 5.33, h: 5.85, sizing: { type: 'cover', w: 5.33, h: 5.85 }, altText: 'Fiamma di vetro sulla scena Prisma' });

// 9 marchio
SEC('Il marchio');
s = pres.addSlide({ masterName: 'BZ_DIVISORE', sectionTitle: 'Il marchio' });
s.addText('03', { placeholder: 'number' }); s.addText('Il marchio', { placeholder: 'title' });
s = pres.addSlide({ masterName: 'BZ_CONTENUTO_NERO', sectionTitle: 'Il marchio' });
s.addText('Spigoli in alto, curve in basso', { placeholder: 'title' });
s.addImage({ path: LG + '3blaze_logo_horizontal_cream_hi.png', x: 0.6, y: 3.2, w: 7.2, h: 1.157, altText: 'Logo 3blaze' });
s.addText([{ text: 'Fiamma 24 × 35 moduli, angoli 45° e 60°.', options: { breakLine: true } }, { text: 'Altezza fiamma = maiuscole del 3blaze Sans.', options: { breakLine: true } }, { text: 'Area di rispetto: una fiamma.' }],
  { x: 8.6, y: 3.0, w: 4.1, h: 2.2, fontSize: 16, color: 'A8A294', margin: 0, valign: 'top', paraSpaceAfter: 10, isTextBox: true });

// 10 citazione
SEC('Chiusura');
s = pres.addSlide({ masterName: 'BZ_CONTENUTO_NERO', sectionTitle: 'Chiusura' });
s.addText('', { placeholder: 'title' });
s.addText('“Un brand si riconosce prima che si legga.”', { x: 0.6, y: 2.2, w: 11.5, h: 2.4, fontSize: 44, italic: true, color: C.background1, margin: 0, valign: 'top', isTextBox: true });
label(s, 'NOME COGNOME — RUOLO, 3BLAZE', 0.6, 4.9, 8, 'FB4F31');

// 11 prossimi passi
s = pres.addSlide({ masterName: 'BZ_CONTENUTO', sectionTitle: 'Chiusura' });
s.addText('Prossimi passi', { placeholder: 'title' });
[['Entro venerdì', 'Conferma del brief e dei referenti'], ['Settimana 1', 'Workshop di diagnosi in sede'], ['Settimana 2', 'Presentazione del concept']].forEach((r, i) => { const y = 2.1 + i * 1.3;
  s.addShape(pres.shapes.ROUND_2_SAME_RECTANGLE, { x: 0.6, y, w: 12.13, h: 1.05, fill: { color: 'F6EDD3' }, flipV: true, rectRadius: 0.3, line: { type: 'none' } });
  label(s, r[0].toUpperCase(), 0.95, y + 0.38, 2.6, 'C93A20');
  s.addText(r[1], { x: 3.8, y: y + 0.22, w: 8.6, h: 0.6, fontSize: 20, color: C.text1, margin: 0, valign: 'middle', isTextBox: true }); });

// 12 chiusura
s = pres.addSlide({ masterName: 'BZ_CHIUSURA', sectionTitle: 'Chiusura' });
s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 4.17, y: 6.36, w: 5.0, h: 0.68, fill: { color: '000000', transparency: 12 }, rectRadius: 0.34, line: { color: '3A3A3A', width: 0.5 }, objectName: 'capsula contatti' });
s.addText('ciao@3blaze.it   ·   3blaze.it', { placeholder: 'body' });

(async () => { await pres.writeFile({ fileName: '3blaze_modello_presentazione_2027.pptx' }); await applyTheme('3blaze_modello_presentazione_2027.pptx', THEME); console.log('ok'); })();
