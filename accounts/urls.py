from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('allauth.urls')),
    path('reauth/', views.reauth_with_email, name='reauth_with_email'),
    path('user_dashboard/',views.dashboard , name="dashboard" ),
    path('profile/', views.profile, name='profile'),
    path('confirm_account_delete/', views.confirm_account_delete, name="confirm_account_delete" ),
    path('delete_account/', views.delete_account, name="delete_account" ),
    path('follow/<str:author_id>', views.follow_author, name='follow'),
    path('unfollow/<str:author_id>', views.unfollow_author, name='unfollow'),
    
]
