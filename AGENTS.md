# AGENTS.md

Guidance for Claude Code and other agents working in this repository.

## Commands

### Setup
- `uv sync` — install all dependencies into `.venv`
- `python --version` — verify Python 3.14+

### Running the project
- `uv run 308digital` — run the entry point (currently prints a greeting)
- `uv run python manage.py runserver` — start Django dev server (when Django is added)

### Testing
- `uv run pytest` — run all tests
- `uv run pytest tests/test_home.py` — run a single test file
- `uv run pytest -k test_name` — run a single test by name
- `uv run pytest --cov` — run tests with coverage report

### Code quality
- `uv run ruff check src/` — lint Python code
- `uv run ruff format src/` — auto-format Python code

### Git
- `git status` — check uncommitted changes
- `git log --oneline -10` — view recent commits
- `gh issue list` — list GitHub issues (corresponds to tasks.md)

### Screenshots (when frontend is being built)
- `node serve.mjs` — start the dev server at `http://localhost:3000`
- `node screenshot.mjs http://localhost:3000` — take a screenshot and save to `temporary screenshots/`
- Compare screenshots to brand guidelines before declaring a page complete

## Rules

### Dependencies
- Dependencies are added in `pyproject.toml` only. Do not add one without asking the user.
- Use `uv add <package>` to add a new dependency (updates both `pyproject.toml` and `uv.lock`).
- Always run `uv sync` after `pyproject.toml` changes.

### Testing
- All new Python code must have corresponding tests.
- Tests live in `tests/` directory mirroring the `src/` structure (e.g., `src/308digital/foo.py` → `tests/test_foo.py`).
- A task is not complete until tests are passing.

### Frontend (when building pages)
- Always invoke the `frontend-design` skill before writing any frontend code.
- All pages must use the brand color palette from `_docs/308_Digital_Brand_Guidelines.md`.
- No default Tailwind colors (indigo, blue, etc.); derive colors from brand palette.
- Screenshot locally on `http://localhost:3000` (not `file:///`); compare to reference before claiming completion.
- Mobile-first responsive design is required.

### Django (when setting up)
- Use Django templates (not a full REST API), following Django best practices.
- Vue.js is used only for the contact form (task #8), not for every interactive element.
- All templates inherit from `base.html`.

### Git & GitHub
- Reference GitHub issue numbers in commits and PRs (e.g., "Closes #3" or "Implements #4").
- One feature/task per PR. Do not batch unrelated work.
- Keep commits focused; do not mix refactoring with feature work.

### Brand & Design
- Consult `_docs/308_Digital_Brand_Guidelines.md` before designing anything.
- If a reference image or design is provided, match it exactly (layout, spacing, typography, colors).
- Do not "improve" a design; match the reference.
- Screenshot comparisons should be specific ("heading is 28px but should be 24px").

### Documentation
- Update CLAUDE.md or AGENTS.md if you discover new patterns or commands.
- Do not write code that requires a README to understand.
- Keep comments minimal: only explain "why," not "what."
