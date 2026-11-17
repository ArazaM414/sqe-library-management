# Code Review Checklist

## 1. Correctness
- [ ] Does the code perform its intended functionality?
- [ ] Are all conditions and calculations correct?
- [ ] Are edge cases handled properly?

## 2. Testing
- [ ] Are unit tests available for new functionality?
- [ ] Do tests cover normal and invalid inputs?
- [ ] Do all existing tests pass?

## 3. Readability
- [ ] Are variable and function names meaningful?
- [ ] Is the code properly formatted and indented?
- [ ] Are docstrings or comments provided where necessary?

## 4. Design
- [ ] Does the code follow the existing project structure?
- [ ] Is unnecessary code duplication avoided?
- [ ] Are functions small and responsible for clear tasks?

## 5. Risk and Security
- [ ] Are passwords and sensitive information protected?
- [ ] Are errors handled safely?
- [ ] Could the changes negatively affect existing functionality?

## Lessons Learned

The correctness checklist helped identify the most valuable issues because incorrect calculations and missing edge cases can produce unexpected results.

For the next review, I would add a checklist item for checking input validation and compatibility with existing functionality.