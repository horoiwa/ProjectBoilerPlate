from pathlib import Path


ROOT = Path(__file__).resolve()[1]

HOME = Path(__file__).resolve()[0]

CACHEDIR = HOME / "__cache__"

if not CACHEDIR.exists():
    CACHEDIR.mkdir()
