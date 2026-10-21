#!/usr/bin/env python3
"""Search papers or list citing papers via the Semantic Scholar Graph API (stdlib only).

  find_papers.py search "selective state space" --year 2024- --venue NeurIPS,ICML,ICLR --limit 30
  find_papers.py citing arXiv:2312.00752 --year 2025- --contains "long context,length generalization"

`search` uses the bulk endpoint, whose query syntax supports "quoted phrases", + (AND), | (OR) and - (NOT).
Set S2_API_KEY for higher rate limits; without it requests share a public pool and may be throttled.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.semanticscholar.org/graph/v1"
FIELDS = "title,venue,year,citationCount,externalIds,url,abstract"


def get(path: str, params: dict) -> dict:
    url = f"{API}{path}?{urllib.parse.urlencode({k: v for k, v in params.items() if v})}"
    headers = {"User-Agent": "research-skills/1.0"}
    if os.environ.get("S2_API_KEY"):
        headers["x-api-key"] = os.environ["S2_API_KEY"]
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as err:
            if err.code == 429 and attempt == 5:
                sys.exit("Rate-limited by Semantic Scholar (429) after retries. Wait a minute and retry, "
                         "set S2_API_KEY, or fall back to web search.")
            if err.code not in (429, 500, 502, 503, 504) or attempt == 5:
                sys.exit(f"Semantic Scholar request failed ({err.code}): {url}")
        except urllib.error.URLError:
            if attempt == 5:
                raise
        time.sleep(2 ** (attempt + 1))
    raise AssertionError("unreachable")


def year_ok(paper: dict, year_range: str | None) -> bool:
    if not year_range:
        return True
    if not paper.get("year"):
        return False
    start, _, end = year_range.partition("-")
    return (not start or paper["year"] >= int(start)) and (not end or paper["year"] <= int(end))


def link(paper: dict) -> str:
    ids = paper.get("externalIds") or {}
    if ids.get("ArXiv"):
        return f"https://arxiv.org/abs/{ids['ArXiv']}"
    if ids.get("DOI"):
        return f"https://doi.org/{ids['DOI']}"
    return paper.get("url") or ""


def search(args: argparse.Namespace) -> list[dict]:
    sort = {"citations": "citationCount:desc", "recent": "publicationDate:desc"}[args.sort]
    data = get("/paper/search/bulk", {"query": args.query, "year": args.year, "venue": args.venue, "fields": FIELDS, "sort": sort})
    print(f"Matched {data.get('total', 0)} papers; showing up to {args.limit}.", file=sys.stderr)
    return (data.get("data") or [])[: args.limit]


def citing(args: argparse.Namespace) -> list[dict]:
    keywords = [k.strip().lower() for k in (args.contains or "").split(",") if k.strip()]
    papers, offset = [], 0
    while offset < args.scan:
        page = get(f"/paper/{urllib.parse.quote(args.paper_id, safe=':')}/citations",
                   {"fields": FIELDS, "limit": min(1000, args.scan - offset), "offset": offset})
        batch = [item["citingPaper"] for item in page.get("data") or [] if item.get("citingPaper", {}).get("title")]
        papers.extend(batch)
        if "next" not in page or not batch:
            break
        offset = page["next"]
    print(f"Scanned {len(papers)} citing papers.", file=sys.stderr)
    papers = [p for p in papers if year_ok(p, args.year)]
    if keywords:
        papers = [p for p in papers if any(k in f"{p['title']} {p.get('abstract') or ''}".lower() for k in keywords)]
    papers.sort(key=lambda p: p.get("citationCount") or 0, reverse=True)
    return papers[: args.limit]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    s = sub.add_parser("search", help="keyword search, filtered by year/venue")
    s.add_argument("query")
    s.add_argument("--venue", help="comma-separated, e.g. NeurIPS,ICML,ICLR,CVPR,ACL")
    s.add_argument("--sort", choices=["citations", "recent"], default="citations")

    c = sub.add_parser("citing", help="papers citing a given paper (to check whether a gap was already addressed)")
    c.add_argument("paper_id", help="Semantic Scholar id, arXiv:<id>, DOI:<doi>, ...")
    c.add_argument("--contains", help="comma-separated keywords; keep papers whose title/abstract mention any")
    c.add_argument("--scan", type=int, default=2000, help="max citing papers to scan (default 2000)")

    for p in (s, c):
        p.add_argument("--year", help="e.g. 2024- or 2021-2026")
        p.add_argument("--limit", type=int, default=30)
        p.add_argument("--json", action="store_true", help="print JSON instead of a Markdown table")

    args = parser.parse_args()
    papers = search(args) if args.command == "search" else citing(args)

    if args.json:
        print(json.dumps([{**{k: p.get(k) for k in ("paperId", "title", "venue", "year", "citationCount", "abstract")},
                           "link": link(p)} for p in papers], ensure_ascii=False, indent=2))
        return
    print("| # | Year | Venue | Cites | Title | Link |\n|---|------|-------|-------|-------|------|")
    for i, p in enumerate(papers, 1):
        title = (p.get("title") or "").replace("|", "\\|")
        print(f"| {i} | {p.get('year') or ''} | {p.get('venue') or ''} | {p.get('citationCount') or 0} | {title} | {link(p)} |")


if __name__ == "__main__":
    main()
