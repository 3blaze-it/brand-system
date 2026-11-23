import os, json, re
P='/home/claude/ds/project/'; O='/home/claude/brand/out/'
def rd(p): return open(p).read().strip()
def demote(md):  # ogni capitolo: "# X" -> "## X" ecc.
    return re.sub(r'^(#+)', lambda m: '#'+m.group(1), md, flags=re.M)
parts=[]
parts.append('''# 3blaze — Brand System 2027 · Documento completo per persone e IA

> Questo file contiene TUTTO il Design System 3blaze 2027 in un unico testo: regole, misure, colori, token, codice dei componenti, codice del Liquid Glass, geometria e SVG del marchio, elenco dei file. È la versione testuale dell'artifact "3blaze — Brand System 2027". Un'IA che legge solo questo file ha tutte le informazioni per produrre materiali conformi.
>
> Versione 1.0 · 17/11/2026 · Proprietario: 3BLAZE S.R.L.S. · Ordine di autorità: questo documento > manuale PDF > esempi.

## Indice
1. Panoramica (README)
2. Marchio · 3. Colore · 4. Tipografia · 5. Liquid Glass · 6. Layout e immagini (Trama Vetro) · 7. Stampati · 8. Cartellonistica e social · 9. Voce · 10. Per le IA
11. Componenti (regole d'uso)
- Appendice A — Token di design (CSS e JSON)
- Appendice B — Codice Liquid Glass (JS + CSS)
- Appendice C — Codice dei componenti (CSS, JS, tipi)
- Appendice D — Marchio: geometria e SVG ufficiali
- Appendice E — Elenco dei file della cartella brand-2027
''')
parts.append(demote(rd(P+'README.md')))
for f in sorted(x for x in os.listdir(P) if re.match(r'\d\d-.*\.md$',x)):
    parts.append(demote(rd(P+f)))
comp='# Componenti\n\n'+'\n\n'.join(demote(rd(P+f'components/{c}/README.md')) for c in ['Logo','Button','Tag','LiquidGlass','PrismaScene'])
parts.append(demote(comp))
def code(lang,txt): return f'```{lang}\n{txt}\n```'
parts.append('## Appendice A — Token di design\n\nI token sono la fonte di verità per colori, tipografia, spazi, raggi, ombre, movimento e vetro. In CSS si usano come variabili `--nome`.\n\n### tokens.css\n'+code('css',rd(O+'code/tokens.css'))+'\n\n### tokens.json\n'+code('json',rd(O+'code/tokens.json')))
parts.append('## Appendice B — Codice Liquid Glass\n\nVetro reale con rifrazione (feDisplacementMap su mappa di spostamento generata), dispersione RGB e riflesso speculare. Uso: aggiungere l\'attributo `data-lg` a un elemento e includere i due file. Funziona pienamente su Chromium; altrove si attiva il fallback `.lg--fallback`.\n\n### liquid-glass.css\n'+code('css',rd(O+'code/liquid-glass.css'))+'\n\n### liquid-glass.js\n'+code('js',rd(O+'code/liquid-glass.js')))
parts.append('## Appendice C — Codice dei componenti\n\n### bundle.css\n'+code('css',rd(P+'components/bundle.css'))+'\n\n### bundle.js\n'+code('js',rd(P+'components/bundle.js'))+'\n\n### index.d.ts\n'+code('ts',rd(P+'components/index.d.ts')))
L=O+'logo/'
svgs=''.join(f'\n### {n}.svg\n'+code('svg',rd(L+n+'.svg'))+'\n' for n in ['3blaze_flame','3blaze_symbol','3blaze_logo_horizontal','3blaze_logo_stacked','3blaze_wordmark','3blaze_net','3blaze_academy','luisa'])
parts.append('## Appendice D — Marchio: geometria e SVG ufficiali\n\nGli SVG usano `fill="currentColor"`: il colore si imposta dal contesto (Crema #FDF6E2 su Nero, Nero #000000 su Crema/Brace). Non ridisegnare mai il marchio: copiare questi file. Varianti colorate, versioni con claim e PNG sono nella cartella `logo/`.\n\n### _geometry.json\n'+code('json',rd(L+'_geometry.json'))+'\n'+svgs)
idx='''## Appendice E — Elenco dei file (cartella brand-2027)

| Cartella | Contenuto |
|---|---|
| `manuale/` | Corporate Brand Guidelines 2027, PDF 69 pagine |
| `guideline-ia/` | Questo documento in MD e PDF |
| `logo/` | SVG e PNG di tutte le versioni (holding, divisioni, claim), tavola costruttiva |
| `fonts/` | 3blaze Sans (Regular, Italic), 3blaze Display, JetBrains Mono |
| `codice/` | tokens.css, tokens.json, token DTCG, liquid-glass.js/.css, componenti CSS |
| `trama/` | Trama Vetro: JPG 16:9, 9:16, 1:1, A4 verticale e orizzontale |
| `vetro/` | Render della scena Prisma con vetro reale (slide, hero, social, retro biglietto) |
| `presentazioni/` | Modello PowerPoint 2027 + anteprima PDF |
| `stampati/` | Carta intestata, biglietti, busta, cartellina, copertina documento, firma email |
| `badge-eventi/` | Badge evento, badge dipendente CR80, lanyard |
| `cartellonistica/` | Affissione, roll-up, targa, insegna, wayfinding |
| `social/` | Avatar, post 4:5, cover LinkedIn |
| `video/` | Sottopancia, end card, video annuncio identità 9:16 |
| `videochiamate/` | Sfondi call per divisione e Prisma |
| `icone/` | Icone app e favicon |
| `sorgenti/` | Script che generano tutto il sistema |
'''
parts.append(idx)
md='\n\n---\n\n'.join(parts)+'\n'
MAP=[('f5fe907c','vetro/prisma_hero.png','3blaze — scena Prisma: Trama Vetro e pannello liquid glass'),('b5291d7a','logo/3blaze_tavola_costruttiva.png',None),('69c7a88c','vetro/prisma_flame.png',None),
 ('26b387ce','stampati/carta_intestata_A4_crema.png',None),('6bf1faee','stampati/biglietti_da_visita_85x55_abbondanza3mm.png',None),('53e82ff3','cartellonistica/affissione_6x3m_scala1-10.png',None),
 ('ef9e4328','cartellonistica/rollup_85x200cm_scala1-4.png',None),('452dbe00','cartellonistica/targa_ingresso_400x200mm.png',None),('7f433bc5','cartellonistica/insegna_cassonetto_300x60cm_scala1-10.png',None),('00b52568','social/social_post_1080x1350.png',None)]
for h,rel,alt in MAP:
    md=re.sub(r'!\[([^\]]*)\]\(/_blob/'+h+r'[0-9a-f]*\)', lambda m: f'![{alt or m.group(1)}](../{rel})', md)
open('3blaze_Brand_System_2027_completo.md','w').write(md); print(len(md))
