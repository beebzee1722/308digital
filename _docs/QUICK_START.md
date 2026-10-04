# Quick Start: Deploy to GoDaddy in 5 Steps

This is a condensed version. See `DEPLOYMENT_GODADDY.md` for detailed instructions.

## Your Info
- **Domain**: `28h.524.mytemp.website`
- **cPanel User**: `e1zcw712avko`
- **Server IP**: `92.205.174.198`
- **SSH Host**: `e1zcw712avko@92.205.174.198`

---

## Step 1: Database Created ✅
Already done! Your database details:
- **Database**: `308_digita`
- **User**: `admin_308`
- **Password**: `diGit@l@308_bankSolut!0n`
- **Host**: `localhost`

---

## Step 2: Upload Files via SFTP
```bash
sftp e1zcw712avko@92.205.174.198
# Then upload all files to: public_html/mysite/
```

Or use FileZilla / cPanel File Manager

---

## Step 3: Configure & Deploy
SSH into server:
```bash
ssh e1zcw712avko@92.205.174.198
cd ~/public_html/mysite

# Copy the production environment file
cp .env.production .env

# Run deployment script
bash deploy.sh
```

---

## Step 4: Create Python App in cPanel
1. Go to: Applications → Python
2. Click: CREATE APPLICATION
3. Fill in:
   - Python: 3.11.16
   - Root: mysite
   - URL: 28h.524.mytemp.website
   - Startup: passenger_wsgi.py
   - Entry: application

---

## Step 5: Visit Your Site
Open: `http://28h.524.mytemp.website`

You should see 308 Digital homepage! 🎉

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Import error | `source venv/bin/activate && pip install -r requirements.txt` |
| Database error | Check database credentials in `.env` |
| Static files missing | `python manage.py collectstatic --noinput` |
| Permission denied | `chmod 755 ~/public_html/mysite` |

---

## Admin Panel
Access Django admin at: `http://28h.524.mytemp.website/admin`

(Create superuser in Step 3: `python manage.py createsuperuser`)

---

See `DEPLOYMENT_GODADDY.md` for full documentation.
