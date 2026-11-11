# Lab 11: Automated Test Coverage Report

## Baseline Coverage Summary
- **Target Module:** `lib_hub`
- **Initial Line Coverage:** 76%
- **Initial Branch Coverage:** (jo terminal ya html report mein show ho)
- **Missing Lines:** `17, 20-23, 27, 29` in `lib_hub/library.py`
## Coverage vs. Quality Discussion
High line coverage does not ensure test quality. A test can execute 100% of statements without proper assertions (e.g. checking only that no exception was raised), creating a false sense of security (a coverage trap). Quality requires asserting exact return values, state transitions, and exception properties.
```