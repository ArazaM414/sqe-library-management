# Selenium Waits & Flakiness Notes (Lab 13)

## Why `WebDriverWait` is Better Than Fixed `sleep`
- UI updates in the browser happen asynchronously after `fetch()` finishes.
- A fixed wait like `time.sleep(0.2)` can finish before the DOM updates, causing flaky failures when responses take longer.
- `WebDriverWait` with `expected_conditions` waits only until the required element or condition appears (up to the timeout), making tests reliable and faster.

## 5-Run Comparison Summary
- **With `WebDriverWait`:** Passed reliably across runs because Selenium waits for the updated row/text to appear.
- **With short fixed delay (`time.sleep(0.2)`) or no wait:** Can fail intermittently if the server/UI takes slightly longer than the fixed pause.