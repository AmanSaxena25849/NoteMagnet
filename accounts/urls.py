from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('allauth.urls')),
    path('reauth/', views.reauth_with_email, name='reauth_with_email'),
    path('user-dashboard/',views.dashboard , name="dashboard" ),
    path('profile/', views.profile, name='profile'),
    path('confirm-account_delete/', views.confirm_account_delete, name="confirm_account_delete" ),
    path('delete-account/', views.delete_account, name="delete_account" ),
    path('follow/<str:author_id>', views.follow_author, name='follow'),
    path('unfollow/<str:author_id>', views.unfollow_author, name='unfollow'),
    path('author/<str:author_id>', views.author_page, name="author_page"),
]
