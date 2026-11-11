# Code Review Checklist — GradeBook

## 1. Correctness
- [ ] Does the code produce the expected result for valid inputs?
- [ ] Are boundary cases handled correctly, such as empty data or a score of 0 or 100?
- [ ] Are invalid scores rejected instead of being accepted silently?

## 2. Tests
- [ ] Are tests provided for the new or modified functionality?
- [ ] Do tests cover normal cases, invalid inputs, and edge cases?
- [ ] Do tests verify the expected behaviour rather than simply copying the implementation logic?

## 3. Readability
- [ ] Are variable and function names clear and meaningful?
- [ ] Is the code formatted consistently and easy to follow?
- [ ] Are docstrings or comments provided where they clarify non-obvious behaviour?

## 4. Design
- [ ] Does the change fit the existing GradeBook structure?
- [ ] Is unnecessary duplicated code avoided?
- [ ] Does each function have a clear, focused responsibility?

## 5. Risk
- [ ] Can invalid input cause a crash or an incorrect result?
- [ ] Could the change break existing functionality?
- [ ] Could the change cause unnecessary performance or security problems?

## Lessons Learned

- **Most valuable checklist item:** Checking boundary cases, because values at the limits can reveal logic errors that ordinary tests miss.
- **Checklist item to add next time:** Check whether error messages clearly explain how invalid input should be corrected.
