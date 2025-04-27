from django.urls import path, include
from .views import reauth_with_email, dashboard, delete_account, confirm_account_delete

urlpatterns = [
    path('', include('allauth.urls')),
    path('reauth/', reauth_with_email, name='reauth_with_email'),
    path('dashboard/', dashboard, name='dashboard'),
    path('confirm_account_delete/', confirm_account_delete, name="confirm_account_delete" ),
    path('delete_account/', delete_account, name="delete_account" ),
]
