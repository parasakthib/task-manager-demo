# Repository custom instructions for GitHub Copilot

This is a Python 3.10+ CLI application with no external dependencies beyond the standard library.

## Before implementing any feature
- Check `docs/REQUIREMENTS.md` for the relevant REQ-ID and acceptance criteria.
- Update the requirements table's status column when a REQ moves from ❌ to ✅.

## Code standards
- No raw tracebacks should ever reach the CLI user — catch and re-raise as a clear message (see REQ-7 / NFR-2).
- Prefer f-strings and `pathlib` over `%`-formatting and `os.path`.
- All public functions need a one-line docstring.

## Testing requirements
- Follow `docs/TESTING.md` exactly: `pytest`, naming convention `test_<fn>_<scenario>_<expected>`, use `tmp_path` for file I/O tests.
- New code must include a happy-path, edge-case, and error-handling test.
- Run `pytest --cov=src` before considering a change complete; target ≥ 85% coverage.

## Pull requests
- Reference the Issue number and REQ-ID in the PR description.
- Do not modify `tasks.json` — it's a runtime artifact, not source.
