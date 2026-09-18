# TC-RTI-002 — RTI driver stays Online after 30 minutes idle

**Platform:** RTI
**Driver/Device:** Mock RTI driver v0.1
**Severity if fails:** High
**Type:** Regression

**Preconditions:**
- Driver connected
- Keepalive enabled

**Steps:**
1. Connect driver.
2. Leave idle for 30 minutes (simulated in automated test).
3. Send Power On.

**Expected result:**
- Driver is still **Online**.
- Power On succeeds.

**Actual result:**
- Pass (after BUG-001 fix).

**Notes:**
- Covered by `tests/regression/test_bug_001_idle_disconnect.py`.