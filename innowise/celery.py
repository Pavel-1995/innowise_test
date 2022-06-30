import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "innowise.settings")
os.environ.setdefault("FORKED_BY_MULTIPROCESSING", "1")

app = Celery("innowise")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
