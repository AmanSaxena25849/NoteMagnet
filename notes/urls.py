from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_note, name='create_note'),
    path('view/<str:note_id>/', views.view_note, name="view_note"),
    path('edit/<str:note_id>/', views.edit_note, name="edit_note"),
    path('delete/', views.delete_note, name="delete_note"),
    
    path('all_notes/', views.all_notes, name="all_notes"),
    
    path('bookmark/<str:note_id>/', views.bookmark_note, name="bookmark"),
    path('remove_bookmark/<str:note_id>/', views.remove_bookmark, name="remove_bookmark"),
    
    path("like_note/<str:note_id>", views.like_note, name="like_note"),
    path("remove_like/<str:note_id>", views.remove_like, name="remove_like"),
    
    path('about_us', views.about_us, name="about_us")
]
