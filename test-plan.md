# Software Test Plan — LibraryHub (v0.2)

## 1. Introduction
This document outlines the testing strategy, scope, resources, and schedule for the LibraryHub core system. The primary goal is to verify inventory management, borrowing transactions, and overdue fine calculations.

## 2. Test Items
* `Book` class (`book.py`)
* `Library` module (`library.py`)
* Fine calculation logic (`fines.py`)

## 3. Features to be Tested
* Book registration and unique ISBN validation.
* Book search functions.
* Borrowing and returning business rules.
* Overdue fine calculations and tier boundaries.

## 4. Features Not to be Tested
* Graphical User Interface (GUI) / Web Frontend: Explicitly excluded as LibraryHub is currently implemented as a core backend library without a presentation layer.
* Multi-user concurrent access: Out of scope for v0.2 single-threaded execution.

## 5. Testing Approach
Testing will combine automated Python unit tests and manual execution via interactive Python shell scripts. Execution focuses on both positive execution flows and negative boundary condition failures.

## 6. Item Pass/Fail Criteria
* **Pass**: 100% of P0/P1 test cases pass, at least 92% (11/12) of all test cases pass, and 0 Critical or High severity open defects remain in GitHub Issues.
* **Fail**: Any failure in critical transactional logic (e.g., negative inventory or duplicate ISBN acceptance).

## 7. Test Deliverables
* Test Plan (`docs/test-plan.md`)
* Test Cases Specification (`docs/test-cases.md`)
* Requirements Traceability Matrix (`docs/rtm.md`)
* Defect Reports (Filed as GitHub Issues)

## 8. Environmental Needs
* Python 3.10+ runtime environment.
* Git and VS Code.

## 9. Responsibilities & Schedule
* **Tester**: Araza Memon
* **Duration**: 3.0 Hours (Task execution, manual verification, and bug reporting).

## 10. Risks & Contingencies
* **Risk**: Missing formal specification for overdue fine edge cases.
* **Contingency**: Validate fine calculations directly against business logic requirements.