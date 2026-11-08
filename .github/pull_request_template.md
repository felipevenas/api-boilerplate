# Pull Request Description

Include a summary of the change, the problem or feature it addresses, and the expected impact on the API contract, security, data, and documentation.

---

## Type of Change

- [ ] 🚀 New feature (`feat`)
- [ ] 🐞 Bug fix (`fix`)
- [ ] 🔧 Refactoring with no functional change (`refactor`)
- [ ] 📝 Documentation only (`docs`)
- [ ] 🎨 Style / formatting (`style`)
- [ ] ⚙️ Tooling, dependencies, CI, or configuration (`chore`)
- [ ] 🔒 Security or privacy (`security`)

## How Was It Tested?

Describe the validations performed and how to reproduce them locally.

- [ ] **Syntax:** ran `python -m compileall app` with no errors.
- [ ] **Startup:** started the API with a valid `.env` and a reachable MySQL instance.
- [ ] **OpenAPI:** loaded `http://localhost:8000/openapi.json` and `http://localhost:8000/docs`.
- [ ] **Authentication:** registered, logged in, and called `GET /api/v1/me` with a bearer token.
- [ ] **Changed flow:** exercised success, validation failure, missing authentication, and not-found cases.
- [ ] **Database:** applied the required schema change manually, because the project has no migrations.
- [ ] Other checks performed:

## Visual Evidence / Logs

*If applicable, paste relevant request/response examples, Swagger screenshots, or logs. Remove tokens, credentials, and personal data first.*

## Checklist

- [ ] I created this branch from `master` and target `master` in this pull request.
- [ ] My change follows the layering rules in [`CONTRIBUTING.md`](https://github.com/felipevenas/api-boilerplate/blob/master/CONTRIBUTING.md).
- [ ] I self-reviewed the diff and removed dead or experimental code.
- [ ] I updated documentation and `CHANGELOG.md` when the change is notable.
- [ ] I did not commit `.env`, secrets, tokens, logs with personal data, or scraped identities.
- [ ] I did not expose password hashes or other sensitive fields in responses.
- [ ] I updated `requeriments.txt` if dependencies changed, keeping the existing filename.
- [ ] I did not rename files or change dependencies in a documentation-only pull request.
- [ ] I described any breaking change to the `/api/v1` contract.

## Additional Context

Add design decisions, trade-offs, follow-up work, or anything reviewers should know.
