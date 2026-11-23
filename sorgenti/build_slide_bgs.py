from build_scene import scene, ROWS, logo_img, CREAM
# copertina: righe + pannello vetro vuoto in basso a sinistra (ospita titolo)
scene('slide_cover',1920,1080,ROWS[:5],200,[{"x":96,"y":560,"w":1120,"h":400,"radius":56,"bezel":56,"scale":85,"blur":2.4,"tint":"rgba(0,0,0,.52)"}],scale=1)
# divisore: fiamma di vetro a destra, metà sinistra nera
extra='<div style="position:absolute;left:0;top:0;bottom:0;width:58%;background:linear-gradient(90deg,#000 78%,rgba(0,0,0,0))"></div>'
scene('slide_section',1920,1080,ROWS,150,[{"x":1080,"y":400,"w":740,"h":282,"shape":"symbol","bezel":36,"scale":70}],scale=1,extra=extra)
# chiusura: pannello con logo
scene('slide_closing',1920,1080,ROWS[:5],200,[{"x":420,"y":330,"w":1080,"h":420,"radius":64,"bezel":60,"scale":90,"blur":1.4,
      "html":logo_img('3blaze_logo_horizontal',CREAM,'left:140px;top:155px;width:800px')}],scale=1)
# sfondi videochiamata (16:9 1920x1080): pannello in basso a destra con logo piccolo, resto scena
scene('vbg_prisma',1920,1080,ROWS[:5],200,[{"x":1440,"y":900,"w":400,"h":110,"radius":55,"bezel":30,"scale":50,"tint":"rgba(0,0,0,.35)",
      "html":logo_img('3blaze_logo_horizontal',CREAM,'left:50px;top:30px;width:300px')}],scale=1)
