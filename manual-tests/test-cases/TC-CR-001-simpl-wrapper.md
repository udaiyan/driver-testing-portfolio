# TC-CR-001 — Crestron driver responds through SIMPL wrapper

**Platform:** Crestron
**Driver/Device:** Mock driver + SIMPL wrapper
**Severity if fails:** High
**Type:** Functional

**Preconditions:**
- SIMPL Windows open
- Mock driver loaded
- XPanel available

**Steps:**
1. Create a SIMPL program.
2. Add the wrapper module.
3. Press **Power On** in XPanel.
4. Check driver feedback.

**Expected result:**
- Driver receives the command.
- Feedback returns **Power On**.
- No errors in SIMPL debugger.

**Actual result:**
- Pass.

**Notes:**
- Tested with XPanel simulator.