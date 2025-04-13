from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('redirect/', views.redirect_page, name='redirect'),
]
