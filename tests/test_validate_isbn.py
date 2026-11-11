import pytest
from lib_hub.library import validate_isbn

def test_validate_isbn_short():
    with pytest.raises(ValueError):
        validate_isbn("978013235")

def test_validate_isbn_long():
    with pytest.raises(ValueError):
        validate_isbn("978013235088412")

def test_validate_isbn_valid():
    assert validate_isbn("9780132350884") is not None