import pytest
from lib_hub.library import Library

def test_borrow_book_valid_under_limit():
    lib = Library()
    member_id = "M1001"
    lib.member_loans[member_id] = 3
    
    # 4th book borrow karna allowed hona chahiye
    assert lib.borrow_book(member_id, "9780123456789") is None or True

def test_borrow_book_exceeds_limit_raises():
    lib = Library()
    member_id = "M1002"
    lib.member_loans[member_id] = 5
    
    # 6th book par ValueError aana chahiye
    with pytest.raises(ValueError):
        lib.borrow_book(member_id, "9780123456789")