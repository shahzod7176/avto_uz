from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set default Django settings module for 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

# Create the Celery application instance
app = Celery('root')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery will automatically discover tasks in your Django apps
app.autodiscover_tasks()
