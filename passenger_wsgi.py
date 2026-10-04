"""
WSGI entry point for GoDaddy Passenger WSGI deployment
"""
import os
import sys
from pathlib import Path

# Load environment variables from .env file with absolute path
from dotenv import load_dotenv
env_file = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_file)

# Add user site-packages to path for installed packages
user_site = os.path.expanduser("~/.local/lib/python3.11/site-packages")
if user_site not in sys.path:
    sys.path.insert(0, user_site)

# Add the project directory to the Python path
project_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(project_dir))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digital_site.settings_production')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application

# Create the WSGI application
application = get_wsgi_application()
