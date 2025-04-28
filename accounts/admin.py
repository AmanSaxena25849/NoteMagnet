from django.contrib import admin
from allauth.account.models import get_user_model

# Register your models here.
users = get_user_model()
admin.site.register(users)