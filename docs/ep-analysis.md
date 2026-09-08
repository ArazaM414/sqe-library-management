# Equivalence Partitioning (EP) Analysis Report - LibraryHub

## Task 1 — Equivalence Class Analysis Tables

### 1. Fine Tier Logic (`days_overdue`)
| Partition Type | Equivalence Class / Range | Representative Value | Expected Behavior |
| :--- | :--- | :--- | :--- |
| Invalid | `< 0` | `-3` | `ValueError` |
| Valid | `0` | `0` | `'None'` |
| Valid | `1 - 7` | `4` | `'Low'` |
| Valid | `8 - 14` | `10` | `'Medium'` |
| Valid | `15 - 30` | `20` | `'High'` |
| Valid | `31+` | `45` | `'Severe'` |

---

### 2. Books on Loan Limit (`current_loans`)
| Partition Type | Equivalence Class | Representative State / Value | Expected Behavior |
| :--- | :--- | :--- | :--- |
| Valid | `0 to 5 books` | Member with 3 books borrowing 4th | Allowed (Returns `True`) |
| Invalid | `6+ books` | Member with 5 books borrowing 6th | `ValueError` (Limit Exceeded) |

---

### 3. ISBN Field Validation (`isbn`)
| Partition Type | Equivalence Class | Representative Input | Expected Behavior |
| :--- | :--- | :--- | :--- |
| Valid | Exactly 13 numeric digits | `"9780321125217"` | Allowed (Returns `True`) |
| Invalid | Empty string | `""` | `ValueError` |
| Invalid | Incorrect length (e.g., 12 digits) | `"123456789012"` | `ValueError` |
| Invalid | Non-numeric characters / symbols | `"978032112521X"` | `ValueError` |

---

## Limitations of Equivalence Partitioning (EP)

> **Note on Boundary Blind Spot:**  
> Equivalence Partitioning selects one representative value from the interior of each partition to minimize test redundancy. Consequently, EP alone often fails to detect **off-by-one errors** occurring at the boundary edges (e.g., passing `7` vs `8` for fine tiers, or `5` vs `6` for borrow limits). To address this gap, EP must be complemented with **Boundary Value Analysis (BVA)** (as covered in Lab 6).

---

## Task 4 — Pytest Execution Summary

```text
============================= test session starts ==============================
platform win32 -- Python 3.14.x, pytest-8.x.x, pluggy-1.x.x
rootdir: C:\Users\New Ameen Computer\sqe-library-management
collected 12 items

tests\test_borrow_limit.py ..                                            [ 16%]
tests\test_fine_tier.py ......                                          [ 66%]
tests\test_validate_isbn.py ....                                        [100%]

============================== 12 passed in 0.04s ==============================