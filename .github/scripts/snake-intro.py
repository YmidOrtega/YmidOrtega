"""Prepend a chronological intro to a Platane/snk SVG.

Before the snake starts, the contribution grid writes itself day by day,
oldest first: each day drops into place glowing and cools to its level.
A label counts the days with contributions as they land.
Then the original animation plays untouched.

snk drives everything with CSS keyframes sharing one duration, so the
intro is made room for by stretching that duration and shifting every
keyframe percentage forward. Each cell gets its landing stops merged in.

Usage: python3 snake-intro.py file.svg [file.svg ...]   (edited in place)
"""
import re
import sys

REVEAL_MS = 2400  # first day to last day
DROP_MS = 220     # fall into place
BOUNCE_MS = 160   # settle after landing
COOL_MS = 900     # glow fading to the day's level
HOLD_MS = 400     # full year on screen before the snake moves
INTRO_MS = REVEAL_MS + DROP_MS + COOL_MS + HOLD_MS
DROP_PX = 18

# Glow of a day with / without contributions, and label text, per theme.
THEMES = {
    "dark": {"--cg": "#ffd0d9", "--cgo": "#3d1019", "--ct": "#8b949e"},
    "light": {"--cg": "#ff2d55", "--cgo": "#f6c9d2", "--ct": "#57606a"},
}

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


def theme_of(style):
    r, g, b = (int(re.search(r"--ce:#(\w{6})", style).group(1)[i:i + 2], 16) for i in (0, 2, 4))
    return "dark" if 0.299 * r + 0.587 * g + 0.114 * b < 128 else "light"


def label(landings, total, width):
    """'<n> days shipped', where n ticks up as each contributed day lands."""
    x = width - 16 - 6 - 7.2 * len(" days shipped")  # monospace 12px
    text = f'<text class="t" x="{x + 4:.1f}" y="-12">days shipped</text>'
    style = (
        ".t,.n{font:600 12px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}"
        ".t{fill:var(--ct)}"
        ".n{fill:var(--c4);text-anchor:end;opacity:0;"
        f"animation:none {total}ms step-end infinite}}.n0{{opacity:1}}"
    )
    marks = [0] + landings
    for n, start in enumerate(marks):
        end = marks[n + 1] if n + 1 < len(marks) else None
        stops = f"{pct(start, total)}{{opacity:1}}" + (f"{pct(end, total)}{{opacity:0}}" if end else "")
        if n:
            style += f"@keyframes n{n}{{{stops}}}.n.n{n}{{animation-name:n{n}}}"
        else:  # visible from the loop start until the first landing
            style += f"@keyframes n0{{{pct(end, total)}{{opacity:0}}}}.n.n0{{animation-name:n0}}" if end else ""
        text += f'<text class="n n{n}" x="{x:.1f}" y="-12">{n}</text>'
    return style, text


def add_intro(svg):
    if MARKER in svg:
        return svg

    head, style, body = re.match(r"(.*?<style>)(.*?)(</style>.*)", svg, re.S).groups()
    durations = set(re.findall(r"(\d+)ms", style))
    if len(durations) != 1:
        raise ValueError(f"expected one shared duration, found {durations}")
    loop = int(durations.pop())
    total = loop + INTRO_MS
    width = float(re.search(r'width="([\d.]+)"', head).group(1))

    # Shift the original timeline to start after the intro; 100% stays 100%.
    style = re.sub(
        r"(\d+(?:\.\d+)?)%",
        lambda m: pct(INTRO_MS + float(m.group(1)) / 100 * loop, total),
        style,
    )
    style = style.replace(f"{loop}ms", f"{total}ms")
    colors = "".join(f"{k}:{v};" for k, v in THEMES[theme_of(style)].items())
    style = style.replace(":root{", ":root{" + colors, 1)
    levels = dict(re.findall(r"\.c\.(c[0-9a-z]+)\{fill:(var\(--c\d\))", style))

    # Cells come column by column (one week each), top to bottom (Sun..Sat),
    # but sort explicitly so the order doesn't hinge on snk's output.
    cells = list(re.finditer(r'<rect class="c( c[0-9a-z]+)?" x="([\d.]+)" y="([\d.]+)"', body))
    cells.sort(key=lambda m: (float(m.group(2)), float(m.group(3))))
    step = REVEAL_MS / max(len(cells) - 1, 1)

    renames, landings = {}, []
    for i, cell in enumerate(cells):
        t = i * step
        name = cell.group(1).strip() if cell.group(1) else None
        glow, rest = ("var(--cg)", levels[name]) if name else ("var(--cgo)", "var(--ce)")
        land = t + DROP_MS
        stops = (
            f"0%,{pct(t, total)}{{opacity:0;transform:translateY(-{DROP_PX}px);fill:{glow};"
            "animation-timing-function:cubic-bezier(.55,0,1,.45)}"
            f"{pct(land, total)}{{opacity:1;transform:translateY(0);fill:{glow};"
            "animation-timing-function:ease-out}"
            f"{pct(land + BOUNCE_MS / 2, total)}{{transform:translateY(-3px)}}"
            f"{pct(land + BOUNCE_MS, total)}{{transform:translateY(0)}}"
            f"{pct(land + COOL_MS, total)}{{fill:{rest}}}"
        )
        if name:
            # Contributed day: merge the landing into its existing "eaten" keyframes.
            style = style.replace(f"@keyframes {name}{{", f"@keyframes {name}{{{stops}", 1)
            landings.append(land)
        else:
            # Empty day: never eaten, so it gets keyframes of its own.
            name = "r" + base36(i)
            style += f"@keyframes {name}{{{stops}}}.c.{name}{{animation-name:{name}}}"
            renames[cell.start()] = name

    for start in sorted(renames, reverse=True):
        old = '<rect class="c"'
        body = body[:start] + f'<rect class="c {renames[start]}"' + body[start + len(old):]

    label_style, label_text = label(landings, total, width)
    style += label_style
    body = body.replace("</svg>", label_text + "</svg>", 1)

    return head + style + body.replace("</svg>", MARKER + "</svg>", 1)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path) as f:
            svg = f.read()
        with open(path, "w") as f:
            f.write(add_intro(svg))
