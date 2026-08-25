# Defect Triage Log & Prioritization Strategy

## Bug Prioritization Order
1. **Issue #1**: Crash when issuing book to student with maximum limit reached
   - **Reason**: Critical functionality crash during standard daily operations. Must fix first.
2. **Issue #3**: Duplicate ISBN allowed when adding new book
   - **Reason**: High data integrity risk; duplicate records corrupt inventory records.
3. **Issue #2**: Negative fine amount allowed for overdue books
   - **Reason**: Financial calculation bug affecting system logic.

---

## Trade-off Analysis (Severity vs Priority)

1. **Issue #4 (Case-Sensitive Book Search)**:
   - **Severity**: Low (Functional inconvenience; workarounds exist by typing exact case).
   - **Priority**: P3 (Deferred: User can still find books if exact title case is used).

2. **Issue #5 (Leap Year Return Date Calculation)**:
   - **Severity**: Low (1-day calculation variance in rare edge case).
   - **Priority**: P3 (Deferred: Business impact is minimal and only applies to leap years).

---

## Deferred Issues (Wontfix for Current Sprint)
- **Issue #4**: Deferred due to low search impact.
- **Issue #5**: Deferred due to rare edge-case occurrence.