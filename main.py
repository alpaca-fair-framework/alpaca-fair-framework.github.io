"""Single entry point of the repository: python main.py

The site is written by hand (index.html), so there is nothing to build. The one
step, `check`, tests what a reader would notice if it broke: every local file the
page points to exists, nothing is loaded from another server, the English and the
German half link to the same places, and the links to AMT.engine and AMT.runner
are there. Standard library only; it needs no network and writes no file.

    python main.py            run all steps
    python main.py --list     print the steps and exit
"""
import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGE = ROOT / "index.html"
CSS = ROOT / "assets" / "site.css"

REQUIRED = [
    "https://n4o-rse.github.io/amt-engine/",
    "https://github.com/n4o-rse/amt-engine",
    "https://github.com/n4o-rse/amt-runner",
]


class Page(HTMLParser):
    """Collects local references, external anchors per language and element ids."""

    def __init__(self):
        super().__init__()
        self.local, self.ids, self.stack = [], [], []
        self.loaded_remote = []            # src / stylesheet pointing to another server
        self.anchors = {"en": set(), "de": set(), "all": set()}
        self.lang = None
        self.depth_lang = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.stack.append(tag)
        if tag == "div" and a.get("data-l") in ("en", "de"):
            self.lang, self.depth_lang = a["data-l"], len(self.stack)
        if "id" in a:
            self.ids.append(a["id"])
        ref = a.get("src") or (a.get("href") if tag == "link" else None)
        if ref:
            (self.loaded_remote if re.match(r"(https?:)?//", ref) else self.local).append(ref)
        if tag == "a" and a.get("href"):
            href = a["href"]
            if re.match(r"https?://", href):
                self.anchors["all"].add(href)
                if self.lang:
                    self.anchors[self.lang].add(href)
            elif not href.startswith("#"):
                self.local.append(href)

    def handle_endtag(self, tag):
        if self.lang and tag == "div" and len(self.stack) == self.depth_lang:
            self.lang = self.depth_lang = None
        if tag in self.stack:
            while self.stack.pop() != tag:
                pass


def check():
    problems = []
    page = Page()
    page.feed(PAGE.read_text(encoding="utf-8"))

    for ref in sorted(set(page.local)):
        if not (ROOT / ref.split("#")[0]).exists():
            problems.append(f"index.html: missing local file {ref}")
    for ref in page.loaded_remote:
        problems.append(f"index.html: loads {ref} from another server")
    dup = {i for i in page.ids if page.ids.count(i) > 1}
    for i in sorted(dup):
        problems.append(f"index.html: id '{i}' is used more than once")

    if page.anchors["en"] != page.anchors["de"]:
        only = page.anchors["en"] ^ page.anchors["de"]
        problems.append("index.html: English and German link to different places: " + ", ".join(sorted(only)))
    for url in REQUIRED:
        if url not in page.anchors["all"]:
            problems.append(f"index.html: no link to {url}")

    css = CSS.read_text(encoding="utf-8")
    for ref in sorted(set(re.findall(r'url\("([^"]+)"\)', css))):
        if not (CSS.parent / ref).resolve().exists():
            problems.append(f"assets/site.css: missing file {ref}")
        if re.match(r"(https?:)?//", ref):
            problems.append(f"assets/site.css: loads {ref} from another server")

    print(f"links: {len(page.anchors['all'])} external, {len(set(page.local))} local")
    return problems


STEPS = [("check", "links, assets, language parity, no remote loading", check)]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true", help="print the steps and exit")
    args = ap.parse_args()
    if args.list:
        for name, what, _ in STEPS:
            print(f"{name:8s} {what}")
        return 0
    failed = 0
    for name, what, fn in STEPS:
        problems = fn()
        for p in problems:
            print("FAIL " + p)
        print(f"[{name}] {'ok' if not problems else str(len(problems)) + ' problem(s)'}")
        failed += len(problems)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
