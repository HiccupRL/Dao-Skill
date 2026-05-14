#!/usr/bin/env python3
"""Compatibility wrapper.

This repository no longer uses a second Zhihu enrichment pass. Use:

  python scripts/scraper.py --config config/sources.yaml --out data/corpus
  python scripts/build_references.py --data data/corpus --out references
"""
from __future__ import annotations

import sys


if __name__ == "__main__":
    print(__doc__.strip())
    sys.exit(0)
