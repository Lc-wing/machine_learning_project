#!/usr/bin/env python3
"""Pull Limitations / Discussion / Future Work / Conclusion sections out of arXiv papers (stdlib only).

  extract_sections.py 2312.00752 2401.10166
  extract_sections.py https://arxiv.org/abs/2312.00752 --pattern "limitation|failure" --max-chars 4000

Reads arXiv's HTML rendering (https://arxiv.org/html/<id>). Papers without one are reported so the
PDF can be read instead. Math is kept as its LaTeX source between $...$.
"""
from __future__ import annotations

import argparse
import json
import re
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser

DEFAULT_PATTERN = (
    r"limitation|discussion|future (work|direction|research)|open (problem|question|challenge)"
    r"|conclusion|broader impact|failure"
)
STOP_HEADING = re.compile(r"acknowledg|references|bibliography", re.I)
ARXIV_ID = re.compile(r"(\d{4}\.\d{4,5}(?:v\d+)?|[a-z-]+(?:\.[A-Z]{2})?/\d{7}(?:v\d+)?)")
SKIP_TAGS = {"script", "style", "nav", "header", "footer", "button"}
BLOCK_TAGS = {"p", "div", "li", "section", "table", "tr", "figcaption", "blockquote", "br"}


class LatexmlParser(HTMLParser):
    """Flattens arXiv's LaTeXML HTML into ("heading", level, text) and ("text", text) items."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.items: list[tuple] = []
        self._buf: list[str] = []
        self._heading: tuple[str, int, str] | None = None
        self._skip: list[str] = []
        self._math_depth = 0

    def _flush(self) -> None:
        text = re.sub(r"\s+", " ", "".join(self._buf)).strip()
        self._buf = []
        if text and self._heading is None:
            self.items.append(("text", text))

    def handle_starttag(self, tag: str, attrs: list) -> None:
        attrs = dict(attrs)
        if self._skip:
            if tag == self._skip[-1]:
                self._skip.append(tag)
            return
        if tag in SKIP_TAGS:
            self._skip.append(tag)
            return
        if tag == "math":
            if self._math_depth == 0:
                self._buf.append(f"${attrs.get('alttext', '')}$")
            self._math_depth += 1
            return
        if self._math_depth:
            return
        classes = attrs.get("class") or ""
        if re.fullmatch(r"h[1-6]", tag) and "ltx_title" in classes and "ltx_runin" not in classes:
            self._flush()
            kind = "document" if "ltx_title_document" in classes else "section"
            self._heading = (tag, int(tag[1]), kind)
        elif tag in BLOCK_TAGS:
            self._flush()

    def handle_endtag(self, tag: str) -> None:
        if self._skip:
            if tag == self._skip[-1]:
                self._skip.pop()
            return
        if tag == "math":
            self._math_depth = max(0, self._math_depth - 1)
            return
        if self._math_depth:
            return
        if self._heading and tag == self._heading[0]:
            text = re.sub(r"\s+", " ", "".join(self._buf)).strip()
            _, level, kind = self._heading
            self._buf, self._heading = [], None
            if kind == "document":
                self.title = text
            elif text:
                self.items.append(("heading", level, text))
        elif tag in BLOCK_TAGS:
            self._flush()

    def handle_data(self, data: str) -> None:
        if not self._skip and not self._math_depth:
            self._buf.append(data)


def extract(items: list[tuple], pattern: re.Pattern, max_chars: int) -> list[dict]:
    """A matching heading collects everything up to the next heading at the same or a higher level,
    or up to an Acknowledgments/References heading."""
    sections: list[dict] = []
    current: dict | None = None
    for item in items:
        if item[0] == "heading":
            _, level, text = item
            if STOP_HEADING.search(text):
                current = None
                continue
            if current and level > current["level"]:
                current["parts"].append(f"[{text}]")
                continue
            current = {"heading": text, "level": level, "parts": []} if pattern.search(text) else None
            if current:
                sections.append(current)
        elif current:
            current["parts"].append(item[1])
    for section in sections:
        text = "\n\n".join(section.pop("parts"))
        section.pop("level")
        if len(text) > max_chars:
            text = f"{text[:max_chars]} …[truncated; {len(text)} chars total, raise --max-chars to see more]"
        section["text"] = text
    return sections


def fetch(arxiv_id: str) -> str | None:
    request = urllib.request.Request(f"https://arxiv.org/html/{arxiv_id}", headers={"User-Agent": "research-skills/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=60) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            return html if "ltx_page_main" in html or "ltx_document" in html else None
        except urllib.error.HTTPError as err:
            if err.code == 404:
                return None
            if attempt == 2:
                raise
        except urllib.error.URLError:
            if attempt == 2:
                raise
        time.sleep(3 * (attempt + 1))
    return None


def process(raw: str, pattern: re.Pattern, max_chars: int) -> dict:
    match = ARXIV_ID.search(raw)
    if not match:
        return {"input": raw, "error": "not an arXiv id or URL"}
    arxiv_id = match.group(1)
    result = {"id": arxiv_id, "abs": f"https://arxiv.org/abs/{arxiv_id}"}
    html = fetch(arxiv_id)
    if html is None:
        return {**result, "error": f"no HTML version; read the PDF instead: https://arxiv.org/pdf/{arxiv_id}"}
    parser = LatexmlParser()
    parser.feed(html)
    parser.close()
    result["title"] = parser.title
    result["sections"] = extract(parser.items, pattern, max_chars)
    if not result["sections"]:
        result["headings"] = [item[2] for item in parser.items if item[0] == "heading" and item[1] <= 3]
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("papers", nargs="+", help="arXiv ids or arxiv.org URLs")
    parser.add_argument("--pattern", default=DEFAULT_PATTERN, help="case-insensitive regex matched against headings")
    parser.add_argument("--max-chars", type=int, default=6000, help="truncate each section (default 6000)")
    parser.add_argument("--json", action="store_true", help="print JSON instead of Markdown")
    args = parser.parse_args()

    pattern = re.compile(args.pattern, re.I)
    results = []
    for i, raw in enumerate(args.papers):
        if i:
            time.sleep(1)
        results.append(process(raw, pattern, args.max_chars))

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return
    for r in results:
        print(f"## {r.get('title') or r.get('id') or r['input']}\n{r.get('abs', '')}\n")
        if "error" in r:
            print(f"> {r['error']}\n")
            continue
        if not r["sections"]:
            print("> No heading matched the pattern. Top-level headings: " + "; ".join(r["headings"]) + "\n")
        for section in r["sections"]:
            print(f"### {section['heading']}\n\n{section['text']}\n")


if __name__ == "__main__":
    main()
