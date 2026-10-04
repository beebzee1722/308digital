# Deployment Guide: 308 Digital on GoDaddy Shared Hosting

## Overview
This guide walks you through deploying the 308 Digital Django application to GoDaddy shared hosting with Passenger WSGI.

### Account Details (from your GoDaddy dashboard)
- **Domain**: `28h.524.mytemp.website`
- **cPanel Username**: `e1zcw712avko`
- **IP Address**: `92.205.174.198`
- **Python Version**: 3.11.16
- **Data Center**: Europe

---

## Step 1: Set Up Database (MySQL on GoDaddy)

### 1.1 Create MySQL Database in cPanel
1. Log in to cPanel: `https://92.205.174.198:2083/`
2. Navigate: **Databases → MySQL Databases**
3. Create a new database:
   - **Database Name**: `308digital_db`
   - Note the full name (usually `e1zcw712avko_308digital_db`)

4. Create a MySQL user:
   - **Username**: `308digital_user`
   - **Password**: Create a strong password (e.g., `SecurePass123!`)
   - Note the full username (usually `e1zcw712avko_308digital_user`)

5. Add user to database:
   - Grant **ALL PRIVILEGES**

### 1.2 Note Down Database Credentials
Save these for Step 4:
```
Database Name: e1zcw712avko_308digital_db
Username: e1zcw712avko_308digital_user
Password: [Your password]
Host: localhost
Port: 3306
```

---

## Step 2: Upload Django Files

### 2.1 Connect via SFTP
Use an SFTP client (FileZilla, Cyberduck, or Terminal):

**For Mac Terminal:**
```bash
sftp e1zcw712avko@92.205.174.198
```

Or use your cPanel file manager directly.

### 2.2 Upload Project Files
1. Create directory: `public_html/mysite/`
2. Upload these files to `public_html/mysite/`:
   - `manage.py`
   - `digital_site/` folder
   - `pages/` folder
   - `passenger_wsgi.py` ⭐ (NEW)
   - `requirements.txt` ⭐ (NEW)
   - All other project files

**Important**: Don't upload:
- `.venv/` or `venv/` folder
- `node_modules/` folder
- `.git/` folder
- `__pycache__/` folders
- `.env` file (create it on server instead)

### 2.3 Create Logs Directory
In `public_html/`, create a `logs/` folder:
```
public_html/
├── logs/          ← Create this
├── mysite/        ← Django files here
├── static/        ← Will be created later
└── media/         ← For user uploads
```

---

## Step 3: Install Python Dependencies

### 3.1 Connect via SSH
```bash
ssh e1zcw712avko@92.205.174.198
```

### 3.2 Navigate to Project
```bash
cd ~/public_html/mysite
```

### 3.3 Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3.4 Install Requirements
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3.5 Verify Installation
```bash
pip list
```
Should show: Django, mysqlclient, pytest, pytest-django, python-dotenv

---

## Step 4: Configure Environment Variables

### 4.1 Create .env File
In `public_html/mysite/`, create `.env`:

```bash
# Django settings
DJANGO_SETTINGS_MODULE=digital_site.settings_production
DJANGO_SECRET_KEY=your-secret-key-here-change-this-to-random-string
DEBUG=False

# Database (from Step 1)
DB_ENGINE=django.db.backends.mysql
DB_NAME=e1zcw712avko_308digital_db
DB_USER=e1zcw712avko_308digital_user
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=3306

# Domain
ALLOWED_HOSTS=28h.524.mytemp.website,www.28h.524.mytemp.website
```

⚠️ **IMPORTANT**: Replace placeholder values with your actual credentials!

### 4.2 Generate Secure Secret Key
In your local machine, generate a secure key:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Copy that value to `DJANGO_SECRET_KEY` in `.env`

### 4.3 Set Permissions
```bash
chmod 600 .env  # Only owner can read
```

---

## Step 5: Set Up Django for Production

### 5.1 Collect Static Files
```bash
source venv/bin/activate
cd ~/public_html/mysite
python manage.py collectstatic --noinput
```

### 5.2 Run Database Migrations
```bash
source venv/bin/activate
cd ~/public_html/mysite
python manage.py migrate
```

### 5.3 Create Superuser (Optional - for Django Admin)
```bash
source venv/bin/activate
cd ~/public_html/mysite
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

---

## Step 6: Set Up Python App in cPanel

### 6.1 Go to Python Apps
1. Log in to cPanel
2. Navigate: **Applications → Python**
3. Click **CREATE APPLICATION**

### 6.2 Configure Application
Fill in these values:

| Field | Value |
|-------|-------|
| **Python version** | 3.11.16 |
| **Application root** | mysite |
| **Application URL** | 28h.524.mytemp.website |
| **Application startup file** | passenger_wsgi.py |
| **Application Entry point** | application |
| **Passenger log file** | /home/e1zcw712avko/logs/passenger.log |

### 6.3 Environment Variables (in cPanel)
Add these in the Python app configuration:

```
DJANGO_SETTINGS_MODULE = digital_site.settings_production
DJANGO_SECRET_KEY = [your-secret-key]
DB_NAME = e1zcw712avko_308digital_db
DB_USER = e1zcw712avko_308digital_user
DB_PASSWORD = [your-password]
```

### 6.4 Click CREATE
GoDaddy will set up the Passenger WSGI configuration.

---

## Step 7: Verify Deployment

### 7.1 Check Website
Visit: `http://28h.524.mytemp.website`

You should see the 308 Digital homepage!

### 7.2 Check Logs (if issues)
```bash
# Django logs
tail -f ~/logs/django.log

# Passenger logs
tail -f ~/logs/passenger.log

# Check Python app status in cPanel
```

### 7.3 Test Django Admin
Visit: `http://28h.524.mytemp.website/admin`

Login with the superuser account you created.

---

## Step 8: Set Up SSL Certificate (HTTPS)

### 8.1 Get Free SSL in cPanel
1. Go to **Security → AutoSSL**
2. Install the free SSL certificate

### 8.2 Update Django Settings
Once SSL is installed, update `.env`:
```
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

And uncomment the HTTPS redirect in `.htaccess`

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'django'"
**Solution**: Make sure virtual environment is activated and requirements are installed:
```bash
source ~/public_html/mysite/venv/bin/activate
pip install -r requirements.txt
```

### Issue: "django.core.exceptions.ImproperlyConfigured"
**Solution**: Check `.env` file exists and environment variables are set correctly:
```bash
cat ~/public_html/mysite/.env
```

### Issue: Database connection error
**Solution**: Verify database credentials in `.env`:
```bash
# In SSH, test connection
mysql -u e1zcw712avko_308digital_user -p -h localhost e1zcw712avko_308digital_db
```

### Issue: Static files not loading
**Solution**: Run collectstatic again:
```bash
source ~/public_html/mysite/venv/bin/activate
python manage.py collectstatic --noinput
```

### Issue: Permission denied errors
**Solution**: Check file permissions:
```bash
chmod 755 ~/public_html/mysite
chmod 644 ~/public_html/mysite/*.py
chmod 755 ~/public_html/mysite/digital_site
```

---

## Maintenance

### Regular Updates
Keep dependencies updated:
```bash
source ~/public_html/mysite/venv/bin/activate
pip install --upgrade -r requirements.txt
```

### Database Backups
Regularly backup your MySQL database through cPanel → **Backups**

### Monitor Logs
Check logs regularly for errors:
```bash
tail -20 ~/logs/django.log
tail -20 ~/logs/passenger.log
```

### Django Management Commands
You can run Django commands via SSH:
```bash
source ~/public_html/mysite/venv/bin/activate
cd ~/public_html/mysite
python manage.py [command]
```

---

## Contact Form Setup

The contact form is already configured to work with Django's email backend.

To enable email notifications when someone submits a contact form:

1. Configure email in `.env`:
   ```
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   ```

2. Or use GoDaddy's email service (check cPanel for SMTP settings)

---

## Support

If you encounter issues:

1. **Check logs**: Look at Django and Passenger logs
2. **SSH into server**: Debug directly
3. **Contact GoDaddy**: If it's a server/database issue
4. **Check Django docs**: https://docs.djangoproject.com/

---

**Last Updated**: 2026-10-04
