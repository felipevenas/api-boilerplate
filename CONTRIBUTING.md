# Contributing Guide 🤝

Thank you for your interest in improving **api-boilerplate**. This document explains the workflow so the template stays readable, secure, and useful as a reference.

> **Golden rule:** this is a public teaching template. Never commit real credentials, `.env` files, private data, or scraped identities. Any automation data must stay synthetic and local, and no change may present the repository as production-ready when it is not.

---

## 🛠️ Development Environment

### Prerequisites

- **Python 3.10+** with `pip`.
- **Docker Desktop** or another Docker Engine with Compose v2.
- **Git**.
- **Google Chrome 144** only if you need to exercise the scraper endpoint.
- A terminal with PowerShell on Windows or a POSIX shell on Linux/macOS.

### Local setup

```powershell
git clone https://github.com/felipevenas/api-boilerplate.git
cd api-boilerplate
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requeriments.txt
docker compose up -d
```

On Linux/macOS, activate the environment with `source .venv/bin/activate`.

Create `.env` at the repository root with the variables documented in [`README.md`](README.md#configuration). The application does not create tables, so create the `users` table using the reference DDL in [`README.md`](README.md#6-create-the-users-table) before calling the user endpoints.

Start the API with:

```bash
uvicorn app.main:app --reload
```

Swagger UI is available at `http://localhost:8000/docs`.

> The dependency file is named **`requeriments.txt`** in this repository. Keep that name in commands until a dedicated rename change is approved.

---

## 🌿 Branches and Commits

The default branch is **`master`**, not `main`. Create every branch from `master` and open pull requests against `master`.

### Branch names

- `feat/feature-name`
- `bug/bug-name`
- `chore/task-name`
- `docs/document-name`
- `style/formatting-adjustment`
- `refactor/refactoring-name`
- `test/test-name`

Examples: `feat/pagination`, `bug/duplicate-email`, `docs/security-notes`.

### Commits

Write commit messages in **English** using Conventional Commits:

| Prefix | Use |
|---|---|
| `feat:` | New user-visible behavior |
| `fix:` | Behavior, contract, or defect fix |
| `refactor:` | Internal change with no functional difference |
| `docs:` | Documentation, README, or comment-only changes |
| `test:` | Tests or test infrastructure |
| `style:` | Formatting with no behavior change |
| `chore:` | Dependencies, tooling, CI, or configuration |

Example: `fix: return 404 when a user does not exist`.

Keep commits focused. Do not mix documentation, refactoring, and behavior changes in the same commit unless they are inseparable.

---

## 🏛️ Architectural Guidelines

The project uses a small, domain-oriented layered structure:

```text
routes -> services -> repositories -> models
routes -> schemas
services -> helpers / infra
```

Rules that must not be broken:

1. **Routes stay thin.** Parse input, call a service, choose the status code, and return. No SQL and no business rules in `routes.py`.
2. **Services own business rules.** They may call repositories and helpers. They must not import FastAPI, `Request`, `HTTPException`, or build HTTP responses.
3. **Repositories own persistence.** SQLAlchemy queries and commits belong in `repository.py`. Repositories must not validate HTTP payloads.
4. **Models are persistence-only.** `models.py` must not know about routes, schemas, or services.
5. **Schemas define the boundary.** Use Pydantic v2 models for request and response validation. Keep `UserRead` free of sensitive fields.
6. **Dependency injection uses `Depends`.** Follow the existing `get_*_service(db)` factory pattern instead of instantiating repositories inside routes.
7. **New domains are self-contained.** Add a folder under `app/domain/{name}/` with `models.py`, `schemas.py`, `repository.py`, `services.py`, and `routes.py`, then register the router in `app/api/endpoints/routes.py`.
8. **Configuration comes from the environment.** Read values through `app/core/config.py`; never hardcode credentials, hosts, or secrets.
9. **API paths stay under `/api/v1`.** Mount new routers through `app/api/endpoints/routes.py`.
10. **Do not silently change the public contract.** Renaming a field, path, or response shape is a breaking change and must be called out in the pull request.

The structure is inspired by Clean Architecture and DDD, but it is not a strict ports-and-adapters implementation. Do not introduce interfaces, containers, or async infrastructure only to match a diagram; prefer the smallest change that keeps the layers honest.

---

## 🧪 Quality Gates

There is currently **no automated test suite, linter, type checker, or CI workflow**. Until those exist, the minimum manual gate is:

```powershell
python -m compileall app
uvicorn app.main:app --reload
```

Then verify:

- [ ] The application starts with a valid `.env` and a reachable MySQL instance.
- [ ] `http://localhost:8000/openapi.json` is generated without errors.
- [ ] Register, login, and `GET /api/v1/me` work with a bearer token.
- [ ] The changed endpoint behaves correctly for success, validation failure, missing authentication, and not-found cases.
- [ ] No new secret, personal data, or generated artifact is staged.

If you introduce tests or tooling, keep it reproducible and document the commands in [`README.md`](README.md#testing). Prefer `pytest` + `httpx` for API tests and a disposable MySQL instance for integration coverage.

---

## 🔐 Security and Privacy

- Never commit `.env`, `SECRET_KEY`, database passwords, tokens, or logs containing personal data.
- Never commit real people's data. The scraper generates synthetic identities; treat even those as local test fixtures.
- Do not log request bodies, authorization headers, passwords, or password hashes.
- Authorization belongs in the API. Hiding a button or route in a client is not a security control.
- Preserve password hashing with Passlib/bcrypt. Never store or return plaintext passwords. Note that the direct `POST /api/v1/` route currently bypasses hashing; fix it if you touch that flow.
- Be careful with the `GET /api/v1/me` response: it currently serializes the ORM object, including the password hash. If you touch that route, return a `UserRead` schema instead of the raw model.
- New dependencies require a justification, a compatible license, and a vulnerability review.
- Report vulnerabilities privately according to [`SECURITY.md`](SECURITY.md). Never open a public issue for an unfixed vulnerability.

---

## 📬 Submitting a Pull Request

1. Create a short-lived branch from **`master`**.
2. Keep the change focused and update documentation when behavior changes.
3. Run the manual quality gate and describe exactly what you verified.
4. Fill in the pull request template, including reproduction steps and evidence.
5. Update [`CHANGELOG.md`](CHANGELOG.md) for notable changes.
6. Open the pull request against **`master`** and wait for review.

For changes touching authentication, user data, the scraper, or database access, add an explicit security and privacy note to the pull request.

### Definition of Done

- The behavior is implemented and manually verified.
- The layering rules above are respected.
- The public contract is documented, including breaking changes.
- Sensitive fields are not exposed in responses or logs.
- No secrets, real personal data, or generated artifacts are committed.
- Documentation and `CHANGELOG.md` are updated when relevant.
- The pull request is reviewed and approved.
