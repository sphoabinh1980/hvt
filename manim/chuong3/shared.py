"""Dùng lại khung trình bày của Chương 1 (common.py, list_cards, line_box, bar_chart)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "chuong1"))

from common import *  # noqa: E402,F401,F403
from bai1 import list_cards, line_box  # noqa: E402,F401
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "chuong2"))
from bai4 import Table2D  # noqa: E402,F401
