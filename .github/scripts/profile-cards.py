"""Generate the profile's own SVG cards, in the snake's burgundy palette.

  stats-{en,es}[-dark].svg    last 12 months of real activity + weekly rhythm
  tagline-{en,es}[-dark].svg  the typed tagline

Data comes from the GitHub GraphQL API (GITHUB_TOKEN). Standard library only.
Usage: python3 profile-cards.py <login> <out_dir>
"""
import json
import os
import sys
import urllib.request
from collections import Counter
from html import escape

THEMES = {
    "": {"text": "#1f2328", "muted": "#57606a", "accent": "#800020",
         "ramp": ["#ebedf0", "#f4c1cb", "#e06a82", "#b01e3c", "#800020"]},
    "-dark": {"text": "#e6edf3", "muted": "#8b949e", "accent": "#ff4d6d",
              "ramp": ["#161b22", "#4a0f1e", "#800020", "#b8213f", "#ff4d6d"]},
}
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"

TEXT = {
    "en": {
        "kicker": "LAST 12 MONTHS", "days": "days shipped",
        "contributions": "contributions", "commits": "commits", "prs": "pull requests",
        "longest": "longest streak", "current": "current streak", "unit": "days",
        "code": "of my code", "weekly": "weekly contributions",
        "tagline": ["Components that cooperate. Systems that come alive.",
                    "I design and build scalable backend systems and APIs"],
        "sep": ",",
    },
    "es": {
        "kicker": "ÚLTIMOS 12 MESES", "days": "días activos",
        "contributions": "contribuciones", "commits": "commits", "prs": "pull requests",
        "longest": "racha más larga", "current": "racha actual", "unit": "días",
        "code": "de mi código", "weekly": "contribuciones por semana",
        "tagline": ["Componentes que cooperan. Sistemas que cobran vida.",
                    "Diseño y construyo sistemas backend y APIs escalables."],
        "sep": ".",
    },
}

QUERY = """query($login: String!) { user(login: $login) {
  contributionsCollection {
    totalCommitContributions totalPullRequestContributions
    contributionCalendar { totalContributions weeks { contributionDays { contributionCount } } }
  }
  repositories(ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC, first: 100) {
    nodes { languages(first: 10, orderBy: {field: SIZE, direction: DESC}) { edges { size node { name } } } }
  }
} }"""


def fetch(login):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.load(r)
    if body.get("errors"):
        raise RuntimeError(body["errors"])
    return body["data"]["user"]


def summarize(user):
    c = user["contributionsCollection"]
    weeks = [[d["contributionCount"] for d in w["contributionDays"]] for w in c["contributionCalendar"]["weeks"]]
    days = [n for w in weeks for n in w]
    longest = run = 0
    for n in days:
        run = run + 1 if n else 0
        longest = max(longest, run)
    # Today may still be empty; the streak is alive if it reached yesterday.
    i = len(days) - 1 - (days[-1] == 0)
    current = 0
    while i >= 0 and days[i]:
        current, i = current + 1, i - 1
    langs = Counter()
    for repo in user["repositories"]["nodes"]:
        for e in repo["languages"]["edges"]:
            langs[e["node"]["name"]] += e["size"]
    top, size = langs.most_common(1)[0]
    return {
        "active": sum(1 for n in days if n),
        "contributions": c["contributionCalendar"]["totalContributions"],
        "commits": c["totalCommitContributions"],
        "prs": c["totalPullRequestContributions"],
        "longest": longest, "current": current,
        "lang": top, "lang_pct": round(size / sum(langs.values()) * 100),
        "weekly": [sum(w) for w in weeks],
    }


def num(n, sep):
    return f"{n:,}".replace(",", sep)


def stats_svg(s, t, theme):
    w, h = 840, 204
    stats = [
        (num(s["contributions"], t["sep"]), t["contributions"]),
        (num(s["commits"], t["sep"]), t["commits"]),
        (num(s["prs"], t["sep"]), t["prs"]),
        (f'{s["longest"]} {t["unit"]}', t["longest"]),
        (f'{s["current"]} {t["unit"]}', t["current"]),
        (f'{s["lang"]} {s["lang_pct"]}%', t["code"]),
    ]
    cells = "".join(
        f'<g transform="translate({300 + (i % 3) * 180},{40 + (i // 3) * 46})">'
        f'<text class="v">{escape(v)}</text><text class="l" y="17">{escape(l)}</text></g>'
        for i, (v, l) in enumerate(stats)
    )
    # Weekly rhythm: one bar per week, colored by the grid's own levels,
    # rising left to right on load like the year being written.
    weekly, top = s["weekly"], max(s["weekly"]) or 1
    step, base, hmax = (w - 32) / len(weekly), h - 4, 40
    bw = step - 3
    bars = []
    for i, n in enumerate(weekly):
        level = 0 if not n else min(4, 1 + int(n / top * 4))
        bh = max(2, round(n / top * hmax))
        bars.append(f'<rect class="b" x="{16 + i * step:.1f}" y="{base - bh}" width="{bw:.1f}" height="{bh}" rx="2" '
                    f'fill="{theme["ramp"][level]}" style="animation-delay:{i * 18}ms"/>')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{s['active']} {t['days']}">
<style>
.k{{font:600 11px {MONO};letter-spacing:.16em;fill:{theme['accent']}}}
.big{{font:700 64px {SANS};fill:{theme['text']}}}
.d{{font:600 14px {MONO};fill:{theme['muted']}}}
.v{{font:700 20px {SANS};fill:{theme['text']}}}
.l{{font:12px {MONO};fill:{theme['muted']}}}
.b{{transform-box:fill-box;transform-origin:bottom;animation:rise .5s cubic-bezier(.3,1.4,.6,1) both}}
@keyframes rise{{from{{transform:scaleY(0)}}}}
@media (prefers-reduced-motion:reduce){{.b{{animation:none}}}}
</style>
<text class="k" x="16" y="22">{escape(t['kicker'])}</text>
<text class="big" x="12" y="96">{s['active']}</text>
<text class="d" x="16" y="122">{escape(t['days'])}</text>
{cells}
<text class="l" x="16" y="{base - hmax - 10}">{escape(t['weekly'])}</text>
{''.join(bars)}
</svg>
"""


def tagline_svg(lines, theme):
    w, h = 760, 72
    sizes, ys, cps = (20, 15), (28, 58), 38  # font px, baselines, ms per character
    t, parts, css = 0, [], []
    for i, (line, size, y) in enumerate(zip(lines, sizes, ys)):
        n = len(line)
        width = round(n * size * 0.6)  # textLength pins the width: steps land on characters
        x = (w - width) // 2
        start, end = t, t + n * cps
        parts.append((i, line, size, y, n, width, x, start, end))
        t = end + 500
    total = t + 3500 + 600
    for i, line, size, y, n, width, x, start, end in parts:
        a, b = start / total * 100, end / total * 100
        nxt = parts[i + 1][7] / total * 100 if i + 1 < len(parts) else 100
        css.append(
            f"@keyframes t{i}{{0%,{a:.2f}%{{transform:scaleX(0);animation-timing-function:steps({n},end)}}{b:.2f}%,100%{{transform:scaleX(1)}}}}"
            f"@keyframes m{i}{{0%,{a:.2f}%{{transform:translateX(0);animation-timing-function:steps({n},end)}}{b:.2f}%,100%{{transform:translateX({width}px)}}}}"
            f"@keyframes v{i}{{0%,{a:.2f}%{{visibility:hidden}}{a + .01:.2f}%,{nxt:.2f}%{{visibility:visible}}{nxt + .01:.2f}%,100%{{visibility:hidden}}}}"
            f".r{i}{{transform-box:fill-box;transform-origin:left;animation:t{i} {total}ms linear infinite}}"
            f".c{i}{{animation:m{i} {total}ms linear infinite}}"
            f".c{i} rect{{animation:v{i} {total}ms linear infinite}}"
        )
    fade = (total - 600) / total * 100
    body = "".join(
        f'<clipPath id="k{i}"><rect class="r{i}" x="{x}" y="{y - size}" width="{width}" height="{size + 8}"/></clipPath>'
        f'<text class="s{i}" x="{x}" y="{y}" textLength="{width}" lengthAdjust="spacingAndGlyphs" clip-path="url(#k{i})">{escape(line)}</text>'
        f'<g class="c{i}"><rect x="{x + 1}" y="{y - size + 2}" width="{max(2, size // 8)}" height="{size + 2}" fill="{theme["accent"]}"/></g>'
        for i, line, size, y, n, width, x, start, end in parts
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(' '.join(lines))}">
<style>
.s0{{font:600 20px {MONO};fill:{theme['text']}}}
.s1{{font:15px {MONO};fill:{theme['muted']}}}
{''.join(css)}
.all{{animation:fade {total}ms linear infinite}}
@keyframes fade{{0%,{fade:.2f}%{{opacity:1}}100%{{opacity:0}}}}
@media (prefers-reduced-motion:reduce){{.all,.all *{{animation:none!important}}.all g{{display:none}}}}
</style>
<g class="all">{body}</g>
</svg>
"""


if __name__ == "__main__":
    login, out = sys.argv[1], sys.argv[2]
    s = summarize(fetch(login))
    for lang, t in TEXT.items():
        for suffix, theme in THEMES.items():
            with open(os.path.join(out, f"stats-{lang}{suffix}.svg"), "w") as f:
                f.write(stats_svg(s, t, theme))
            with open(os.path.join(out, f"tagline-{lang}{suffix}.svg"), "w") as f:
                f.write(tagline_svg(t["tagline"], theme))
    print(f"{s['active']} active days, {s['contributions']} contributions, longest streak {s['longest']}")
