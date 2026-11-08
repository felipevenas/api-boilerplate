---
name: Bug Report
about: Create a report to help us identify and fix problems in the boilerplate
title: '[BUG] '
labels: bug
assignees: ''
---

## Problem Description

A clear and concise description of the bug.

## Steps to Reproduce

1. Configure `.env` and start MySQL with `docker compose up -d`.
2. Start the API with `uvicorn app.main:app --reload`.
3. Call the endpoint or execute the flow `...`
4. Send the payload `...`
5. Observe the returned status, response body, or application log.

## Expected Behavior

A clear and concise description of what you expected to happen.

## Actual Behavior

What actually happened, including the HTTP status, response body, and any traceback. Remove tokens, passwords, and personal data before pasting.

## Logs or Visual Evidence

If applicable, add the relevant console output, `logs/api.log` excerpt, or Swagger screenshot. Remove credentials and personal data first.

## Environment

- **Operating System**: [e.g. Windows 11, Ubuntu 24.04]
- **Python version**: [e.g. 3.12.4]
- **Docker / Compose version**: [e.g. Docker 27.3, Compose v2.29]
- **MySQL**: [e.g. 8.0 container from `docker-compose.yml`]
- **Chrome version**: [only for scraper issues, e.g. 144.0.x]
- **Branch / commit**: [e.g. `master` / `abc1234`]

## Privacy and Security Impact

- [ ] This report contains no real personal data, credentials, or tokens.
- [ ] This issue may have a security impact (if checked, do **not** post exploit details publicly; follow [`SECURITY.md`](https://github.com/felipevenas/api-boilerplate/blob/master/SECURITY.md)).

## Additional Context

Any other context, such as database state, a minimal reproduction repository, or related issues.
