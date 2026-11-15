import sys, re, urllib.request
pages = ["index.html", "resume/index.html", "work/nyando-flood-ai/index.html", "404.html"]
forbidden = ["jameskoero.dev", "lorem ipsum"]
bad = 0
txt = {}
for p in pages:
    try: txt[p] = open(p, encoding="utf-8").read()
    except FileNotFoundError: print("MISSING", p); bad += 1
for p, t in txt.items():
    for f in forbidden:
        if f in t: print("FORBIDDEN", f, "in", p); bad += 1
if "0.971" in txt.get("work/nyando-flood-ai/index.html", "") and "mappable" not in txt["work/nyando-flood-ai/index.html"]:
    print("0.971 shown without frame label"); bad += 1
if "--links" in sys.argv:
    urls = sorted({u for t in txt.values() for u in re.findall(r'https?://[^\s"\'<>)]+', t) if "fonts.g" not in u and "schema.org" not in u})
    for u in urls:
        try: c = urllib.request.urlopen(urllib.request.Request(u, method="HEAD", headers={"User-Agent": "Mozilla/5.0"}), timeout=15).status
        except Exception as e: c = str(e)[:40]
        if c not in (200, 301, 302): print("LINK?", c, u)
print("PASS" if not bad else "FAIL")
sys.exit(1 if bad else 0)
