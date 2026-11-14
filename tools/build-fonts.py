#!/usr/bin/env python3
"""
Convert purchased OTF/TTF font files into subset woff2 for the web.

Usage:  python3 -I tools/build-fonts.py <source-dir> [--out assets/fonts]

Reads every .otf/.ttf in <source-dir>, subsets each to the characters the
site actually needs, writes woff2 next to the other assets, and prints a
size report plus a ready-to-paste @font-face block.

Subsetting matters: a full OTF carries every glyph the foundry drew,
including scripts the site never renders. Cutting to Latin plus the
punctuation we use typically removes 60-80% of the file.
"""
import argparse, os, sys, glob

try:
    from fontTools.ttLib import TTFont
    from fontTools.subset import Subsetter, Options, parse_unicodes
except ImportError:
    sys.exit("fonttools missing:  pip install --break-system-packages fonttools brotli")

# Characters the site renders. Latin + the punctuation and symbols actually
# used in the markup (curly quotes, en/em dashes, arrows, middots, × ·).
UNICODES = (
    "U+0020-007E,"          # basic latin
    "U+00A0-00FF,"          # latin-1 supplement (accents, ©, ×, ·)
    "U+0100-017F,"          # latin extended-A
    "U+2000-206F,"          # general punctuation (– — ' ' " " … ‹ ›)
    "U+20AC,"               # euro
    "U+2122,U+2190-2193,"   # trademark, arrows
    "U+2212,U+2022"         # minus, bullet
)

WEIGHT_HINTS = [
    ("thin", 100), ("extralight", 200), ("ultralight", 200), ("light", 300),
    ("book", 400), ("regular", 400), ("roman", 400), ("normal", 400),
    ("medium", 500), ("semibold", 600), ("demibold", 600),
    ("extrabold", 800), ("ultrabold", 800), ("black", 900), ("heavy", 900),
    ("bold", 700),   # after extrabold/semibold so it doesn't swallow them
]


def guess(name):
    """Infer weight and style from a filename like SharpGrotesk-SemiBold20.otf"""
    n = name.lower().replace(" ", "").replace("_", "")
    style = "italic" if "italic" in n or "oblique" in n else "normal"
    weight = 400
    for token, w in WEIGHT_HINTS:
        if token in n:
            weight = w
            break
    return weight, style


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src", help="directory holding the purchased .otf/.ttf files")
    ap.add_argument("--out", default="assets/fonts")
    ap.add_argument("--family", default=None, help="override the CSS font-family name")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    files = []
    for ext in ("otf", "ttf", "woff2", "woff"):
        files += glob.glob(os.path.join(args.src, "**", f"*.{ext}"), recursive=True)
    files = sorted(set(files))
    if not files:
        sys.exit(f"no .otf, .ttf, .woff2 or .woff found in {args.src}")

    faces, total_before, total_after = [], 0, 0
    for path in files:
        base = os.path.splitext(os.path.basename(path))[0]
        font = TTFont(path, fontNumber=0)

        family = args.family or font["name"].getDebugName(16) or font["name"].getDebugName(1)
        weight, style = guess(base)

        opts = Options()
        opts.layout_features = ["*"]      # keep kerning, ligatures, figure sets
        opts.name_IDs = ["*"]
        opts.notdef_outline = True
        opts.recalc_bounds = True
        opts.drop_tables = []

        sub = Subsetter(options=opts)
        sub.populate(unicodes=parse_unicodes(UNICODES))
        sub.subset(font)

        font.flavor = "woff2"
        out_name = f"{base.lower().replace(' ', '-')}.woff2"
        out_path = os.path.join(args.out, out_name)
        font.save(out_path)
        font.close()

        before, after = os.path.getsize(path), os.path.getsize(out_path)
        total_before += before
        total_after += after
        faces.append((family, weight, style, out_name))
        print(f"{base:38} {before//1024:>5} KB -> {after//1024:>4} KB woff2   "
              f"weight {weight} {style}")

    print(f"\ntotal {total_before//1024} KB -> {total_after//1024} KB "
          f"({100 - round(total_after / total_before * 100)}% smaller)\n")

    print("/* paste into css/style.css, above :root */")
    for family, weight, style, fn in faces:
        print(f"@font-face{{font-family:'{family}';font-style:{style};"
              f"font-weight:{weight};font-display:swap;"
              f"src:url('/assets/fonts/{fn}') format('woff2')}}")


if __name__ == "__main__":
    main()
