# Testing Guidelines

## Framework
- `pytest` for all unit and integration tests.
- No other test frameworks (unittest, nose) should be introduced.

## Structure
- One test file per source module: `src/foo.py` → `tests/test_foo.py`.
- Group related tests into classes only when they share setup/fixtures; otherwise use flat functions.

## Naming Convention
```
test_<function_under_test>_<scenario>_<expected_result>
```
Example:
```python
def test_add_task_with_empty_title_raises_value_error():
    ...
```

## Coverage Targets
- Minimum 85% line coverage on `src/`.
- Every public function must have at least:
  - 1 "happy path" test
  - 1 edge case test (empty input, boundary value, etc.)
  - 1 error-handling test (invalid input)

## Fixtures
- Use `tmp_path` (pytest built-in) for any test that touches `tasks.json` — never write to the real file system location used by the CLI.
- Shared fixtures go in `tests/conftest.py`.

## What NOT to test
- Don't test Python standard library behavior.
- Don't write tests that depend on wall-clock time without freezing it (use `freezegun` or inject a clock).

## Running tests
```bash
pytest                     # run all tests
pytest --cov=src           # run with coverage report
pytest -k "priority"       # run tests matching a keyword
```

## Definition of Done for a test suite
A feature is not "done" until:
1. All acceptance criteria in `docs/REQUIREMENTS.md` have a corresponding test.
2. `pytest --cov=src` reports ≥ 85% coverage with no untested branches on new code.
3. Tests pass in CI on a clean checkout (no reliance on local state).
