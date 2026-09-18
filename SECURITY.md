# Security Policy

## Scope

This repository is a **portfolio project**. It contains synthetic mock drivers, test fixtures and documentation only. It does **not** contain production code, customer data, credentials, proprietary vendor SDKs, or anything covered by an NDA.

Because of that, the realistic attack surface here is small — but the reporting process below still applies if you spot something.

## Supported versions

Only the latest commit on `main` is supported. There are no released versions or maintenance branches.

| Version | Supported |
|---|---|
| `main` (latest) | ✅ |
| Anything older | ❌ |

## What counts as a security issue here

- Accidental inclusion of real credentials, tokens, API keys or customer data
- Accidental inclusion of proprietary or confidential vendor material
- A dependency with a known critical vulnerability
- A test or script that could cause harm if someone ran it against a real device or network
- Anything in the docs that could mislead an installer into an unsafe configuration

## What does *not* count

- The mock device being "insecure" by design - it's a simulation, not a real device
- Missing authentication on the mock driver - out of scope for a testing demo
- Opinions about platform vendors' own security postures

## How to report

Please **do not** open a public issue for anything sensitive.

Instead, email the maintainer at:
dudai@tester.com

Include:

- A short description of the issue
- Where in the repo it is (file and line if possible)
- Why you think it matters
- Any suggested fix (optional)

If you'd prefer, GitHub's private vulnerability reporting is also enabled on this repo.

## What to expect

This is a personal portfolio repo, so response times are best-effort:

- **Acknowledgment:** within 5 working days
- **Initial assessment:** within 10 working days
- **Fix or explanation:** as soon as reasonably possible

If the report is about accidentally committed sensitive content, it will be treated as **highest priority**.

## Disclosure

Once a fix is in place, a short note will be added crediting the reporter, unless you'd prefer to stay anonymous.

## Dependencies

This project keeps a deliberately tiny dependency list (`pytest`, `pytest-cov`, `ruff`). Dependabot alerts are enabled on the repo.

## Out of scope

- Vulnerabilities in the real Control4, RTI or Crestron platforms — report those to the respective vendor
- Vulnerabilities in third-party emulator or virtual drivers — report those to their authors