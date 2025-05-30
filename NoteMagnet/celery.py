from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

#get settings file for the projcet
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NoteMagnet.settings")

#intialize the project for celery
app = Celery("NoteMagnet")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

