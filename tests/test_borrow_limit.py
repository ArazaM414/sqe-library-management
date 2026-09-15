import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.mark.parametrize('current_loans, expected_can_borrow', [
    (4, True),   # 4 books on loan (Max - 1) -> Allowed
    (5, False),  # 5 books on loan (Max limit) -> Denied
    (6, False),  # 6 books on loan (Max + 1) -> Denied
])
def test_borrow_limit_bva(current_loans, expected_can_borrow):
    MAX_LOANS = 5
    can_borrow = current_loans < MAX_LOANS
    assert can_borrow == expected_can_borrow