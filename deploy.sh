#!/bin/bash

# 308 Digital - GoDaddy Deployment Setup Script
# Run this script on GoDaddy server after uploading files
# Usage: bash deploy.sh

set -e

echo "=========================================="
echo "308 Digital - GoDaddy Deployment Setup"
echo "=========================================="

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if .env exists
if [ ! -f .env ]; then
    echo -e "${RED}Error: .env file not found!${NC}"
    echo "Please copy .env.example to .env and configure it first:"
    echo "  cp .env.example .env"
    echo "  nano .env  # Edit with your database credentials"
    exit 1
fi

echo -e "${YELLOW}Step 1: Creating virtual environment...${NC}"
python3 -m venv venv
source venv/bin/activate

echo -e "${YELLOW}Step 2: Upgrading pip...${NC}"
pip install --upgrade pip setuptools wheel

echo -e "${YELLOW}Step 3: Installing Python dependencies...${NC}"
pip install -r requirements.txt

echo -e "${YELLOW}Step 4: Setting permissions...${NC}"
chmod 600 .env
chmod 755 ..
chmod 644 passenger_wsgi.py

echo -e "${YELLOW}Step 5: Running database migrations...${NC}"
python manage.py migrate

echo -e "${YELLOW}Step 6: Collecting static files...${NC}"
python manage.py collectstatic --noinput

echo ""
echo -e "${GREEN}=========================================="
echo "✓ Deployment setup complete!"
echo "=========================================${NC}"
echo ""
echo "Next steps:"
echo "1. Create a superuser (optional):"
echo "   python manage.py createsuperuser"
echo ""
echo "2. Go to cPanel and create Python app with these settings:"
echo "   - Python version: 3.11.16"
echo "   - Application root: mysite"
echo "   - Application URL: 28h.524.mytemp.website"
echo "   - Application startup file: passenger_wsgi.py"
echo "   - Application Entry point: application"
echo ""
echo "3. Visit your site: http://28h.524.mytemp.website"
echo ""
echo "For detailed instructions, see _docs/DEPLOYMENT_GODADDY.md"
