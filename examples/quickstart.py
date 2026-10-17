"""Offline example using the public implementation; see README for evidence scope."""
import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
os.chdir(ROOT)

from economics import annual_net_benefit,break_even_avoided_fraction
print({k:str(v) for k,v in annual_net_benefit(100,5000,.3,50,800,50000).items()})
print({'break_even':str(break_even_avoided_fraction(100,5000,50,800,50000))})
