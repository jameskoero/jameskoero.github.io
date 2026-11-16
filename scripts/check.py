import os, sys, re, urllib.request, urllib.error
cases = ("nyando-flood-ai", "afrisalaries", "segmentiq", "churchos")
pages = ["index.html", "resume/index.html", "404.html", "work/index.html", "about/index.html", "experience/index.html", "research/index.html", "skills/index.html", "contact/index.html"] + ["work/%s/index.html" % s for s in cases]
forbidden = ["jameskoero.dev", "lorem ipsum", "ministry", "migosi", "bishop", "mwamburi", "an machine learning"]
bad = 0
txt = {}
for p in pages:
    try: txt[p] = open(p, encoding="utf-8").read()
    except FileNotFoundError: print("MISSING", p); bad += 1
for p, t in txt.items():
    for f in forbidden:
        if f in t.lower(): print("FORBIDDEN", f, "in", p); bad += 1
ny = txt.get("work/nyando-flood-ai/index.html", "")
if "0.971" in ny and "mappable" not in ny:
    print("0.971 shown without frame label"); bad += 1
if "0.971" in txt.get("research/index.html", "") and "mappable" not in txt["research/index.html"]:
    print("0.971 shown without frame label on research"); bad += 1
# structure of the pages this pack owns
own = [p for p in txt if p not in ("index.html", "resume/index.html", "404.html")]
for p in own:
    t = txt[p]
    for need in ('<title>', 'rel="canonical"', 'name="description"', '<main'):
        if need not in t: print("NO", need, "in", p); bad += 1
    if t.count("<h1>") != 1: print("h1 count", t.count("<h1>"), "in", p); bad += 1
# internal links must exist
def exists(path):
    path = path.split("#")[0].split("?")[0]
    if not path: return True
    f = path.lstrip("/")
    if f == "" or f.endswith("/"): f += "index.html"
    return os.path.exists(f)
for s in cases:
    t = txt.get("work/%s/index.html" % s, "")
    if "<svg" not in t and "/assets/diagrams/" not in t: print("no diagram in", s); bad += 1
    if '<h2 id="' not in t: print("no h2 ids in", s); bad += 1
    if "What I would do next" not in t: print("no next steps in", s); bad += 1
for p, t in txt.items():
    for src in re.findall(r'<img [^>]*src="(/[^"]+)"', t):
        if not exists(src): print("MISSING image", src, "in", p); bad += 1
    for tag in re.findall(r"<img [^>]*>", t):
        if 'alt="' not in tag: print("img without alt in", p); bad += 1
    for w in ("pgvector", "ten years", "10 years", "10+ years", "onyango"):
        if w in t.lower(): print("WARN claim to review:", w, "in", p)
    if re.search(r"\baws\b", t.lower()): print("WARN claim to review: aws in", p)
for p in own:
    for h in re.findall(r'href="(/[^"]*)"', txt[p]):
        if not exists(h): print("BROKEN internal link", h, "in", p); bad += 1
try:
    sm = open("sitemap.xml", encoding="utf-8").read()
    for u in re.findall(r"<loc>https://jameskoero\.github\.io([^<]*)</loc>", sm):
        if not exists(u): print("SITEMAP URL has no file", u); bad += 1
except FileNotFoundError: print("MISSING sitemap.xml"); bad += 1
if "--links" in sys.argv:
    urls = sorted({u for t in txt.values() for u in re.findall(r'https?://[^\s"\'<>)]+', t) if "fonts.g" not in u and "schema.org" not in u})
    for u in urls:
        try: c = urllib.request.urlopen(urllib.request.Request(u, method="HEAD", headers={"User-Agent": "Mozilla/5.0"}), timeout=15).status
        except urllib.error.HTTPError as e: c = e.code
        except Exception as e: c = str(e)[:40]
        if "doi.org" in u and c == 403: continue
        if c not in (200, 301, 302): print("LINK?", c, u)
print("PASS" if not bad else "FAIL")
sys.exit(1 if bad else 0)
