# 3blaze — Brand 2027 · cartella di lavoro

**Prima di tutto:** installa i font da `fonts/` (file .ttf, doppio clic → Installa). Senza i font il modello PowerPoint e i file modificabili mostrano un carattere sostitutivo.

| Cartella | Contenuto |
|---|---|
| `manuale/3blaze_Corporate_Brand_Guidelines_2027.pdf` | Il manuale completo: 69 pagine A4 orizzontali, 9 capitoli. |
| `BRAND_GUIDELINES_3blaze_2027.md` | Il manuale in testo, per IA e strumenti automatici. |
| `logo/svg` · `logo/png` | Tutti i marchi: SVG (nero, crema, colori di divisione, currentColor), PNG @2x e ad alta risoluzione. `3blaze_logo_claim_*` = marchio con la firma *Ignite Beyond.*; `3blaze_claim_*` = claim da solo. |
| `logo/3blaze_tavola_costruttiva.pdf` | Tavola costruttiva A3. |
| `fonts` | 3blaze Sans (tondo, corsivo), 3blaze Display, JetBrains Mono: .ttf da installare, .woff2 per il web. |
| `codice` | `tokens.css`, `tokens.json`, `3blaze.tokens.dtcg.json` (Figma/Style Dictionary), `liquid-glass.js` + `.css`, `3blaze-components.css`. |
| `presentazioni` | Modello PowerPoint 16:9 con layout (copertina, divisore, contenuti, manifesto, chiusura) + anteprima PDF. |
| `stampati` | Carta intestata (bianco/crema), biglietti da visita, busta DL, cartellina, copertina documento, firma email. |
| `badge-eventi` | Badge evento 90×130 (staff, speaker, ospite, stampa, luisa lab + retro), badge dipendente CR80, lanyard. |
| `cartellonistica` | Affissione 6×3 (1:10), roll-up 85×200 (1:4), targa ingresso, insegna (1:10), segnaletica interna. |
| `social` | Avatar per divisione, cover LinkedIn, post 4:5. |
| `video` · `videochiamate` | Video annuncio nuova identità 9:16 (22 s, MP4), sottopancia (PNG trasparente), chiusura video, sfondi Meet/Teams/Zoom per divisione. |
| `icone` | Favicon e icone app per divisione (16–1024 px, ICO, SVG). |
| `guideline-ia` | Il Design System completo in un unico file: MD per le IA (regole + token + codice + SVG del marchio) e PDF da leggere/stampare. È il file da dare a un'IA. |
| `trama` | Trama Vetro: "3blaze" nascosto in vetro gigante su Nero, colori del brand sui bordi. JPG 16:9, 9:16, 1:1, A4 verticale/orizzontale. Sorgente: `sorgenti/build_trama.py`. |
| `vetro` | Render Liquid Glass ad alta risoluzione: scena Prisma (Trama Vetro + tre fiamme di vetro), sfondi slide. |
| `sorgenti` | Script che rigenerano marchio, scene, stampati, manuale e presentazione (Python + Playwright/Chromium, Node + pptxgenjs). |

Prima della stampa: inserire P.IVA, PEC, telefono e i nomi su biglietti e badge (oggi segnaposto); fissare CMYK/Pantone con lo stampatore.
