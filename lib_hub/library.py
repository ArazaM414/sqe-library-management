def fine_tier(days_overdue: int) -> str:
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative.")
    if days_overdue == 0:
        return 'None'
    elif 1 <= days_overdue <= 7:
        return 'Low'
    elif 8 <= days_overdue <= 14:
        return 'Medium'
    elif 15 <= days_overdue <= 30:
        return 'High'
    else:
        return 'Severe'

class Library:
    def __init__(self):
        self.member_loans = {}

    def borrow_book(self, member_id: str, isbn: str):
        current_count = self.member_loans.get(member_id, 0)
        if current_count >= 5:
            raise ValueError("Member has reached maximum borrow limit (5 books).")
        self.member_loans[member_id] = current_count + 1

def validate_isbn(isbn: str) -> bool:
    if not isinstance(isbn, str):
        raise ValueError("ISBN must be a string.")
    if not isbn.isdigit():
        raise ValueError("ISBN must contain digits only.")
    if len(isbn) != 13:
        raise ValueError("ISBN must be exactly 13 digits long.")
    return True