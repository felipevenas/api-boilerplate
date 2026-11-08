# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

### 📝 Documentation

- Rewrote `README.md` in English with verified stack versions, architecture, project layout, quick start, configuration reference, API surface, testing status, deployment boundaries, known limitations, governance, related documentation, and license status.
- Corrected documentation that did not match the code: the MySQL driver is PyMySQL (not `asyncmy`), the Selenium pin is `4.16.0`, the database variable is `DB_PASS`, the automation path is `/api/v1/automations/scraper/generate-user`, and the application does not create database tables automatically.
- Documented that this repository is a boilerplate, not a production service, and listed the current security, persistence, automation, and tooling gaps without changing runtime behavior.
- Added `CONTRIBUTING.md` with the `master`-based branch flow, Conventional Commits, architecture rules, manual quality gates, security guidance, and Definition of Done.
- Added `SECURITY.md` with supported-version scope, private disclosure channel, project-specific vulnerability scope, and a downstream hardening checklist.
- Added `CODE_OF_CONDUCT.md` adapted from the Contributor Covenant.
- Added GitHub issue and pull request templates under `.github/`.
- Added `.editorconfig` and `.gitattributes` for UTF-8, LF normalization, indentation, and final-newline consistency.
- Documented the existing `requeriments.txt` filename as-is and recorded the rename to `requirements.txt` as a follow-up rather than changing dependencies or file names in this documentation-only change.

<!--
When a release is created, add a new section with the version and ISO date, for example:

## [0.2.0] - YYYY-MM-DD

### Added
### Changed
### Fixed
### Removed
### Security
-->
