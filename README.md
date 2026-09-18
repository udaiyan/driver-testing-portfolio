# Driver Testing Portfolio — Control4, RTI, Crestron

> Mock/synthetic examples only. No confidential or proprietary information.

Hi, DarrenU here. This repo shows how I approach **manual and automated testing**, **technical support** and **technical authoring** for smart-home / AV drivers and integrations.

It's built around the Janus Technology Test Engineer & Technical Author role: testing drivers/integrations, investigating issues, verifying fixes, supporting installers, and producing guides, KB articles and setup videos.

## Repo conventions

- Developer tasks: `make help`
- Contribution rules: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Linting: `make lint` (ruff)
- Full suite: `make test`

## How this maps to the job spec

| Job spec requirement | Where to look |
|---|---|
| Testing drivers/integrations across Control4, RTI, Crestron | `mocks/`, `tests/integration/`, `manual-tests/test-cases/` |
| Investigating issues, analysing results, verifying fixes | `manual-tests/bug-reports/`, `tests/regression/` |
| Supporting installers/integrators | `docs/kb-*.md`, `docs/installer-guide.md` |
| Creating installer/user guides and KB content | `docs/` |
| Producing setup/troubleshooting videos | `docs/video-scripts/` |
| Software testing / QA | `tests/`, `manual-tests/` |
| Communication and attention to detail | `docs/style-guide.md`, whole repo |

## Manual testing

- [Test plan (filled-in example)](manual-tests/test-plan.md)
- [Generic test plan template](manual-tests/test-plan-template.md)
- [Test case template](manual-tests/test-cases/TEMPLATE.md)
- [Control4 online test](manual-tests/test-cases/TC-C4-001-driver-online.md)
- [RTI idle-disconnect bug report](manual-tests/bug-reports/BUG-001-rti-idle-disconnect.md)
- [Exploratory charter](manual-tests/exploratory-charters/charter-001-driver-resilience.md)
- [Test summary report](manual-tests/test-summary-report.md)

## Automated testing

- Unit tests: `tests/unit/`
- Integration tests (per platform): `tests/integration/`
- Regression test for BUG-001: `tests/regression/`

Run:

```bash
pip install -r requirements.txt
pytest -v
```
## Documentation
* Installer guide
* User guide
* KB: Control4 offline driver
* KB: RTI idle disconnect
* Video script: setup
* Video script: troubleshooting

## Contact
D Udaiyan· https://github.com/udaiyan

## License
Released under the MIT License.

## Security
This repo contains synthetic examples only — no proprietary code, credentials or customer data. See SECURITY.md for the reporting process.

## Repo hygiene
- Contributing rules: CONTRIBUTING.md
- Security policy: SECURITY.md
- Developer tasks: make help
- CI: .github/workflows/ci.yml

<sub>Portfolio project by D Udaiyan · All examples are mock/synthetic and intended for demonstration only.</sub>


