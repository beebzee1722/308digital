# Deployment Package - 308 Digital for GoDaddy Hosting

## What's Included

This deployment package contains everything needed to run 308 Digital on GoDaddy shared hosting.

### 📄 Documentation Files

| File | Purpose |
|------|---------|
| `DEPLOYMENT_GODADDY.md` | **MAIN** - Complete step-by-step deployment guide (70+ steps) |
| `QUICK_START.md` | Quick reference for experienced developers (5 steps) |
| `DEPLOYMENT_PACKAGE.md` | This file - overview of all deployment files |

### ⚙️ Configuration Files

| File | Purpose |
|------|---------|
| `passenger_wsgi.py` | ⭐ **CRITICAL** - Entry point for GoDaddy Passenger WSGI server |
| `.htaccess` | ⭐ **CRITICAL** - Apache configuration for Passenger routing |
| `digital_site/settings_production.py` | Production Django settings (database, security, etc.) |
| `.env.example` | Template for environment variables - copy to `.env` before deployment |
| `requirements.txt` | Python dependencies (Django, MySQL, etc.) |

### 🚀 Automation

| File | Purpose |
|------|---------|
| `deploy.sh` | Automated setup script - runs on GoDaddy server |

---

## Quick Deployment Checklist

- [ ] **Step 1**: Create MySQL database in cPanel (database name, user, password)
- [ ] **Step 2**: Upload project files to `public_html/mysite/`
- [ ] **Step 3**: Create `logs/` directory in `public_html/`
- [ ] **Step 4**: SSH into server and run `deploy.sh`
- [ ] **Step 5**: Create Python app in cPanel (Python 3.11.16)
- [ ] **Step 6**: Visit `28h.524.mytemp.website` to verify

---

## Key Files Explained

### passenger_wsgi.py
```python
# This is the main entry point for GoDaddy's Passenger WSGI server
# It loads Django and returns the WSGI application
# Location: ~/public_html/mysite/passenger_wsgi.py
# Referenced in cPanel → Python Apps → "passenger_wsgi.py"
```

### .htaccess
```
# Routes all requests through Passenger WSGI
# Handles compression, caching, security headers
# Location: ~/public_html/mysite/.htaccess
# Must be in the same directory as passenger_wsgi.py
```

### settings_production.py
```python
# Production-only Django settings
# - DEBUG = False
# - MySQL database configuration
# - Static/media file paths
# - Security settings
# - Email configuration (optional)
# Location: ~/digital_site/settings_production.py
# Loaded by: DJANGO_SETTINGS_MODULE=digital_site.settings_production (in .env)
```

### .env (from .env.example)
```
# Contains sensitive data:
# - Django SECRET_KEY
# - Database credentials
# - Email credentials (optional)
# Location: ~/public_html/mysite/.env
# MUST be in .gitignore - never commit to git!
# MUST have chmod 600 permissions
```

---

## Directory Structure on GoDaddy

After deployment, your directory structure should look like:

```
home/e1zcw712avko/
├── public_html/
│   ├── mysite/                    ← Application root
│   │   ├── passenger_wsgi.py      ← WSGI entry point
│   │   ├── .env                   ← Secret config (NOT in git)
│   │   ├── .htaccess              ← Apache config
│   │   ├── manage.py              ← Django CLI
│   │   ├── requirements.txt        ← Python dependencies
│   │   ├── deploy.sh              ← Setup script
│   │   ├── venv/                  ← Virtual environment (created by deploy.sh)
│   │   ├── digital_site/          ← Django project settings
│   │   │   ├── settings.py
│   │   │   ├── settings_production.py
│   │   │   ├── wsgi.py
│   │   │   └── urls.py
│   │   ├── pages/                 ← Django app (HTML templates, views)
│   │   └── db.sqlite3             ← Database (created by migrations)
│   ├── static/                    ← Static files (CSS, JS, images)
│   │   └── [collected by manage.py collectstatic]
│   └── logs/                      ← Application logs
│       ├── django.log             ← Django errors
│       └── passenger.log          ← Passenger WSGI errors
└── [other GoDaddy files]
```

---

## Environment Variables (.env)

The `.env` file contains these critical variables:

```bash
# Django Configuration
DJANGO_SETTINGS_MODULE=digital_site.settings_production  # Use production settings
DJANGO_SECRET_KEY=<random-50-char-string>               # MUST be unique and secret
DEBUG=False                                              # Never True in production

# Database (from cPanel)
DB_ENGINE=django.db.backends.mysql
DB_NAME=e1zcw712avko_308digital_db
DB_USER=e1zcw712avko_308digital_user
DB_PASSWORD=<your-database-password>
DB_HOST=localhost
DB_PORT=3306

# Domain
ALLOWED_HOSTS=28h.524.mytemp.website,www.28h.524.mytemp.website

# Security (enable after SSL certificate)
SECURE_SSL_REDIRECT=False  # Set to True with HTTPS
SESSION_COOKIE_SECURE=False # Set to True with HTTPS
```

---

## Deployment Workflow

### Before Uploading
1. ✅ All files are in git repo
2. ✅ `passenger_wsgi.py` created
3. ✅ `requirements.txt` updated with all dependencies
4. ✅ `settings_production.py` created
5. ✅ `.env.example` template provided

### On GoDaddy Server
1. Create database in cPanel
2. Upload files via SFTP to `public_html/mysite/`
3. Copy `.env.example` to `.env` and edit with credentials
4. Run `bash deploy.sh` (creates venv, installs deps, runs migrations)
5. Create Python app in cPanel (points to passenger_wsgi.py)
6. Site goes live! 🚀

---

## Support & Troubleshooting

### Common Issues

**Import Error: `ModuleNotFoundError: No module named 'django'`**
- Solution: Activate venv and install requirements
```bash
source venv/bin/activate
pip install -r requirements.txt
```

**Database Connection Error**
- Check `.env` has correct credentials
- Verify database exists in cPanel
- Test with: `mysql -u [user] -p -h localhost [database]`

**Static files not loading**
- Run: `python manage.py collectstatic --noinput`
- Check permissions: `chmod 755 ../static`

**Permission Denied**
- Fix with: `chmod 755 ~/public_html/mysite`

### View Logs

```bash
# Django errors
tail -f ~/logs/django.log

# Passenger WSGI errors  
tail -f ~/logs/passenger.log

# Check environment
cat ~/public_html/mysite/.env
```

---

## SSL Certificate (HTTPS)

Once you have an SSL certificate:

1. Update `.env`:
```bash
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

2. Uncomment HTTPS redirect in `.htaccess`:
```apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

3. Restart Passenger app in cPanel

---

## Contact Form Email (Optional)

To enable email notifications when users submit contact form:

1. Get SMTP credentials (Gmail or GoDaddy email)
2. Add to `.env`:
```bash
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

3. Code already handles this in `pages/views.py`

---

## Version Information

- **Django**: 6.1.1
- **Python**: 3.11.16 (on GoDaddy)
- **MySQL**: 5.7+ (GoDaddy default)
- **Hosting**: GoDaddy Shared Hosting with Passenger WSGI
- **Deployment Date**: 2026-10-04

---

## Next Steps After Deployment

1. ✅ Verify site is live at `28h.524.mytemp.website`
2. ✅ Test contact form submissions
3. ✅ Create Django superuser account
4. ✅ Access admin at `/admin`
5. ✅ Set up SSL certificate (get free from GoDaddy AutoSSL)
6. ✅ Update `.env` for HTTPS when certificate is ready
7. ✅ Set up regular database backups in cPanel
8. ✅ Monitor logs for errors

---

## File Checklist

Before uploading, verify these files are ready:

- [x] `passenger_wsgi.py` - WSGI entry point
- [x] `.htaccess` - Apache configuration
- [x] `.env.example` - Environment template
- [x] `requirements.txt` - Python dependencies
- [x] `digital_site/settings_production.py` - Production Django settings
- [x] `deploy.sh` - Automation script
- [x] `_docs/DEPLOYMENT_GODADDY.md` - Full documentation
- [x] `_docs/QUICK_START.md` - Quick reference
- [x] All Django app files (manage.py, pages/, digital_site/, etc.)

---

**Package prepared**: 2026-10-04
**Last updated**: 2026-10-04
