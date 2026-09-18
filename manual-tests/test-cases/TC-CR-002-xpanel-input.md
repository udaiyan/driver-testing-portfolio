# TC-CR-002 — XPanel input switches driver input source

**Platform:** Crestron
**Driver/Device:** Mock driver + SIMPL wrapper
**Severity if fails:** Medium
**Type:** Functional

**Preconditions:**
- TC-CR-001 passed

**Steps:**
1. In XPanel, press **Input 2**.
2. Observe driver feedback.

**Expected result:**
- Driver reports input source = HDMI2.
- No errors.

**Actual result:**
- Pass.