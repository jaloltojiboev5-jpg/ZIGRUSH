#!/usr/bin/env python3
"""ZIGRUSH -> ZIGZAG: browser look + earlier obstacles. Run at repo root."""
from pathlib import Path
import json
import sys

root = Path.cwd()
file = root / 'www' / 'index.html'
if not file.exists():
    sys.exit('Ошибка: запусти скрипт в корне GitHub-репозитория ZIGRUSH (там должна быть папка www).')
source = file.read_text(encoding='utf-8')
if 'ZIGZAG_UI_V1' in source:
    sys.exit('Обновление ZIGZAG уже применено, повторно менять файл не нужно.')


def replace_once(old, new, label):
    global source
    n = source.count(old)
    if n != 1:
        sys.exit(f'Файл отличается от проверенной версии: {label} (найдено {n} совпадений). Ничего не сохранено.')
    source = source.replace(old, new, 1)

# 1) Display name, leave storage key to preserve player records.
replace_once('<title>ZIGRUSH</title>', '<title>ZIGZAG — Ski Adventure</title>', 'название вкладки')
replace_once('<div class="brand">ZIGRUSH</div>', '<div class="brand">ZIGZAG</div>', 'название в меню')
replace_once('ZIGRUSH 4.1 • Reward Test', 'ZIGZAG • Ski Adventure', 'подпись меню')
replace_once('alt="ZIGRUSH 3"', 'alt="ZIGZAG"', 'подпись заставки')

# 2) Obstacles immediately at start, and a little more frequent, without
#    changing jump, collisions, obstacle sizes or the existing difficulty curves.
replace_once('if(!practice&&meters>30){', 'if(!practice&&meters>=0){', 'ранний старт препятствий')
replace_once('function spawn(){const top=-70,c=trackCenter()',
             'function spawn(){const top=elapsed<1.1?H*.14:-70,c=trackCenter()',
             'первое препятствие ближе к лыжнику')
replace_once('nextSpawn+=Math.max(40,96-density*50+Math.random()*18)',
             'nextSpawn+=Math.max(40,78-density*38+Math.random()*18)',
             'интервалы препятствий')

# 3) Brighter, more polished 2D slope (no physics or gameplay changes).
replace_once("ctx.fillStyle='#d8edf6';ctx.fillRect(0,0,W,H);const tw=trackWidth()",
'''// ZIGZAG_UI_V1: sky-blue snowfield, soft side banks
const snow=ctx.createLinearGradient(0,0,0,H);
snow.addColorStop(0,'#b4dce9');snow.addColorStop(1,'#e0f3f9');
ctx.fillStyle=snow;ctx.fillRect(0,0,W,H);
const tw=trackWidth()''', 'фон игрового поля')
replace_once("ctx.fillStyle='#f8fcff';ctx.fillRect(left,0,tw,H);ctx.strokeStyle='#8eafbf';ctx.lineWidth=5;",
'''const slope=ctx.createLinearGradient(left,0,right,0);
slope.addColorStop(0,'#e7f4fa');slope.addColorStop(.17,'#ffffff');
slope.addColorStop(.83,'#ffffff');slope.addColorStop(1,'#e7f4fa');
ctx.fillStyle=slope;ctx.fillRect(left,0,tw,H);
ctx.fillStyle='rgba(255,255,255,.42)';
ctx.fillRect(Math.max(0,left-10),0,10,H);ctx.fillRect(right,0,10,H);
ctx.strokeStyle='#9bbfce';ctx.lineWidth=3;''', 'цвет трассы')
replace_once("ctx.fillStyle='#1f664a';for(const q of[[0,-25,16]",
             "ctx.fillStyle='#15745d';for(const q of[[0,-25,16]", 'цвет деревьев')
replace_once("ctx.fillStyle='#e83f3f';ctx.beginPath();ctx.roundRect(-10,-8,20,25,6);ctx.fill();",
             "ctx.fillStyle='#ed5750';ctx.shadowColor='#892e2e66';ctx.shadowBlur=5;ctx.beginPath();ctx.roundRect(-10,-8,20,25,6);ctx.fill();ctx.shadowBlur=0;",
             'куртка лыжника')

style = '''
<style id="zigzag-mobile-ui-v1">
/* ZIGZAG: crisp mobile-friendly UI, safe areas and readable HUD */
:root{color-scheme:dark}
.app{background:linear-gradient(160deg,#103957 0%,#08223b 54%,#061322 100%)}
.screen:not(#game){padding:max(22px,env(safe-area-inset-top)) 20px max(24px,env(safe-area-inset-bottom))}
.brand{font-size:clamp(30px,9vw,44px);letter-spacing:.11em;line-height:1.1;
 background:linear-gradient(100deg,#ffffff 20%,#9cecff 75%,#ffffff);
 background-clip:text;-webkit-background-clip:text;color:transparent;
 text-shadow:0 5px 30px #6cceff2a}
.hero{padding:18px 0}.skiIcon{font-size:clamp(78px,20vw,108px);filter:drop-shadow(0 13px 19px #0007)}
.btn{background:linear-gradient(135deg,#11c6ec,#3474ed);border:1px solid #a0eaff44;
 box-shadow:0 10px 26px #009bef35;transition:filter .15s,transform .15s}
.btn:active,.card:active{transform:scale(.97);filter:brightness(1.1)}
.card{background:linear-gradient(160deg,#183f58,#102e49);border:1px solid #6cb6cf55;
 box-shadow:0 8px 22px #0002;min-height:96px}
.muted{color:#b4cede}.footer{color:#91b3c5;letter-spacing:.05em}
#game{background:#dceef6}.hud{top:max(14px,env(safe-area-inset-top));left:12px;right:12px;gap:9px}
.hud .pill{font-weight:850;font-size:clamp(16px,4.4vw,21px);border-radius:18px;
 padding:12px 15px;background:#092b45de;border:1px solid #c8f4ff33;
 box-shadow:0 5px 18px #153e5a35;white-space:nowrap}
.hudRight{gap:9px}.pauseBtn{width:54px;height:54px;border-radius:18px;
 background:#092b45e8;border:1px solid #c8f4ff33;box-shadow:0 5px 18px #153e5a35}
.modal{background:linear-gradient(160deg,#123b54,#081d32);border:1px solid #70b3d055;
 box-shadow:0 24px 65px #0006}.tip{bottom:max(22px,env(safe-area-inset-bottom));
 width:max-content;max-width:calc(100% - 30px);text-align:center;
 background:#082c45d9;border:1px solid #ffffff33;box-shadow:0 7px 22px #0002}
@media(max-width:390px){.hud .pill{font-size:16px;padding:11px 12px}.pauseBtn{width:48px;height:48px}}
</style>
'''
replace_once('</style></head><body>', '</style>'+style+'</head><body>', 'мобильный стиль')

# Replace the splash image with a clean ZIGZAG visual wordmark; no legacy name remains.
replace_once('<div id="z3splash"><img src="splash-zigrush3.jpg" alt="ZIGZAG"></div>',
'''<div id="z3splash" style="background:radial-gradient(ellipse at 50% 25%,#25668a,#081827 70%);flex-direction:column;gap:12px"><div style="font-size:78px;filter:drop-shadow(0 12px 18px #0007)">⛷️</div><div style="font-weight:950;letter-spacing:.14em;font-size:clamp(38px,11vw,66px)">ZIGZAG</div><div style="color:#b8d6e4;font-size:13px;letter-spacing:.18em">SKI ADVENTURE</div></div>''', 'заставка')

backup = file.with_name('index.before-zigzag.html')
if not backup.exists():
    backup.write_text(file.read_text(encoding='utf-8'), encoding='utf-8')
file.write_text(source, encoding='utf-8')

# Keep Android app id, so future updates can retain the same package identity.
cfg = root / 'capacitor.config.json'
if cfg.exists():
    data = json.loads(cfg.read_text(encoding='utf-8'))
    data['appName'] = 'ZIGZAG'
    cfg.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
print('Готово: меню, заставка, ранние препятствия, мобильные стили.')
print('Прыжок, коллизии, AdMob, лучший рекорд и appId не менялись.')
print('Изменено: www/index.html, capacitor.config.json')
print('Резервная копия: www/index.before-zigzag.html (не публикуйте её)')
