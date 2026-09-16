# 308 Digital — Technology Architecture

## Overview

308 Digital is a modern, full-stack web application combining a Django backend with React/Next.js frontend capabilities, featuring an interactive hero section with a custom ConstellationField component. The architecture supports both dynamic server-side rendering and client-side interactivity.

---

## Tech Stack

### **Frontend**

#### Core Framework
- **Next.js 14** — React meta-framework for server-side rendering, static generation, and API routes
  - Provides file-based routing via `app/` directory
  - Built-in TypeScript support
  - Optimized image handling and performance
  - API route capabilities for serverless functions

#### UI Framework & Styling
- **React 18** — Component-based UI library
- **TypeScript** — Static type checking for JavaScript
  - Strict mode enabled for maximum type safety
  - JSX support with full TSX compatibility
- **Tailwind CSS 3** — Utility-first CSS framework
  - PostCSS for processing
  - Custom color scheme (dark navy, gold accents, cream backgrounds)
  - Responsive design with mobile-first approach
- **Custom CSS** — Global styles in `app/globals.css`
  - Brand typography setup (Space Grotesk, IBM Plex Sans)
  - CSS reset and base element styling

#### Typography
- **Space Grotesk** — Modern geometric sans-serif for headings
  - Weights: 400, 500, 600, 700
  - Loaded via Google Fonts CDN
- **IBM Plex Sans** — Clean, legible sans-serif for body text
  - Weights: 400, 500, 600
  - Loaded via Google Fonts CDN

#### Animation & Interactivity
- **Canvas API** — Native HTML5 canvas for WebGL particle animations
- **GSAP 3** — GreenSock Animation Platform (available in CDN)
  - ScrollTrigger plugin for scroll-based animations
  - Staggered word reveal animations
  - Smooth easing functions
- **Vue.js 3** — Progressive JavaScript framework for interactive components
  - Used specifically for contact form validation and state management
  - Imported via CDN
  - Island-based architecture (Vue only where needed)

#### Icons
- **Iconify** — Unified icon framework
  - `solar` icon set for UI elements
  - Loaded via CDN for zero-build overhead

#### HTTP & State
- **Fetch API** — Native browser API for HTTP requests
- **Vue.js Reactivity** — Reactive data binding for form state

---

### **Backend**

#### Web Framework
- **Django 6.1** — Python web framework
  - MTV (Model-Template-View) architecture
  - Built-in admin panel for content management
  - ORM for database interactions
  - Middleware stack for cross-cutting concerns

#### Server Runtime
- **Python 3.14** — Latest Python release
- **Gunicorn** (recommended for production) — WSGI HTTP server
- **uWSGI** (alternative) — Application container

#### Database
- **SQLite** — Development database
  - Recommended upgrade to PostgreSQL for production
- **Django ORM** — Object-relational mapping for schema and queries

#### API & Backend Services
- **Django REST Framework** (optional, for API expansion)
- **Contact Form Endpoint** — `/api/contact/` POST endpoint
  - Server-side validation (name, email, message)
  - Email sending via Django mail backend
  - CSRF protection via Django middleware
  - JSON request/response format

#### Email Backend
- **Console Email Backend** (development) — Prints emails to console
- **SMTP** (production) — Configurable via `EMAIL_BACKEND` setting
  - AWS SES, SendGrid, or standard SMTP

#### Security
- **CSRF Protection** — Django middleware for cross-site request forgery prevention
- **Same-Origin Policy** — Browser security enforcement
- **Secure Headers** — X-Frame-Options, X-Content-Type-Options, etc.

---

### **Component Architecture**

#### Custom Components

**ConstellationField** (`components/ui/constellation-field.tsx`)
- React component wrapping iframe-based canvas animation
- Configurable properties:
  - `mode`: dark/light/auto
  - `speed`: animation speed multiplier (0–3)
  - `size`: particle size scale (0.05–200)
  - `density`: node count density (0.25–2.5)
  - `strokeWidth`: line thickness (0.25–8)
  - `opacity`: global opacity (0.05–1)
  - `hue`, `saturation`, `brightness`: CSS filter adjustments
- Uses `useRef` and `useEffect` hooks for iframe management
- Props memoization for performance optimization

#### Shared Components
- **Navigation** — Sticky header with blur backdrop
- **Hero Section** — ConstellationField background + content overlay
- **Trust Indicators** — User avatars and rating display
- **CTA Buttons** — Gradient-bordered call-to-action elements
- **Company Logos** — Logo grid with hover effects
- **Contact Form** — Vue.js-controlled validation and submission

---

### **Data Flow**

```
User Browser
    ↓
Next.js Frontend (React/TypeScript)
    ├─ Static Pages (Home, Services, etc.)
    ├─ Interactive Components (ConstellationField, Vue Forms)
    └─ API Requests (fetch)
       ↓
Django Backend
    ├─ URL Routing (`pages/urls.py`)
    ├─ Views (class-based and function-based)
    ├─ Request Processing
    ├─ Database Access (Django ORM)
    └─ Response (JSON/HTML)
       ↓
User Browser (Rendered Response)
```

---

### **Development Workflow**

#### Local Development
```bash
# Start Django development server
uv run python manage.py runserver 0.0.0.0:8000

# Or with Next.js (requires Node.js)
npm install
npm run dev
```

#### Production Deployment
```bash
# Build Next.js (if using Next.js)
npm run build

# Run with Gunicorn
gunicorn digital_site.wsgi:application --bind 0.0.0.0:8000

# Or with uWSGI
uwsgi --http :8000 --wsgi-file digital_site/wsgi.py --master --processes 4
```

---

### **Project Structure**

```
308digital/
├── app/                          # Next.js app directory
│   ├── layout.tsx               # Root layout
│   ├── page.tsx                 # Home page
│   ├── globals.css              # Global styles
├── components/
│   └── ui/
│       └── constellation-field.tsx  # ConstellationField component
├── pages/                        # Django app
│   ├── views.py                 # View handlers
│   ├── urls.py                  # URL routing
│   ├── models.py                # Database models
│   ├── templates/
│   │   └── pages/
│   │       ├── index.html       # Single-page website
│   │       ├── home.html
│   │       ├── services.html
│   │       ├── industries.html
│   │       ├── about.html
│   │       └── contact.html
├── digital_site/                # Django project settings
│   ├── settings.py              # Configuration
│   ├── urls.py                  # URL patterns
│   └── wsgi.py                  # WSGI application
├── package.json                 # Node.js dependencies
├── tsconfig.json                # TypeScript configuration
├── tailwind.config.ts           # Tailwind CSS configuration
├── postcss.config.js            # PostCSS configuration
├── next.config.js               # Next.js configuration
├── manage.py                    # Django management script
└── ARCHITECTURE.md              # This file
```

---

### **Key Technologies & Versions**

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Next.js** | 14.0 | React meta-framework |
| **React** | 18.2 | UI library |
| **TypeScript** | 5.2 | Type safety |
| **Django** | 6.1 | Backend framework |
| **Python** | 3.14 | Runtime |
| **Tailwind CSS** | 3.3 | Utility CSS |
| **Vue.js** | 3 | Interactive forms |
| **GSAP** | 3.12 | Animations |
| **PostgreSQL** | 15+ | Database (recommended) |

---

### **Features Enabled by Tech Stack**

#### Frontend Features
✅ Server-side rendering with Next.js
✅ Static site generation for performance
✅ React component reusability
✅ TypeScript type safety across the stack
✅ Tailwind CSS responsive design
✅ Interactive particle animations (Canvas)
✅ Scroll-triggered animations (GSAP)
✅ Client-side form validation (Vue.js)

#### Backend Features
✅ Dynamic API endpoints
✅ Form submission handling with CSRF protection
✅ Email integration
✅ Database persistence (SQLite → PostgreSQL)
✅ Admin panel for content management
✅ Middleware stack for security

#### Performance Optimizations
✅ Tailwind CSS tree-shaking (minimal CSS)
✅ Next.js code splitting and lazy loading
✅ Canvas-based animations (GPU accelerated)
✅ Responsive image handling
✅ Caching strategies (HTTP headers)
✅ Minified and optimized assets

---

### **Deployment Considerations**

#### Environment Variables
```bash
DEBUG=False                     # Disable debug mode in production
SECRET_KEY=<secure-random>     # Django secret key
ALLOWED_HOSTS=...              # Allowed domain names
DATABASE_URL=...               # Database connection
EMAIL_HOST=...                 # SMTP server
EMAIL_PORT=...                 # SMTP port
EMAIL_USER=...                 # SMTP credentials
EMAIL_PASSWORD=...             # SMTP credentials
```

#### Production Checklist
- [ ] Set `DEBUG=False` in Django settings
- [ ] Use environment variables for secrets
- [ ] Enable HTTPS/SSL
- [ ] Set up PostgreSQL database
- [ ] Configure email service (SendGrid, AWS SES, etc.)
- [ ] Enable security headers (HSTS, CSP, X-Frame-Options)
- [ ] Set up monitoring and logging
- [ ] Configure CDN for static assets
- [ ] Use Gunicorn or uWSGI as application server
- [ ] Use Nginx as reverse proxy

---

### **Future Enhancements**

#### Potential Additions
- **Database Layer** — Migrate from SQLite to PostgreSQL for scalability
- **API Expansion** — Expose full REST API via Django REST Framework
- **Authentication** — Add user accounts with JWT tokens
- **CMS Integration** — Headless CMS for content management
- **Analytics** — Google Analytics, Mixpanel, or Segment integration
- **CDN** — CloudFront, Cloudflare, or similar for global distribution
- **Caching** — Redis for session storage and performance
- **Search** — Elasticsearch or Algolia for full-text search
- **Testing** — Pytest for backend, Vitest for frontend
- **CI/CD** — GitHub Actions for automated testing and deployment

---

### **References**

- [Next.js Documentation](https://nextjs.org/docs)
- [Django Documentation](https://docs.djangoproject.com/)
- [React Documentation](https://react.dev/)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Vue.js Documentation](https://vuejs.org/guide/)
- [GSAP Documentation](https://greensock.com/gsap/)

---

**Last Updated:** 2026-09-16
**Version:** 1.0
