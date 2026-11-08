# Security Policy 🔒

**api-boilerplate** is a public FastAPI reference template. It is not a hosted production service, but it demonstrates authentication, password storage, database access, and browser automation, so security reports are welcome and taken seriously.

If you believe you have found a vulnerability, please disclose it privately.

---

## Supported Versions

There are no tagged releases. Only the latest commit on **`master`** receives security attention:

| Version | Supported |
|---|---|
| `master` (latest commit) | :white_check_mark: |
| Older commits, forks, and copies | :x: |

Because this is a template, downstream users are responsible for the security of their own deployments, data, and modifications.

---

## Reporting a Vulnerability

**Please do not report security vulnerabilities in public issues, discussions, or pull requests.**

1. Open a confidential report through **[Private Vulnerability Reporting](https://github.com/felipevenas/api-boilerplate/security/advisories/new)**.
2. If that feature is unavailable, contact the maintainer through [@felipevenas](https://github.com/felipevenas) without opening a public issue.
3. Include the affected endpoint or file, reproduction steps, potential impact, and a minimal proof of concept.
4. Do not include real credentials, production data, or third-party personal data in the report.

We aim to acknowledge reports within **48 business hours** and will share an assessment and remediation plan as soon as the issue is reproduced.

---

## Security Scope

The following issues are considered high priority for this repository:

- **Secret exposure:** `SECRET_KEY`, database credentials, `.env` contents, tokens, or password hashes in the repository, logs, responses, or build artifacts.
- **Password hash disclosure:** any endpoint returning the `password` column. `GET /api/v1/me` currently returns the ORM object directly and is a known gap.
- **Plaintext password storage:** the direct `POST /api/v1/` user-creation route passes `UserCreate.password` to the repository without hashing it. `/api/v1/register` and the automation service do hash passwords.
- **Authentication bypass:** forged, unsigned, expired, or algorithm-confused JWTs; missing signature validation; tokens accepted after user deactivation.
- **Authorization failure:** any authenticated user reading, updating, deleting, or toggling another user without an ownership or role check. The current template has no roles, so this is a known design limitation rather than a hidden feature.
- **Injection:** SQL injection through repository queries, header injection, log injection, or unsafe interpolation of configuration into the database URL.
- **Data exposure:** listing inactive users, returning password hashes, exposing internal exception details, or leaking stack traces.
- **Privacy and scraping:** use of the automation module to collect, store, or publish real personal data, or use that violates a third-party site's terms, robots policy, or applicable privacy law.
- **Local infrastructure exposure:** MySQL or phpMyAdmin reachable beyond localhost, default or empty root passwords, or Compose files used in an untrusted network.
- **Denial of service:** unbounded request bodies, expensive scraper calls, or missing resource limits that can be triggered remotely.
- **Vulnerable dependencies:** a pinned dependency with a known advisory that affects runtime behavior.

### Explicitly out of scope

- Vulnerabilities that require a compromised host, physical access, or a malicious browser extension.
- Reports about the template lacking features it never claimed, such as rate limiting, MFA, or refresh tokens. These are documented limitations; open a feature request instead.
- Social engineering and spam.
- Findings that only affect an unsupported fork or an outdated commit.

---

## Resolution Process

1. Confirm the report and classify its impact.
2. Reproduce the issue in a controlled local environment.
3. Prepare the smallest safe fix, with a regression test when the test infrastructure exists.
4. Publish the fix on `master` and record user-relevant changes in [`CHANGELOG.md`](CHANGELOG.md).
5. Credit the reporter after the fix, if they wish to be named.

For issues that affect downstream users, the advisory will describe the affected versions or commits and the recommended action.

---

## Hardening Checklist for Downstream Users

Before adapting this template, at minimum:

- [ ] Add a `LICENSE` file and review the legal terms of every dependency.
- [ ] Replace `SECRET_KEY` with a long random value stored outside the repository.
- [ ] Return a `UserRead` schema from `GET /api/v1/me` and every user-facing route.
- [ ] Hash passwords on every creation path, including the direct `POST /api/v1/` route.
- [ ] Add authorization rules; do not let any authenticated user manage any account.
- [ ] Restrict MySQL and phpMyAdmin to localhost and remove empty-password settings.
- [ ] Add CORS with an explicit allowlist if a browser client will call the API.
- [ ] Add rate limiting, request size limits, and authentication lockout.
- [ ] Add migrations, backups, and a timezone policy.
- [ ] Add tests, static analysis, and CI before deploying.
- [ ] Review the scraper's legal and privacy implications or remove it.

Thank you for helping keep this template safe.
