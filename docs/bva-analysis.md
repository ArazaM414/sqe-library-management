# Lab 6: Boundary Value Analysis (BVA) Report

## 1. Boundary Analysis for `fine_tier(days)`

| Cut-off Point / Boundary | Value - 1 | Value | Value + 1 | Expected Results (`Value-1`, `Value`, `Value+1`) |
| :--- | :--- | :--- | :--- | :--- |
| **Domain Start (0)** | -1 | 0 | 1 | `ValueError` / Invalid, `'None'`, `'Low'` |
| **Low / Medium (8)** | 7 | 8 | 9 | `'Low'`, `'Medium'`, `'Medium'` |
| **Medium / High (15)** | 14 | 15 | 16 | `'Medium'`, `'High'`, `'High'` |
| **High / Max Tier (31)** | 30 | 31 | 32 | `'High'`, `'Max'`, `'Max'` |

---

## 2. Boundary Analysis for Borrow Limit (`0–5` Active Loans)

* **Rule:** A member can hold up to 5 active loans. Attempting to borrow when at max limit should be rejected.
* **Tested Currently Borrowed Counts:** `4`, `5`, `6`

| Current Books On Loan | Action | Expected Outcome |
| :--- | :--- | :--- |
| **4** (Max - 1) | Borrow 1 more | **Success** (Total becomes 5) |
| **5** (Max) | Borrow 1 more | **Denied / Error** (Limit Reached) |
| **6** (Max + 1) | Borrow 1 more | **Denied / Error** (Exceeds Limit) |

---

## 3. Boundary Analysis for ISBN Length (Target: 13 Digits)

| String Length | Sample Input | Expected Outcome |
| :--- | :--- | :--- |
| **11** (13 - 2) | `"97801323508"` | `False` / Invalid |
| **12** (13 - 1) | `"978013235088"` | `False` / Invalid |
| **13** (Target) | `"9780132350884"` | `True` / Valid |
| **14** (13 + 1) | `"97801323508841"` | `False` / Invalid |
| **15** (13 + 2) | `"978013235088412"` | `False` / Invalid |