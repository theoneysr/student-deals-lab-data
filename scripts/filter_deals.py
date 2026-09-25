#!/usr/bin/env python3
"""Filter the Student Deals Lab CSV and print a small Markdown table."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", help="case-insensitive text search across name, category, and status")
    parser.add_argument("--category", help="exact category match")
    parser.add_argument("--status", help="case-insensitive status substring")
    parser.add_argument("--csv", type=Path, default=Path(__file__).parents[1] / "data" / "student-deals.csv")
    args = parser.parse_args()

    with args.csv.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    def matches(row: dict[str, str]) -> bool:
        if args.query:
            haystack = " ".join(row[field] for field in ("name", "category", "status")).lower()
            if args.query.lower() not in haystack:
                return False
        if args.category and row["category"].lower() != args.category.lower():
            return False
        if args.status and args.status.lower() not in row["status"].lower():
            return False
        return True

    selected = [row for row in rows if matches(row)]
    print("| Name | Category | Status | Source |")
    print("| --- | --- | --- | --- |")
    for row in selected:
        print(f"| {row['name']} | {row['category']} | {row['status']} | [{row['source_url']}]({row['source_url']}) |")
    print(f"\n{len(selected)} result(s) from {len(rows)} rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
