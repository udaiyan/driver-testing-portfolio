# Test Plan — Mock Smart-Home/AV Drivers

**Author:** [Your Name]
**Version:** 1.0
**Scope:** Manual and automated testing of mock drivers for Control4, RTI and Crestron.

## 1. Objective

Verify that each mock driver can be added, configured, controlled and removed in a simulated environment, and that common failure modes are handled gracefully.

## 2. In scope

- Connection / disconnection
- Power On / Power Off
- Volume control
- Keepalive and idle-disconnect behaviour
- Error handling for unreachable devices and unknown commands
- Installer-facing documentation

## 3. Out of scope

- Real hardware, production credentials, proprietary Janus code
- Performance/load testing
- Security testing

## 4. Test approach

| Type | Where | Purpose |
|---|---|---|
| Manual functional | `manual-tests/test-cases/` | Confirm behaviour matches spec |
| Exploratory | `manual-tests/exploratory-charters/` | Find edge cases not in test cases |
| Automated unit | `tests/unit/` | Fast feedback on driver logic |
| Automated integration | `tests/integration/` | End-to-end flow per platform |
| Regression | `tests/regression/` | Verify fixes stay fixed |

## 5. Environments

- Python 3.12, pytest 8.x
- Mock device with injectable clock
- Control4: DriverEditor / Composer Pro (illustrative only)
- RTI: Integration Designer with RTI Virtual Blu-ray
- Crestron: SIMPL Windows + XPanel

## 6. Entry criteria

- Mock device and drivers import cleanly
- `pytest` runs without collection errors

## 7. Exit criteria

- All manual test cases executed
- All automated tests pass
- No open high-severity bugs
- Test summary report published

## 8. Risks

- No real hardware available → mitigated by virtual drivers and injectable clock
- Platform SDKs not publicly runnable → documented as illustrative

## 9. Deliverables

- Test cases
- Bug reports
- Test summary report
- Installer guide, KB articles, video scripts