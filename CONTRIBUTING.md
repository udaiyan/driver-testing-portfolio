# Contributing

Thanks for taking a look. This repo is a portfolio piece demonstrating testing and documentation practice for smart-home / AV drivers, so the contribution rules are intentionally simple and lightweight.

## Ground rules

- **No proprietary or confidential content.** No real vendor code, no customer data, no production credentials, no NDA material. Everything here must be synthetic or publicly documented.
- **Everything must be reproducible.** If you add a step to a guide, it should work from a clean checkout.
- **Documentation is first-class.** Changes to driver behaviour must come with a matching test case or a note explaining why not.
- **Keep it small.** Prefer a short, working example over a clever one.

## Getting started

```bash
git clone https://github.com/<you>/driver-testing-portfolio.git
cd driver-testing-portfolio
make install
make test
```

## Common tasks
| Task | Command |
|---|---|
| Run all tests | `make test` |
| Run unit tests only | `make test-unit` |
| Run integration tests only | `make test-integration` |
| Run regression tests only | `make test-regression` |
| Coverage report | `make coverage` |
| Lint | `make lint` |
| Auto-fix lint | `make lint-fix` |
| Format | `make format` |
| List docs | `make docs` |
| Clean caches | `make clean` |

## Adding a new test case
- Copy manual-tests/test-cases/TEMPLATE.md.
- Name it TC-<PLATFORM>-<NNN>-<short-title>.md (e.g. TC-C4-003-volume-limits.md).
- Fill in preconditions, steps, expected, actual, status.
- If the case can be automated, add it under tests/ and reference the test file name in the Notes section.
- New drivers should start from manual-tests/test-plan-template.md.

## Adding a new mock driver
- Create mocks/<platform>_driver.py subclassing BaseDriver.
- Set platform and keepalive_interval.
- Add a fixture in tests/conftest.py.
- Add an integration test under tests/integration/.
- Add a platform note in docs/platforms.md.

## Adding a bug report
- Copy the format used in manual-tests/bug-reports/BUG-001-rti-idle-disconnect.md.
- Include: severity, environment, reproducibility, steps, expected vs actual, logs, hypothesis.
- If fixed, add a regression test under tests/regression/ and link it from the report.

## Documentation style
- Follow docs/style-guide.md:
- Second person, active voice, short sentences.
- Numbered steps, one action per step.
- code formatting for IPs, ports, file paths.
- Alt text for images; don't rely on colour alone.

## Commit messages
Short and imperative:

```
add TC-C4-003 volume limits case
fix keepalive interval in RTI driver
docs: add troubleshooting video script
```

## Pull request checklist

- [ ] `make lint` passes
- [ ] `make test` passes
- [ ] New behaviour has a test case and/or automated test
- [ ] Docs updated if user-facing behaviour changed
- [ ] No proprietary or confidential content added
## Questions
Open an issue or reach out — see README.md for contact details.

