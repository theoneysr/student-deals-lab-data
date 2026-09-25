# Student Deals Lab dataset

This repository turns the public [Student Deals Lab directory](https://studentdealslab.com/tools/) into a small, reusable dataset. It records the tool name, the category shown on the site, the site's current status label, and the canonical research page URL.

The source site checks vendor terms and verification requirements before labeling a deal. Status labels are intentionally cautious: a row can say that an offer is unavailable, institution-dependent, or not publicly verified. Treat every row as a dated research snapshot and re-check the linked page before relying on an offer.

## Files

- `data/student-deals.csv` — 33 directory entries as CSV, reviewed on 2026-08-13 according to the source directory.
- `scripts/filter_deals.py` — dependency-free command-line filter that searches by name, category, or status and prints a Markdown table.

Example:

```bash
python scripts/filter_deals.py --category "AI coding"
python scripts/filter_deals.py --status "Free education plan available"
python scripts/filter_deals.py --query GitHub
```

The dataset is a mirror of public editorial metadata, not an endorsement or a coupon list. Corrections should cite the vendor's current terms and explain the change. For the full research notes and official source links, see [studentdealslab.com](https://studentdealslab.com/).

## License and provenance

The script is MIT-licensed. The CSV is a factual compilation of the public directory metadata; preserve the `source_url` and `last_reviewed` fields when redistributing it. The canonical research and source citations remain on [Student Deals Lab](https://studentdealslab.com/).
