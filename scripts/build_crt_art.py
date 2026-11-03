#!/usr/bin/env python3
"""Generate frameless CRT content for one shared README monitor surface."""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "Assets" / "profile"
FONT = {
    "A": "01110/10001/10001/11111/10001/10001/10001",
    "C": "01111/10000/10000/10000/10000/10000/01111",
    "I": "11111/00100/00100/00100/00100/00100/11111",
    "N": "10001/11001/11001/10101/10011/10011/10001",
    "P": "11110/10001/10001/11110/10000/10000/10000",
    "T": "11111/00100/00100/00100/00100/00100/00100",
    "X": "10001/10001/01010/00100/01010/10001/10001",
    "0": "01110/10001/10011/10101/11001/10001/01110",
    "9": "01110/10001/10001/01111/00001/00001/01110",
}
LINKS = ("portfolio", "telegram", "sortify", "pixie", "glyph", "echo", "archive")


def text(x, y, value, size=14, cls="phosphor", end=False):
    anchor = ' text-anchor="end"' if end else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" class="{cls}"{anchor}>{escape(value)}</text>'


def svg(w, h, title, parts, extra_css="", display_width=None):
    """The README's one pre element supplies the continuous background/frame."""
    dw = display_width or w
    dh = h * dw / w
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{dw:g}" height="{dh:g}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title">
<title id="title">{escape(title)}</title>
<defs>
<pattern id="lines" width="4" height="4" patternUnits="userSpaceOnUse"><rect y="3" width="4" height="1" fill="#000" fill-opacity=".09"/></pattern>
<filter id="glow" x="-10%" y="-35%" width="120%" height="170%"><feGaussianBlur stdDeviation=".6"/><feComponentTransfer><feFuncA type="linear" slope=".35"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<style>
text{{font-family:ui-monospace,'DejaVu Sans Mono',Consolas,monospace;font-weight:400}}
.phosphor{{fill:#b2d5b7}}.dim{{fill:#88a98f}}.dots{{fill:#c2e4c5;filter:url(#glow)}}
.rule{{stroke:#3c5143;stroke-width:1}}.cell{{fill:#203428;fill-opacity:.25;stroke:#3d5545}}.accent{{stroke:#9bc5a4;stroke-width:2}}
.cursor{{fill:#b2d5b7;animation:blink 1.2s step-end infinite}}
@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
@media(prefers-color-scheme:light){{.phosphor{{fill:#315e3e}}.dim{{fill:#52755b}}.dots{{fill:#315e3e}}.rule{{stroke:#9caf9f}}.cell{{fill:#c5d9c9;fill-opacity:.4;stroke:#9caf9f}}.accent{{stroke:#52755b}}.cursor{{fill:#315e3e}}}}
{extra_css}
@media(prefers-reduced-motion:reduce){{.cursor{{animation:none}}}}
</style>
{''.join(parts)}
<rect width="{w}" height="{h}" fill="url(#lines)" pointer-events="none"/>
</svg>
'''


def bitmap(word, x, y, pitch=3.4):
    parts=[]
    for i,letter in enumerate(word):
        for row,line in enumerate(FONT[letter].split("/")):
            for col,pixel in enumerate(line):
                if pixel=="1":
                    parts.append(f'<circle cx="{x+(i*6+col)*pitch:g}" cy="{y+row*pitch:g}" r="{pitch*.33:g}"/>')
    return '<g class="dots">'+''.join(parts)+'</g>'


def top(mobile=False):
    w,h=(420,128) if mobile else (850,108)
    x=12 if mobile else 18
    p=[text(x,18,"cap@arch: ~",11,"dim"),text(w-x,18,"PERSONAL TERMINAL",10,"dim",True),
       f'<path class="rule" d="M{x} 29H{w-x}"/>',text(x,52,"$ whoami",12,"dim"),
       bitmap("XCAPTAIN09",x+1,69)]
    if mobile:p.append(text(x,113,"Muhammed Dilshad A",12,"dim"))
    else:p.append(text(w-x,83,"MUHAMMED DILSHAD A",12,"dim",True))
    return svg(w,h,"xCaptaiN09 — Muhammed Dilshad A. Android kernels / Linux desktops / AI & Data Science.",p)


def cell(x,y,w,label,value,size=14):
    return [f'<rect class="cell" x="{x}" y="{y}" width="{w}" height="48" rx="2"/>',
            f'<path class="accent" d="M{x+1} {y+11}v13"/>',text(x+12,y+17,label,10,"dim"),text(x+12,y+36,value,size)]


def bottom(mobile=False):
    w,h=(420,314) if mobile else (850,200)
    x=12 if mobile else 18
    p=[f'<path class="rule" d="M{x} 7H{w-x}"/>',text(x,30,"$ fastfetch",12,"dim")]
    values=(("LAPTOP","Samsung"),("CPU","Core 5 120U"),("OS","Arch Linux"),("WM","Hyprland"),
            ("SHELL","ii-p3drovfx"),("TERM / EDITOR","Kitty / Zed"),("LANGUAGES","Python / C / C++ / Shell"))
    if mobile:
        for i,(label,value) in enumerate(values[:6]):
            p+=cell(x+(i%2)*204,43+(i//2)*58,192,label,value)
        p+=cell(x,217,396,*values[-1],14)
        p += [text(x,288,"Student by day. Maintainer by night.",12),text(x,309,"$",12,"dim"),'<rect class="cursor" x="29" y="299" width="6" height="11"/>']
    else:
        for i,(label,value) in enumerate(values[:4]):p+=cell(x+i*207,43,193,label,value)
        for i,(label,value) in enumerate(values[4:]):p+=cell(x+i*207,101,400 if i==2 else 193,label,value)
        p += [text(x,174,"Student by day. Maintainer by night.",13),text(x,196,"$",12,"dim"),'<rect class="cursor" x="35" y="186" width="6" height="11"/>',text(w-x,196,"BUILT FROM SOURCE",10,"dim",True)]
    return svg(w,h,'Samsung / Intel Core 5 120U / Arch Linux / Hyprland / ii-p3drovfx / Kitty / Zed / Python / C / C++ / Shell. Student by day. Maintainer by night.',p)


def link(name,mobile=False):
    p=[text(50,18,f'[{name}]',13).replace('class="phosphor"','class="phosphor" text-anchor="middle"')]
    return svg(100,26,'Open '+name,p,display_width=72 if mobile else 100)


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    for mobile in (False,True):
        suffix='-mobile' if mobile else ''
        for name,builder in [('top',top),('bottom',bottom)]:
            (OUT/f'monitor-{name}{suffix}.svg').write_text(builder(mobile),encoding='utf-8')
        for name in LINKS:
            (OUT/f'monitor-link-{name}{suffix}.svg').write_text(link(name,mobile),encoding='utf-8')
    print('Generated 18 frameless SVG assets for one shared monitor.')


if __name__=='__main__':main()
