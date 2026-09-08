import pytest
from lib_hub.library import validate_isbn

def test_validate_isbn_valid_class():
    assert validate_isbn("9780321125217") is True

def test_validate_isbn_empty_string_raises():
    with pytest.raises(ValueError):
        validate_isbn("")

def test_validate_isbn_too_short_raises():
    with pytest.raises(ValueError):
        validate_isbn("123456789012")

def test_validate_isbn_contains_letters_raises():
    with pytest.raises(ValueError):
        validate_isbn("978032112521X")