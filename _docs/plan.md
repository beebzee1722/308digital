# 308 Digital — Website Project Scope

## Objective
Build a multi-page marketing website for 308 Digital, an AI consulting firm targeting finance, insurance, healthcare, retail, and public sector clients. The layout pattern is loosely inspired by meritmap.ai's single-audience landing page structure (hero → problem/value → process → CTA), adapted into a multi-page site with 308 Digital's own branding and copy.

## Tech Stack
- **Backend/templating:** Django templates
- **Interactivity:** Vue.js islands (used only where needed — not a full SPA)
- **Styling:** Brand palette and typography from the 308 Digital Brand Guidelines doc

## Pages & Sections

### Home
- Hero banner (headline + subheading)
- "What we do" teaser (3 of the 6 services, linking to full Services page)
- "Industries" teaser (names/logos, linking to full Industries page)
- Why-choose-us highlights
- Closing CTA

### Services
- Intro line
- All 6 service cards (title + description):
  - AI Strategy & Consulting
  - Intelligent Automation
  - Data Analytics & Business Intelligence
  - Finance & Insurance Solutions
  - Custom AI Solutions
  - Digital Transformation Services

### Industries
- Intro line
- All 5 industry cards (title + description):
  - Financial Services
  - Insurance
  - Healthcare
  - Retail & E-commerce
  - Public Sector & Enterprise

### About
- Mission statement
- Vision statement
- Why-choose-us (all 5, in full)
- Optional team/company info (future addition)

### Contact
- Contact form (name, email, message)
- Success/error state on submit
- Company contact details in footer area

## Contact Form — Technical Scope
- Vue.js island for client-side validation + submit state (loading/success/error)
- Django view/endpoint to receive and email the submission (email delivery for MVP; DB storage optional later)
- Spam protection: **decision pending** — honeypot field (low-effort, no user friction) vs. reCAPTCHA vs. deferring to a later phase

## Shared Components
- Navigation bar
- Footer
- CTA banner block
- Section header pattern

## Explicitly Out of Scope (this phase)
- Blog
- Case studies / testimonials
- Login / dashboard
- Pricing page
- Multi-language support

## Open Decisions
- [ ] Contact form spam protection: honeypot now, reCAPTCHA, or defer