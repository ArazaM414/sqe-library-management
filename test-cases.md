# Test Cases & Execution Log — LibraryHub

| ID | Title | Requirement | Preconditions | Steps | Expected Result | Priority | Type | Status | Notes / Issue Link |
|---|---|---|---|---|---|---|---|---|---|
| **TC-001** | Add book with valid ISBN | REQ-1 | Catalog initialized | 1. Call `add_book()` with new ISBN | Book added successfully | High | Functional | **PASS** | Working fine. |
| **TC-002** | Add duplicate ISBN | REQ-1 | ISBN already in catalog | 1. Call `add_book()` with same ISBN | Raises `ValueError` | High | Negative | **FAIL** | GitHub Issue #2 |
| **TC-003** | Add malformed ISBN | REQ-1 | Catalog initialized | 1. Call `add_book()` with bad ISBN | Raises `ValueError` | Medium | Negative | **PASS** | Validated format. |
| **TC-004** | Borrow when copies available | REQ-2 | Copies > 0 | 1. Call `borrow_book()` | Borrow succeeds | High | Functional | **PASS** | Stock updated. |
| **TC-005** | Borrow when no copies available | REQ-2 | Copies = 0 | 1. Call `borrow_book()` | Raises `ValueError` | High | Negative | **FAIL** | GitHub Issue #1 |
| **TC-006** | Return book on loan | REQ-3 | Book is borrowed | 1. Call `return_book()` | Return succeeds | High | Functional | **PASS** | Stock restored. |
| **TC-007** | Return book not on loan | REQ-3 | Book not borrowed | 1. Call `return_book()` | Raises `ValueError` | Medium | Negative | **PASS** | Action blocked. |
| **TC-008** | Borrow at allowed limit | REQ-4 | Limit = 3 | 1. Call `borrow_book()` for 3rd book | Borrow succeeds | Medium | Functional | **PASS** | Limit reached. |
| **TC-009** | Borrow beyond limit | REQ-4 | Limit = 3, has 3 books | 1. Call `borrow_book()` for 4th book | Raises `ValueError` | High | Negative | **FAIL** | GitHub Issue #3 |
| **TC-010** | Fine for 0 days overdue | REQ-5 | On time return | 1. Call `calculate_fine(0)` | Returns `0.00` | Low | Functional | **PASS** | No fine. |
| **TC-011** | Fine for mid-range overdue | REQ-5 | 4 days overdue | 1. Call `calculate_fine(4)` | Returns `6.00` | Medium | Functional | **PASS** | Correct fine. |
| **TC-012** | Fine at tier boundary | REQ-5 | 8 days overdue | 1. Call `calculate_fine(8)` | Returns `16.00` | Medium | Boundary | **PASS** | Tier rate applied. |