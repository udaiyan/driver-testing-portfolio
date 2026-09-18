# BUG-001 — RTI driver drops connection after idle period

**Severity:** High
**Priority:** High
**Platform:** RTI
**Environment:** Mock RTI driver v0.1, mock device idle timeout 300s
**Reproducibility:** 3/3
**Reported by:** D Udaiyan
**Status:** Fixed and verified

## Summary
The RTI driver reports Offline after a period of inactivity, even though the device is reachable.

## Steps to reproduce
1. Connect the RTI driver.
2. Leave the device idle for 5+ minutes.
3. Send Power On.

## Expected
Command succeeds. Driver stays Online.

## Actual
Driver reports Offline. Power On fails.

## Logs

[12:05:01] Keepalive failed: Idle timeout
[12:05:01] Driver status: Offline


## Root cause hypothesis
The keepalive interval (60s) combined with the driver only sending keepalives on activity meant the device idle timer (300s) could still fire before the next keepalive in low-activity scenarios.

## Fix
- Reduced `RTIDriver.keepalive_interval` to 30s.
- Keepalive loop now runs unconditionally every interval.

## Fix verification
- Re-ran idle scenario for 5 minutes and 30 minutes.
- Driver stayed Online in both.
- Regression tests added: `tests/regression/test_bug_001_idle_disconnect.py`.

## Related artefacts
- Test case: `TC-RTI-002-idle-disconnect.md`
- KB article: `docs/kb-troubleshooting-rti.md`