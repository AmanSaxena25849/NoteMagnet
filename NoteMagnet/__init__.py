from .celery import app as celery_app

#initialize celery app
__all__ = ("celery_app",)