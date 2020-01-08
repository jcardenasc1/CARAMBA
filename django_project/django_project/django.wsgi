import os
import sys

sys.path.append('/home/django/django_project')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


