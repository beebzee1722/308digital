# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

308 Digital is a multi-page marketing website for an AI consulting firm. The site targets five industries: financial services, insurance, healthcare, retail & e-commerce, and public sector.

**Tech Stack:**
- Backend: Django (templates + views)
- Frontend interactivity: Vue.js islands (opt-in, not a full SPA)
- Package management: `uv` (not pip)
- Python: 3.14+

**Reference docs:**
- `_docs/plan.md` — full product scope, pages, sections, and open decisions
- `_docs/tasks.md` — task backlog with 10 independent work items
- `_docs/308_Digital_Brand_Guidelines.md` — brand colors, typography, tone
- GitHub issues (linked 1:1 with tasks.md) — track progress

## Setup & Common Commands

### Install and run
```bash
uv sync              # Install all dependencies (creates .venv)
uv run 308digital    # Run the entry point (currently just prints a greeting)
```

### Django commands (when Django is added)
```bash
uv run python manage.py runserver          # Start dev server
uv run python manage.py migrate            # Apply migrations
uv run python manage.py createsuperuser    # Create admin user
```

### Testing (when tests are added)
```bash
uv run pytest                    # Run all tests
uv run pytest path/to/test.py    # Run a single test file
uv run pytest -k test_name       # Run a single test by name
uv run pytest --cov             # Run with coverage report
```

### Code quality (when linters are added)
```bash
uv run ruff check src/           # Lint Python code
uv run ruff format src/          # Auto-format Python code
```

## Project Structure

```
src/308digital/           # Main Python package
_docs/                    # Documentation
  plan.md               # Full project scope and architecture
  tasks.md              # Task backlog (also as GitHub issues #1–#10)
  308_Digital_Brand_Guidelines.md
```

No templates, static files, or Django app structure yet—these will be added as tasks progress.

## Architecture & Key Decisions

**Django project structure (to be created):**
- `manage.py` — Django management script
- `308digital_project/` — Django project settings (settings.py, urls.py, wsgi.py)
- `<app_name>/` — Django apps, one per feature area (e.g., `pages`, `contact`)
  - `views.py` — render templates or return JSON
  - `urls.py` — route patterns
  - `models.py` — database models (if needed)
  - `templates/<app_name>/` — Django templates (inherit from `base.html`)

**Frontend patterns:**
- **Base template** (`base.html`) — shared nav, footer, head boilerplate
- **Page templates** — inherit from base; static content per task 3–7
- **Vue.js islands** — only the contact form (task 8) needs Vue; isolated component tree, not a full app
- **Static files** — CSS (inline or linked), images, Vue.js bundle

**Contact form flow (tasks 7–9):**
1. Task 7: HTML structure (form fields, error/success placeholders)
2. Task 8: Vue.js wraps the form with client-side validation & UX state
3. Task 9: Django view receives POST, validates, emails, returns JSON

**Spam protection decision (open in plan.md):** Currently unresolved—honeypot (low friction, no JS required) vs. reCAPTCHA vs. defer. Implement during task 9.

## Brand & Design Guidelines

**Before writing frontend code:**
1. Consult `_docs/308_Digital_Brand_Guidelines.md` for colors, fonts, tone
2. All pages must match the brand palette—no default Tailwind colors
3. Screenshot locally and compare to reference if provided

**Responsive design:**
- Mobile-first approach (required by CLAUDE.md global rules)
- Test on mobile, tablet, desktop viewports

## Task Dependencies

Tasks 1–2 are blocking (set up Django + base templates). Tasks 3–7 are independent (can be worked in any order once 1–2 are done). Task 8 depends on task 7. Task 9 depends on task 8. Task 10 (styling) improves all previous pages.

## GitHub & Issue Tracking

All 10 tasks are tracked as GitHub issues (#1–#10). Close an issue when the corresponding task is complete. PRs should reference the issue number (e.g., "Closes #1").
