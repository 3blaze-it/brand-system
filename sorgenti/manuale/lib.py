"""Libreria di impaginazione del manuale 3blaze (A4 orizzontale, 1123x794 px CSS)."""
import json
B='/home/claude/brand'
A=json.load(open(B+'/logo_assets.json'))
FLAME=A['3blaze_flame']['d']
CREAM='#FDF6E2'; BLACK='#000000'; OR='#FB4F31'; OR_INK='#C93A20'; TEAL='#006172'; TEAL_L='#3FA9BA'
WINE='#4D1821'; WINE_L='#D98C99'; MUTED_L='#6B665C'; MUTED_D='#A8A294'; INK2='#2A2620'
W,H=1123,794
SECTIONS=['Introduzione','Il marchio','Architettura di marca','Colore','Tipografia','Liquid Glass','Elementi grafici','Applicazioni','Voce','Appendice']

def logo(key, color=BLACK, css='', cls=''):
    x,y,w,h=A[key]['viewBox']
    return f'<svg class="{cls}" viewBox="{x} {y} {w} {h}" style="display:block;aspect-ratio:{w}/{h};{css}" aria-label="{A[key]["title"]}"><path fill="{color}" d="{A[key]["d"]}"/></svg>'

def flame(color=BLACK, css=''):
    return logo('3blaze_flame', color, css)

ICONS={
 'home':'<path d="M4 11.5 12 4l8 7.5V20h-5.5v-5.5h-5V20H4z"/>',
 'search':'<circle cx="10.5" cy="10.5" r="6"/><path d="m15 15 5 5"/>',
 'play':'<path d="M8 5.5v13l10.5-6.5z" fill="currentColor"/>',
 'pause':'<path d="M8 5v14M16 5v14"/>',
 'user':'<circle cx="12" cy="8.5" r="3.8"/><path d="M4.5 20c1.2-4 4-6 7.5-6s6.3 2 7.5 6"/>',
 'plus':'<path d="M12 5v14M5 12h14"/>',
 'share':'<path d="M12 3.5v11M7.5 8 12 3.5 16.5 8M5.5 13v6.5h13V13"/>',
 'close':'<path d="m6.5 6.5 11 11M17.5 6.5l-11 11"/>',
 'chev':'<path d="m9.5 5.5 6.5 6.5-6.5 6.5"/>',
 'back':'<path d="M14.5 5.5 8 12l6.5 6.5"/>',
 'grid':'<rect x="4.5" y="4.5" width="6" height="6" rx="1.5"/><rect x="13.5" y="4.5" width="6" height="6" rx="1.5"/><rect x="4.5" y="13.5" width="6" height="6" rx="1.5"/><rect x="13.5" y="13.5" width="6" height="6" rx="1.5"/>',
 'bell':'<path d="M6.5 16.5V11a5.5 5.5 0 0 1 11 0v5.5l1.5 1.5h-14z"/><path d="M10 20.5h4"/>',
 'mic':'<rect x="9" y="3.5" width="6" height="11" rx="3"/><path d="M5.5 11.5a6.5 6.5 0 0 0 13 0M12 18v3"/>',
 'calendar':'<rect x="4" y="5.5" width="16" height="14.5" rx="2.5"/><path d="M4 10h16M8.5 3.5v4M15.5 3.5v4"/>',
 'book':'<path d="M4.5 5.5c2.5-1 5-1 7.5.8 2.5-1.8 5-1.8 7.5-.8v13c-2.5-1-5-1-7.5.8-2.5-1.8-5-1.8-7.5-.8z"/><path d="M12 6.3v13"/>',
 'news':'<rect x="4" y="5" width="16" height="14" rx="2.5"/><path d="M7.5 9h9M7.5 12.5h9M7.5 16h5"/>',
 'spark':'<path d="M12 3.5 13.8 10.2 20.5 12l-6.7 1.8L12 20.5l-1.8-6.7L3.5 12l6.7-1.8z"/>',
 'heart':'<path d="M12 19.5s-7.5-4.6-7.5-10A4.2 4.2 0 0 1 12 7a4.2 4.2 0 0 1 7.5 2.5c0 5.4-7.5 10-7.5 10z"/>',
 'pin':'<path d="M12 21s-6.5-6-6.5-11a6.5 6.5 0 0 1 13 0c0 5-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>',
 'mail':'<rect x="3.5" y="5.5" width="17" height="13" rx="2.5"/><path d="m4 7 8 6 8-6"/>',
 'more':'<circle cx="6" cy="12" r="1.3" fill="currentColor"/><circle cx="12" cy="12" r="1.3" fill="currentColor"/><circle cx="18" cy="12" r="1.3" fill="currentColor"/>',
 'settings':'<circle cx="12" cy="12" r="3"/><path d="M12 3.5v2.5M12 18v2.5M3.5 12H6M18 12h2.5M6 6l1.8 1.8M16.2 16.2 18 18M6 18l1.8-1.8M16.2 7.8 18 6"/>',
 'arrow':'<path d="M5 12h13M13 6.5l5.5 5.5-5.5 5.5"/>',
}
def icon(name, size=20, color='currentColor', sw=1.7):
    return (f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="square" stroke-linejoin="miter" style="display:block;color:{color}">{ICONS[name]}</svg>')

def glass(x, y, w, h, inner='', r=None, variant='regular', bezel=None, scale=None, disp=0.22, blur=None, extra_style='', shape=None, cls=''):
    """Superficie Liquid Glass in stile iOS. variant: regular | clear | tint | tint-teal | tint-wine | light."""
    r = min(w, h)/2 if r is None else r
    bezel = bezel if bezel is not None else max(8, min(36, min(w, h)*0.32))
    scale = scale if scale is not None else max(24, min(90, bezel*1.9))
    blur = blur if blur is not None else {'regular':3.2,'clear':0.6,'light':2.4}.get(variant,1.6)
    a=f'data-lg data-lg-bezel="{bezel:.0f}" data-lg-scale="{scale:.0f}" data-lg-dispersion="{disp}" data-lg-blur="{blur}"'
    if shape=='flame': a+=f' data-lg-path="{FLAME}" data-lg-viewbox="0 0 480 700"'
    elif shape=='symbol':
        sv=A['3blaze_symbol']['viewBox']; a+=f' data-lg-path="{A["3blaze_symbol"]["d"]}" data-lg-viewbox="{sv[0]} {sv[1]} {sv[2]} {sv[3]}"'
    else: a+=f' data-lg-radius="{r:.0f}"'
    return (f'<div class="gl gl-{variant} {cls}" {a} style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;'
            + (f'border-radius:{r}px;' if not shape else '') + f'{extra_style}">{inner}</div>')

def rows(words=None, size=100, colors=None, top=0, height=None, offset=0, cls='', opacity=None, ink=None):
    """Trama Vetro 2027: '3blaze' in vetro gigante su Nero, colori del brand solo sui bordi. (words/colors ignorati: compatibilità)"""
    hh = height or H
    if ink in (BLACK,'#000','#000000') or (colors and colors[0] in (BLACK,'#000','#000000')):
        return ''   # sul tema Crema la trama non si usa: fondo pieno
    pos = ['30% 40%','70% 20%','15% 80%','85% 65%','50% 50%','60% 85%'][int(size+offset)%6]
    op = opacity if opacity is not None else 1
    if colors and colors[0] not in (CREAM,): op = min(op, .55)
    return (f'<div class="rows {cls}" style="top:{top}px;height:{hh}px;opacity:{op};'
            f'background:#000 url(\'{B}/out/trama/3blaze_trama_vetro_16x9.jpg\') {pos}/cover"></div>')

CSS = f'''
@font-face{{font-family:'3blaze Sans';src:url({B}/out/fonts/3blazeSans-Regular.woff2);font-weight:500}}
@font-face{{font-family:'3blaze Sans';src:url({B}/out/fonts/3blazeSans-Italic.woff2);font-style:italic;font-weight:500}}
@font-face{{font-family:'3blaze Display';src:url({B}/out/fonts/3blazeDisplay-Regular.woff2)}}
@font-face{{font-family:'JetBrains Mono';src:url({B}/out/fonts/JetBrainsMono-Medium.woff2);font-weight:500}}
@font-face{{font-family:'JetBrains Mono';src:url({B}/out/fonts/JetBrainsMono-Regular.woff2);font-weight:400}}
@page{{size:297mm 210mm;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{-webkit-print-color-adjust:exact;print-color-adjust:exact;background:#555}}
body{{font-family:'3blaze Sans','JetBrains Mono',sans-serif;font-weight:500;color:{BLACK}}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{CREAM};page-break-after:always;break-after:page}}
.page.dark{{background:{BLACK};color:{CREAM}}}
.page:last-of-type{{page-break-after:auto;break-after:auto}}
.mono{{font-family:'JetBrains Mono',monospace;font-weight:500;text-transform:uppercase;letter-spacing:.14em}}
.abs{{position:absolute}}
.hd{{position:absolute;left:48px;right:48px;top:26px;display:flex;justify-content:space-between;font-size:6.6px;color:{MUTED_L}}}
.ft{{position:absolute;left:48px;right:48px;bottom:24px;display:flex;justify-content:space-between;align-items:center;font-size:6.6px;color:{MUTED_L}}}
.dark .hd,.dark .ft{{color:{MUTED_D}}}
.ft .pg{{display:flex;align-items:center;gap:8px}}
.code{{font-size:8px;color:{OR_INK};letter-spacing:.14em}}
.dark .code{{color:{OR}}}
.h1{{font-size:27px;line-height:1.08;letter-spacing:-.01em}}
.h2{{font-size:17px;line-height:1.2}}
.lead{{font-size:12.5px;line-height:1.5}}
.p{{font-size:9.6px;line-height:1.6;color:{INK2}}}
.dark .p{{color:#D9D2C0}}
.p p+p{{margin-top:7px}}
.cap{{font-size:6.4px;line-height:1.5;color:{MUTED_L};letter-spacing:.12em}}
.dark .cap{{color:{MUTED_D}}}
.it{{font-style:italic}}
.rule{{position:absolute;height:0;border-top:.75px solid #0000002A}}
.dark .rule{{border-top-color:#FDF6E22E}}
.tbl{{width:100%;border-collapse:collapse;font-size:8.6px;line-height:1.45}}
.tbl th{{font-family:'JetBrains Mono';font-weight:500;font-size:6.2px;letter-spacing:.12em;text-transform:uppercase;color:{MUTED_L};text-align:left;padding:0 8px 6px 0;border-bottom:.75px solid #00000040}}
.tbl td{{padding:6px 8px 6px 0;border-bottom:.75px solid #0000001F;vertical-align:top}}
.dark .tbl th{{color:{MUTED_D};border-bottom-color:#FDF6E240}} .dark .tbl td{{border-bottom-color:#FDF6E220}}
.sw{{position:absolute;border-radius:0 0 18px 18px;overflow:hidden}}
.do,.dont{{font-size:6.4px;letter-spacing:.12em;display:flex;align-items:center;gap:6px}}
.do::before,.dont::before{{content:'';width:9px;height:9px;border-radius:50%}}
.do::before{{background:#3DDC97}} .dont::before{{background:{OR}}}
.box{{position:absolute;border-radius:0 0 22px 22px;overflow:hidden}}
.rows{{position:absolute;left:0;right:0;overflow:hidden}}
.row{{font-family:'3blaze Display';line-height:1.0;white-space:nowrap;border-top:1px solid #FDF6E21F;padding-top:.02em}}
/* Liquid Glass (stile iOS) */
.gl{{position:absolute;isolation:isolate;display:flex;align-items:center;justify-content:center;color:{CREAM}}}
.gl.lg::before{{opacity:.38}}
.gl-regular{{background-color:#0E0C0A9E !important}}
.gl-clear{{background-color:#FDF6E208 !important}}
.gl-light{{background-color:#FDF6E28C !important;color:{BLACK}}}
.gl-tint{{background-color:#FB4F31B8 !important;color:{BLACK}}}
.gl-tint-teal{{background-color:#006172BF !important}}
.gl-tint-wine{{background-color:#4D1821C7 !important}}
.gl-txt{{font-size:12px;letter-spacing:.01em;text-shadow:0 1px 2px #0000007A}}
.gl-tint .gl-txt,.gl-light .gl-txt{{text-shadow:none}}
.lg--baked::before,.lg--baked::after{{display:none !important}}
.lg--baked{{background-color:transparent !important;backdrop-filter:none !important;-webkit-backdrop-filter:none !important}}
.snap > *{{visibility:hidden !important}}
.ann{{position:absolute;font-family:'JetBrains Mono';font-size:6.2px;letter-spacing:.1em;text-transform:uppercase;color:{OR_INK};white-space:nowrap}}
.dark .ann{{color:{OR}}}
.ann-l{{position:absolute;border-top:.75px solid {OR}}}
.phone{{position:absolute;border-radius:46px;background:#0B0B0B;box-shadow:0 0 0 2px #2a2a2a, 0 30px 60px -20px #0009;overflow:hidden}}
.phone .scr{{position:absolute;inset:9px;border-radius:38px;overflow:hidden;background:{BLACK}}}
.island{{position:absolute;left:50%;top:10px;width:84px;height:24px;margin-left:-42px;border-radius:12px;background:#000;z-index:5}}
.win{{position:absolute;border-radius:14px;overflow:hidden;box-shadow:0 30px 70px -25px #000A, 0 0 0 1px #0000001A;background:{BLACK}}}
'''

def header(sec_idx, sec_name, dark=False):
    return f'<div class="hd mono"><span>3blaze — Corporate Brand Guidelines</span><span>{sec_idx:02d} — {sec_name}</span></div>'

def footer(n, dark=False):
    col = CREAM if dark else BLACK
    return (f'<div class="ft mono"><span class="pg">{flame(col,"width:7px")}<span>{n:03d}</span></span>'
            f'<span>Edizione 1.0 — 2027</span></div>')

class Doc:
    def __init__(self): self.pages=[]; self.toc=[]
    def add(self, body, dark=False, sec=None, chrome=True, cls=''):
        n=len(self.pages)+1
        hf=''
        if chrome and sec is not None:
            hf=header(sec, SECTIONS[sec], dark)+footer(n, dark)
        self.pages.append(f'<section class="page {"dark" if dark else ""} {cls}" data-n="{n}">{body}{hf}</section>')
        return n
    def html(self):
        return (f'<!doctype html><html lang="it"><head><meta charset="utf-8"><title>3blaze — Corporate Brand Guidelines 2027</title>'
                f'<link rel="stylesheet" href="{B}/out/code/liquid-glass.css"><style>{CSS}</style></head><body>'
                + f'<svg width="0" height="0" style="position:absolute"><defs><path id="lgpat" fill="currentColor" d="{A["3blaze_logo_horizontal"]["d"]}"/></defs></svg>' + ''.join(self.pages) + f'<script src="{B}/out/code/liquid-glass.js"></script></body></html>')

def text_col(code, title, body, x=48, y=88, w=300, lead=None):
    l = f'<div class="lead" style="margin-top:14px">{lead}</div>' if lead else ''
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px"><div class="code mono">{code}</div>'
            f'<div class="h1" style="margin-top:10px">{title}</div>{l}<div class="p" style="margin-top:14px">{body}</div></div>')

def cap(x, y, txt, w=None, color=None):
    return f'<div class="cap mono abs" style="left:{x}px;top:{y}px;{f"width:{w}px;" if w else ""}{f"color:{color};" if color else ""}">{txt}</div>'
