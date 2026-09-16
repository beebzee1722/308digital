# 308 Digital — Task Backlog

## 1. Set up Django project with passing test
Goal: Initialize Django app with a working test suite.
Description: Create a minimal Django project structure with `manage.py`, a basic test module, and a passing unit test. Verify the test runner works and all project dependencies are installed. This establishes the foundation for subsequent tasks.

## 2. Create base templates and shared components
Goal: Build reusable layout template, navigation, and footer.
Description: Create Django template base structure with a main layout template (`base.html`), navigation bar component, footer component, and CSS reset/global styles. Ensure all pages can inherit from this base. No page-specific content yet.

## 3. Build home page
Goal: Implement the home page with hero, services teaser, industries teaser, and CTAs.
Description: Create the home page view and template with hero section (headline + subheading), a "What we do" section teasing 3 services with links to the full services page, industries teaser with logos, why-choose-us highlights, and a closing call-to-action. Static content only.

## 4. Build services page
Goal: Display all 6 AI services as cards.
Description: Create services listing page with intro text and 6 service cards (AI Strategy & Consulting, Intelligent Automation, Data Analytics & BI, Finance & Insurance Solutions, Custom AI Solutions, Digital Transformation Services). Each card shows title and description.

## 5. Build industries page
Goal: Display all 5 target industries as cards.
Description: Create industries page with intro text and 5 industry cards (Financial Services, Insurance, Healthcare, Retail & E-commerce, Public Sector & Enterprise). Each card includes title and description.

## 6. Build about page
Goal: Showcase company mission, vision, and why-choose-us statement.
Description: Create about page with mission statement section, vision statement section, and a full "why choose us" section listing all 5 value propositions. Layout as readable text blocks with clear hierarchy.

## 7. Build contact page (HTML structure)
Goal: Create contact page layout with form structure and success/error states.
Description: Build contact page template with a contact form (name, email, message fields), placeholder for success/error messages, and company contact details footer. Form is static HTML; Vue.js interactivity added in a later task.

## 8. Add Vue.js contact form island
Goal: Add client-side validation and UX to contact form.
Description: Wire up a Vue.js island to the contact form with live validation (required fields, email format), loading/success/error state handling, and button state changes. Form doesn't yet submit; this task is pure frontend UX.

## 9. Implement contact form backend
Goal: Create Django view to receive and process form submissions.
Description: Build a Django view/endpoint that accepts contact form POST requests, validates data, sends an email to the company inbox (or logs success), and returns appropriate JSON response. Pair with the Vue.js island from task 8.

## 10. Apply brand styling and polish
Goal: Apply 308 Digital brand colors, typography, and spacing.
Description: Implement color palette from brand guidelines (primary, secondary, accent colors), typography hierarchy (headings + body fonts), spacing tokens, and visual polish (shadows, borders, hover states, animations). Ensure mobile responsiveness across all pages.
