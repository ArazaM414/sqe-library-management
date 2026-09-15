import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib_hub.library import validate_isbn

@pytest.mark.parametrize('isbn, is_valid', [
    ("97801323508", False),     # 11 digits
    ("978013235088", False),    # 12 digits
    ("9780132350884", True),    # 13 digits
    ("97801323508841", False),  # 14 digits
    ("978013235088412", False), # 15 digits
])
def test_validate_isbn_bva(isbn, is_valid):
    if not is_valid:
        with pytest.raises(ValueError):
            validate_isbn(isbn)
    else:
        assert validate_isbn(isbn) == is_valid