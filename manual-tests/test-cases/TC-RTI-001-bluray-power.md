# TC-RTI-001 — RTI Virtual Blu-ray responds to Power On

**Platform:** RTI
**Driver/Device:** RTI Virtual Blu-ray
**Severity if fails:** High
**Type:** Functional

**Preconditions:**
- Integration Designer open
- RTI Virtual Blu-ray driver added to project
- XP processor model selected

**Steps:**
1. Assign Virtual Blu-ray to a zone.
2. Send **Power On** command.
3. Observe feedback.

**Expected result:**
- Virtual Blu-ray reports **Power On**.
- UI feedback updates correctly.

**Actual result:**
- Pass.

**Notes:**
- No physical hardware required.