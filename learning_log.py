"""
Keeps data/learning_log.csv: every "Today's learning" topic the morning list has used.

The morning routine reads this file before picking a topic and never reuses one on it.
After sending the email it starts learning_log.yml with the new row (and any rows the file
was missing), and this script appends them. The email's "Learning log:" line is a second copy.

Input (env LEARNING_ENTRIES): one entry per line, or several split by ";;", each
"YYYY-MM-DD|topic|source_url" (source optional). Rows already on file (same date and topic,
ignoring case and punctuation) are skipped, so re-sending the same entry is harmless.
"""
import csv
import os
import re
import sys

LOG = os.path.join("data", "learning_log.csv")
FIELDS = ["date", "topic", "source_url"]


def key(date, topic):
    return date.strip(), re.sub(r"[^a-z0-9]+", " ", topic.lower()).strip()


def main():
    raw = os.environ.get("LEARNING_ENTRIES", "")
    entries = []
    for part in re.split(r";;|\n", raw):
        bits = [b.strip() for b in part.split("|")]
        if len(bits) < 2 or not bits[1]:
            continue
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", bits[0]):
            sys.exit(f"bad date in entry: {part!r}")
        entries.append({"date": bits[0], "topic": bits[1], "source_url": bits[2] if len(bits) > 2 else ""})
    if not entries:
        sys.exit("no entries given")

    rows = []
    if os.path.exists(LOG):
        with open(LOG, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    seen = {key(r["date"], r["topic"]) for r in rows}
    added = 0
    for e in entries:
        if key(e["date"], e["topic"]) in seen:
            continue
        rows.append(e)
        seen.add(key(e["date"], e["topic"]))
        added += 1
    rows.sort(key=lambda r: r["date"])
    with open(LOG, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    print(f"learning log: {added} added, {len(rows)} on file")


if __name__ == "__main__":
    main()
