# AGENTS.md

Critical rules for every agent session in this repository.

## Commands

- `uv sync` — install dependencies
- `uv run pytest` — run all tests
- `uv run pytest tests/test_home.py` — run one test file

## Rules

### Dependencies
Dependencies are added in `pyproject.toml` only. Do not add a dependency without asking the user first.

### Testing
All new Python code must have corresponding tests. A task is not complete until tests pass.

### GitHub Issues
Reference issue numbers in commits (e.g., "Closes #3"). One task per PR.

### Frontend
Always invoke the `frontend-design` skill before writing frontend code. Screenshot on `http://localhost:3000` and compare to reference before declaring a page complete.
