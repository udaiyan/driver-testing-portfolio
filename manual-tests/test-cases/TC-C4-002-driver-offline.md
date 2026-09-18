# TC-C4-002 — Control4 driver reports Offline with unreachable device

**Platform:** Control4
**Driver/Device:** Mock Control4 driver v0.1 + unreachable device
**Severity if fails:** High
**Type:** Negative

**Preconditions:**
- Mock device is unreachable

**Steps:**
1. Add the mock driver.
2. Set IP to `192.168.1.50`.
3. Apply settings.

**Expected result:**
- Driver status shows **Offline**.
- Log shows a clear "no response" warning.
- No crash or unhandled exception.

**Actual result:**
- Pass.

**Notes:**
- Covered by `tests/unit/test_connection.py`.