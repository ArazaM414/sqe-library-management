import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib_hub.library import fine_tier

@pytest.mark.parametrize('days, expected', [
    (-1, "Invalid"),
    (0, "None"),
    (1, "Low"),
    (7, "Low"),
    (8, "Medium"),
    (9, "Medium"),
    (14, "Medium"),
    (15, "High"),
    (16, "High"),
    (30, "High"),
    (31, "Severe"),
    (32, "Severe"),
])
def test_fine_tier_bva(days, expected):
    if expected == "Invalid":
        with pytest.raises(ValueError):
            fine_tier(days)
    else:
        assert fine_tier(days) == expected