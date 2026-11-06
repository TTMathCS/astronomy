# Rewrites the Books menu in mkdocs.yml from the folders in docs/books (python3 tools/nav.py).
# A book shows up once its folder has an index.md; chapters are the NN-Name.md files, in order.
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS = [
    ("night-sky", "The night sky"),
    ("light-and-telescopes", "Light and telescopes"),
    ("orbits", "Orbits"),
    ("solar-system", "The solar system"),
    ("mars", "Mars"),
    ("sun", "The Sun"),
    ("stars", "Stars"),
    ("galaxies", "Galaxies"),
    ("cosmology", "Cosmology"),
    ("exoplanets", "Exoplanets and life"),
    ("history", "History of astronomy"),
]

out = ["  # books: start", "  - Books:", "      - books/index.md"]
for d, t in BOOKS:
    p = os.path.join(ROOT, "docs/books", d)
    if not os.path.exists(os.path.join(p, "index.md")):
        continue
    out += [f'      - "{t}":', f"          - books/{d}/index.md"]
    for f in sorted(os.listdir(p)):
        if re.match(r"\d\d-.*\.md$", f):
            out.append(f"          - books/{d}/{f}")
    if os.path.exists(os.path.join(p, "Glossary.md")):
        out.append(f"          - books/{d}/Glossary.md")
out.append("  # books: end")

y = os.path.join(ROOT, "mkdocs.yml")
s = open(y).read()
a, b = s.index("  # books: start"), s.index("  # books: end") + len("  # books: end")
open(y, "w").write(s[:a] + "\n".join(out) + s[b:])
print(len(out) - 4, "menu lines")
