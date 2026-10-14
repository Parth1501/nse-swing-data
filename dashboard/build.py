"""Build the NSE Swing Desk dashboard page.

Usage: python3 build.py <nse-swing-data checkout> <output.html>
Reads the repo's data files, the newest option chain day, the pattern log and the
newest lessons file in /mnt/project-files/nse-swing/reviews, and fills template.html.
"""
import datetime, glob, html, json, os, subprocess, sys

repo, out = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
r = lambda p: open(os.path.join(repo, p), encoding="utf-8").read()
opt = lambda p: r(p) if os.path.exists(os.path.join(repo, p)) else None

ocs = sorted(glob.glob(os.path.join(repo, "data/option_chain/2*.csv")))
lessons = sorted(glob.glob("/mnt/project-files/nse-swing/reviews/lessons_*.md"))
if lessons:
    try:
        lessons_html = subprocess.run(["pandoc", "-f", "gfm", "-t", "html", lessons[-1]], capture_output=True, text=True, check=True).stdout
    except Exception:
        lessons_html = "<pre style='white-space:pre-wrap'>" + html.escape(open(lessons[-1]).read()) + "</pre>"
else:
    lessons_html = "<p>No trade review written yet.</p>"

ist = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5, minutes=30)
oc_latest = opt("data/oc_learning/latest.json")
data = {
    "built_ist": ist.strftime("%d %b %H:%M"),
    "meta": json.loads(r("data/meta.json")),
    "global": json.loads(r("data/global.json")),
    "picks_log": r("data/picks_log.csv"),
    "latest": r("data/latest.csv"),
    "option_chain": {"date": os.path.basename(ocs[-1])[:-4], "csv": open(ocs[-1], encoding="utf-8").read()} if ocs else None,
    "oc_latest": json.loads(oc_latest) if oc_latest else None,
    "oc_library": opt("data/oc_learning/pattern_library.csv"),
    "lessons_html": lessons_html,
    "lessons_name": os.path.basename(lessons[-1]) if lessons else "none",
}
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
page = open(os.path.join(here, "template.html"), encoding="utf-8").read().replace("/*__DATA__*/", blob)
open(out, "w", encoding="utf-8").write(page)
print("built", out, len(page), "bytes; data", data["meta"].get("data_date"), "; option chain", data["option_chain"] and data["option_chain"]["date"])
