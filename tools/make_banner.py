"""Banner of the profile README, light and dark. Run from the repository root: python3 tools/make_banner.py"""
import random

THEMES = {"light": dict(bg="#f6f8fa", line="#d0d7de", ink="#1f2328", ink2="#59636e", blue="#0969da", soft="#b6d4f7",
                        empty="#e3e8ee", gold="#9a6700"),
          "dark": dict(bg="#0d1117", line="#30363d", ink="#f0f6fc", ink2="#9198a1", blue="#4493f8", soft="#1f4a80",
                       empty="#1c232c", gold="#d29922")}
W, H = 1200, 280
FONT = 'font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif"'


def banner(t):
    rnd = random.Random(7)
    b = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
         f'aria-label="Lijiayu Deng: machine learning for single-cell perturbation biology">',
         f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="{t["bg"]}" stroke="{t["line"]}"/>']
    # a screen as a grid of perturbations: measured (filled), chosen next (ring), not yet measured (pale)
    cols, rows, s, g = 13, 7, 22, 8
    x0 = W - 64 - cols * (s + g) + g
    y0 = (H - (rows * (s + g) - g)) / 2
    for r in range(rows):
        for c in range(cols):
            x, y = x0 + c * (s + g), y0 + r * (s + g)
            fade = min(1.0, (c + 1) / 5)
            u = rnd.random()
            if u < 0.30:
                fill, stroke = t["blue"], "none"
            elif u < 0.48:
                fill, stroke = t["soft"], "none"
            elif u < 0.55:
                fill, stroke = "none", t["gold"]
            else:
                fill, stroke = t["empty"], "none"
            sw = ' stroke-width="2"' if stroke != "none" else ""
            b.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{s}" height="{s}" rx="5" fill="{fill}" stroke="{stroke}"{sw} '
                     f'opacity="{fade:.2f}"/>')
    b += [f'<text x="64" y="112" {FONT} font-size="54" font-weight="700" fill="{t["ink"]}" letter-spacing="-0.5">Lijiayu Deng</text>',
          f'<text x="66" y="156" {FONT} font-size="23" font-weight="500" fill="{t["blue"]}">Machine learning for single-cell perturbation biology</text>',
          f'<text x="66" y="198" {FONT} font-size="17" fill="{t["ink2"]}">The Wen Group · John Curtin School of Medical Research</text>',
          f'<text x="66" y="224" {FONT} font-size="17" fill="{t["ink2"]}">The Australian National University · Canberra</text>',
          '</svg>']
    return "\n".join(b)


for k, t in THEMES.items():
    open(f"assets/banner_{k}.svg", "w").write(banner(t) + "\n")
