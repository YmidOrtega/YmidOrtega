"""Prepend a chronological intro to a Platane/snk SVG.

Before the snake starts, the contribution grid writes itself day by day,
oldest first; then the original animation plays untouched.

snk drives everything with CSS keyframes sharing one duration, so the
intro is made room for by stretching that duration and shifting every
keyframe percentage forward. Each cell gets a pop-in stop at its own time.

Usage: python3 snake-intro.py file.svg [file.svg ...]   (edited in place)
"""
import re
import sys

REVEAL_MS = 2400  # first day to last day
POP_MS = 180      # each cell's pop-in
HOLD_MS = 500     # full year on screen before the snake moves
INTRO_MS = REVEAL_MS + POP_MS + HOLD_MS

MARKER = "<!-- snake-intro -->"


def pct(ms, total):
    return f"{ms / total * 100:.2f}".rstrip("0").rstrip(".") + "%"


def base36(n):
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    out = ""
    while True:
        n, r = divmod(n, 36)
        out = digits[r] + out
        if not n:
            return out


def add_intro(svg):
    if MARKER in svg:
        return svg

    head, style, body = re.match(r"(.*?<style>)(.*?)(</style>.*)", svg, re.S).groups()
    durations = set(re.findall(r"(\d+)ms", style))
    if len(durations) != 1:
        raise ValueError(f"expected one shared duration, found {durations}")
    loop = int(durations.pop())
    total = loop + INTRO_MS

    # Shift the original timeline to start after the intro; 100% stays 100%.
    style = re.sub(
        r"(\d+(?:\.\d+)?)%",
        lambda m: pct(INTRO_MS + float(m.group(1)) / 100 * loop, total),
        style,
    )
    style = style.replace(f"{loop}ms", f"{total}ms")
    style = style.replace(".c{", ".c{transform-box:fill-box;transform-origin:center;", 1)

    # Cells come column by column (one week each), top to bottom (Sun..Sat),
    # but sort explicitly so the order doesn't hinge on snk's output.
    cells = list(re.finditer(r'<rect class="c( c[0-9a-z]+)?" x="([\d.]+)" y="([\d.]+)"', body))
    cells.sort(key=lambda m: (float(m.group(2)), float(m.group(3))))
    step = REVEAL_MS / max(len(cells) - 1, 1)

    renames = {}
    for i, cell in enumerate(cells):
        t = i * step
        hidden = "0%" if i == 0 else f"0%,{pct(t, total)}"
        pop = (
            f"{hidden}{{transform:scale(0)}}"
            f"{pct(t + POP_MS * 0.6, total)}{{transform:scale(1.25)}}"
            f"{pct(t + POP_MS, total)}{{transform:scale(1)}}"
        )
        if cell.group(1):
            # Contributed day: merge the pop into its existing "eaten" keyframes.
            name = cell.group(1).strip()
            style = style.replace(f"@keyframes {name}{{", f"@keyframes {name}{{{pop}", 1)
        else:
            # Empty day: never eaten, so it gets keyframes of its own.
            name = "r" + base36(i)
            style += f"@keyframes {name}{{{pop}}}.c.{name}{{animation-name:{name}}}"
            renames[cell.start()] = name

    for start in sorted(renames, reverse=True):
        old = '<rect class="c"'
        body = body[:start] + f'<rect class="c {renames[start]}"' + body[start + len(old):]

    return head + style + body.replace("</svg>", MARKER + "</svg>", 1)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path) as f:
            svg = f.read()
        with open(path, "w") as f:
            f.write(add_intro(svg))
