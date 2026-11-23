"""Fonte unica dei token 3blaze 2027 → tokens.json (Design System), tokens.css, 3blaze.tokens.json (DTCG per tool esterni)."""
import json, os
OUT='/home/claude/brand/out'

THEMES=[{"id":"dark","name":"Nero (primario)"},{"id":"light","name":"Crema"}]
C=[
 # nome, {dark, light}, uso
 ("ground", {"dark":"#000000","light":"#FDF6E2"}, "Fondo pagina. Nero è il fondo del gruppo; Crema è il fondo editoriale e della carta."),
 ("surface-1", {"dark":"#0E0E0E","light":"#F6EDD3"}, "Prima superficie su ground: sezioni, pannelli opachi."),
 ("surface-2", {"dark":"#1A1A1A","light":"#EDE3C6"}, "Seconda superficie: card opache, campi di input."),
 ("ink", {"dark":"#FDF6E2","light":"#000000"}, "Testo e logo su ground/surface. 19,5:1."),
 ("ink-muted", {"dark":"#A8A294","light":"#6B665C"}, "Testo secondario, didascalie. ≥5,3:1 su ground in entrambi i temi."),
 ("hairline", {"dark":"#FDF6E224","light":"#0000001F"}, "Filetti 1px tra righe tipografiche e sezioni."),
 ("brand-nero", "#000000", "Colore istituzionale del gruppo 3blaze (media / holding)."),
 ("brand-crema", "#FDF6E2", "Crema 3blaze: il 'bianco' del brand. Mai #FFFFFF per fondi o logo."),
 ("academy", "#FB4F31", "Brace — 3blaze academy. Fondi, logo, numeri grandi. Testo crema su Brace solo ≥24px (3,1:1); per testo piccolo usare nero (6,3:1)."),
 ("academy-ink", {"dark":"#FB4F31","light":"#C93A20"}, "Brace come TESTO: su crema serve la versione profonda (4,7:1); su nero va bene la Brace piena (6,3:1)."),
 ("news", "#006172", "Petrolio — 3blaze .net (news). Fondi e logo. Crema su Petrolio 6,6:1."),
 ("news-ink", {"dark":"#3FA9BA","light":"#006172"}, "Petrolio come TESTO: su nero serve la versione chiara (7,6:1)."),
 ("ia", "#4D1821", "Vinaccia — luisa (IA). Fondi e logo. Crema su Vinaccia 13,3:1."),
 ("ia-ink", {"dark":"#D98C99","light":"#4D1821"}, "Vinaccia come TESTO: su nero serve la versione chiara (8,2:1)."),
 ("accent", {"dark":"{academy}","light":"{academy-ink}"}, "Accento del gruppo: la Brace. Una sola cosa per schermata (CTA, numero chiave)."),
 ("focus", "#2EC4FF", "Anello di focus da tastiera (2px + 2px di offset). Mai decorativo."),
 ("prism-1", "#FF4F31", "Prisma — solo bordo arcobaleno del liquid glass. Rosso."),
 ("prism-2", "#FFD23F", "Prisma — giallo."),
 ("prism-3", "#3DDC97", "Prisma — verde."),
 ("prism-4", "#2EC4FF", "Prisma — ciano."),
 ("prism-5", "#7B61FF", "Prisma — viola."),
 ("prism-6", "#FF5FA2", "Prisma — magenta. I sei Prisma esistono solo come rifrazione: mai fondi, mai testo."),
 ("glass-tint", {"dark":"#FDF6E20A","light":"#FFFFFF33"}, "Velo del pannello liquid glass sopra la rifrazione."),
]

TYPE={
 "fonts":[
  {"family":"3blaze Sans","file":"fonts/3blazeSans-Regular.woff2","weight":"500","style":"normal"},
  {"family":"3blaze Sans","file":"fonts/3blazeSans-Italic.woff2","weight":"500","style":"italic"},
  {"family":"3blaze Display","file":"fonts/3blazeDisplay-Regular.woff2","weight":"400","style":"normal"},
  {"family":"JetBrains Mono","file":"fonts/JetBrainsMono-Regular.woff2","weight":"400","style":"normal"},
  {"family":"JetBrains Mono","file":"fonts/JetBrainsMono-Medium.woff2","weight":"500","style":"normal"}],
 "families":{
  "sans":"\"3blaze Sans\", \"Futura\", system-ui, sans-serif",
  "display":"\"3blaze Display\", \"3blaze Sans\", sans-serif",
  "mono":"\"JetBrains Mono\", ui-monospace, \"SF Mono\", Menlo, monospace"},
 "groups":[
  {"name":"Display","family":"display","styles":[
    {"name":"display-xl","fontSize":"160px","lineHeight":0.92,"fontWeight":400,"letterSpacing":"-0.01em","sample":"MEDIA","usage":"Manifesti, hero di pagina, affissioni. Solo maiuscolo o 1–2 parole. Mai sotto 48px."},
    {"name":"display-l","fontSize":"112px","lineHeight":0.95,"fontWeight":400,"letterSpacing":"-0.01em","sample":"Una holding, quattro fuochi.","usage":"Titolo di apertura di sezione."},
    {"name":"display-m","fontSize":"72px","lineHeight":1.0,"fontWeight":400,"sample":"2027","usage":"Numeri chiave, titoli di slide. Minimo assoluto del Display: 48px."}]},
  {"name":"Titoli","family":"sans","styles":[
    {"name":"headline-l","fontSize":"48px","lineHeight":1.05,"fontWeight":500,"letterSpacing":"-0.02em","sample":"Strategia, contenuti e codice.","usage":"H1 in 3blaze Sans."},
    {"name":"headline-m","fontSize":"32px","lineHeight":1.15,"fontWeight":500,"letterSpacing":"-0.01em","sample":"Un sistema, quattro fuochi.","usage":"H2."},
    {"name":"title","fontSize":"24px","lineHeight":1.25,"fontWeight":500,"sample":"3blaze academy","usage":"H3, titoli di card."},
    {"name":"title-italic","fontSize":"24px","lineHeight":1.25,"fontWeight":500,"fontStyle":"italic","sample":"Spigoli in alto, curve in basso.","usage":"Occhielli, citazioni brevi. Il corsivo è la voce del marchio."}]},
  {"name":"Testo","family":"sans","styles":[
    {"name":"body-l","fontSize":"19px","lineHeight":1.55,"fontWeight":500,"sample":"Ogni progetto parte da una domanda semplice: cosa rende un brand impossibile da confondere?","usage":"Lead, primo paragrafo."},
    {"name":"body","fontSize":"16px","lineHeight":1.6,"fontWeight":500,"sample":"Strategia, contenuti e design lavorano come un unico sistema, sullo schermo e nel mondo fisico.","usage":"Testo corrente. Misura 60–72 caratteri."},
    {"name":"small","fontSize":"14px","lineHeight":1.5,"fontWeight":500,"sample":"Consegna in 3 settimane.","usage":"Note, form, tabelle."},
    {"name":"caption","fontSize":"13px","lineHeight":1.45,"fontWeight":500,"fontStyle":"italic","sample":"Foto: backstage matchday, Terni 2027.","usage":"Didascalie."}]},
  {"name":"Codice","family":"mono","styles":[
    {"name":"label","fontSize":"12px","lineHeight":1.3,"fontWeight":500,"letterSpacing":"0.12em","sample":"01 — MEDIA · TERNI · 2027","usage":"Etichette maiuscole, numerazioni, metadati. Lo strato 'codice' del brand."},
    {"name":"code","fontSize":"14px","lineHeight":1.55,"fontWeight":400,"sample":"--accent: var(--academy);","usage":"Snippet, specifiche tecniche, dati."}]}
 ]}

SPACE=[("space-1","4px","Spazio minimo: icona ↔ testo."),("space-2","8px","Gap interno di chip e bottoni piccoli."),
 ("space-3","12px","Padding verticale bottoni."),("space-4","16px","Padding card piccola, gap di form."),
 ("space-6","24px","Padding card, gutter griglia mobile."),("space-8","32px","Gutter griglia desktop."),
 ("space-12","48px","Distanza tra blocchi in sezione."),("space-16","64px","Margine di sezione mobile."),
 ("space-24","96px","Margine di sezione desktop."),("space-32","128px","Respiro di apertura (hero).")]
RADIUS=[("radius-xs","6px","Chip, tag, input piccoli."),("radius-sm","12px","Input, bottoni secondari."),
 ("radius-md","20px","Card opache."),("radius-lg","32px","Pannelli liquid glass (default)."),
 ("radius-xl","48px","Glass hero e media grandi."),("radius-pill","999px","Bottoni primari, toggle: l'arco della fiamma.")]
SHADOW=[("shadow-glass",{"dark":"0 24px 60px -18px #0000008C, 0 2px 6px #00000040","light":"0 24px 60px -24px #3D2A0A40, 0 2px 6px #3D2A0A1F"},"Ombra dei pannelli liquid glass."),
 ("shadow-lift",{"dark":"0 8px 24px -8px #00000099","light":"0 8px 24px -10px #3D2A0A33"},"Card opache sollevate.")]
GLASS=[("glass-bezel","40px","Larghezza del bordo rifrangente (lente) dei pannelli."),
 ("glass-refraction","70","Intensità di spostamento (scale di feDisplacementMap)."),
 ("glass-dispersion","0.22","Separazione R/G/B sul bordo: genera il bordo arcobaleno."),
 ("glass-blur","1.2px","Micro-sfocatura del vetro: solo per ammorbidire, mai per nascondere.")]
MOTION_NOTE="Durate: 160ms (hover), 280ms (pannelli), 600ms (hero). Easing: cubic-bezier(.2,.8,.2,1)."

def tokens_json():
    col=[]
    for n,v,u in C: col.append({"name":n,"value":v,"usage":u})
    return {"name":"3blaze","version":1,
      "meta":{"source":"Ricostruzione marchio 2027 (palette fornita da 3blaze, font 3blaze Sans v0.2 e 3blaze Display)","motion":MOTION_NOTE},
      "color":{"themes":THEMES,"tokens":col},"type":TYPE,
      "spacing":{"tokens":[{"name":a,"value":b,"usage":c} for a,b,c in SPACE]},
      "radius":{"tokens":[{"name":a,"value":b,"usage":c} for a,b,c in RADIUS]},
      "shadow":{"tokens":[{"name":a,"value":b,"usage":c} for a,b,c in SHADOW]},
      "glass":{"note":"Parametri del liquid glass reale (vedi liquid-glass.js).","tokens":[{"name":a,"value":b,"usage":c} for a,b,c in GLASS]}}

def resolve(v, theme):
    if isinstance(v,dict): v=v.get(theme, v.get('dark'))
    if isinstance(v,str) and v.startswith('{'):
        ref=v[1:-1]; return 'var(--%s)'%ref
    return v

def tokens_css():
    L=["/* 3blaze 2027 — tokens.css (generato da tokens_src.py). Non modificare a mano. */"]
    for th in ['dark','light']:
        sel=':root, [data-theme="dark"]' if th=='dark' else '[data-theme="light"]'
        L.append(sel+" {")
        for n,v,u in C: L.append(f"  --{n}: {resolve(v,th)};")
        for n,v,u in SHADOW: L.append(f"  --{n}: {resolve(v,th)};")
        L.append("}")
    L.append(":root {")
    for a,b,c in SPACE+RADIUS+GLASS: L.append(f"  --{a}: {b};")
    for k,v in TYPE['families'].items(): L.append(f"  --font-{k}: {v};")
    L.append("  --ease-out: cubic-bezier(.2,.8,.2,1);\n  --dur-1: 160ms; --dur-2: 280ms; --dur-3: 600ms;\n}")
    for f in TYPE['fonts']:
        L.append(f"@font-face {{ font-family: '{f['family']}'; src: url('{f['file'].replace('fonts/','../fonts/')}') format('woff2'); font-weight: {f['weight']}; font-style: {f['style']}; font-display: swap; }}")
    for g in TYPE['groups']:
        for s in g['styles']:
            fam=s.get('family',g['family'])
            props=[f"font-family: var(--font-{fam})", f"font-size: {s['fontSize']}", f"line-height: {s['lineHeight']}", f"font-weight: {s['fontWeight']}"]
            if 'letterSpacing' in s: props.append(f"letter-spacing: {s['letterSpacing']}")
            if s.get('fontStyle'): props.append(f"font-style: {s['fontStyle']}")
            if fam=='mono' and s['name']=='label': props.append("text-transform: uppercase")
            L.append(f".t-{s['name']} {{ {'; '.join(props)}; }}")
    return "\n".join(L)+"\n"

def dtcg():
    out={"$description":"3blaze 2027 design tokens (formato W3C DTCG) per Figma Tokens / Style Dictionary.","color":{},"space":{},"radius":{}}
    for n,v,u in C:
        if isinstance(v,dict):
            out["color"][n]={"$type":"color","$value":resolve(v,'dark') if not str(v.get('dark','')).startswith('{') else v['dark'],"$description":u,"$extensions":{"3blaze.themes":v}}
        else: out["color"][n]={"$type":"color","$value":v,"$description":u}
    for a,b,c in SPACE: out["space"][a]={"$type":"dimension","$value":b,"$description":c}
    for a,b,c in RADIUS: out["radius"][a]={"$type":"dimension","$value":b,"$description":c}
    return out

if __name__=='__main__':
    os.makedirs(OUT+'/code',exist_ok=True)
    json.dump(tokens_json(),open(OUT+'/code/tokens.json','w'),indent=1,ensure_ascii=False)
    open(OUT+'/code/tokens.css','w').write(tokens_css())
    json.dump(dtcg(),open(OUT+'/code/3blaze.tokens.dtcg.json','w'),indent=1,ensure_ascii=False)
    print('ok')
