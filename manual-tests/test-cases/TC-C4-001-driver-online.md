# TC-C4-001 — Control4 driver reports Online with valid IP

**Platform:** Control4
**Driver/Device:** Mock Control4 driver v0.1 + Mock device at 192.168.1.50
**Severity if fails:** Critical
**Type:** Functional

**Preconditions:**
- Mock device is reachable
- Driver loaded

**Steps:**
1. Add the mock driver.
2. Set IP to `192.168.1.50`.
3. Set port to `5000`.
4. Apply settings.

**Expected result:**
- Driver status changes to **Online**.
- No errors in the log.

**Actual result:**
- Pass.

**Notes:**
- Repeated 3 times.
- Covered by `tests/integration/test_control4_flow.py`.