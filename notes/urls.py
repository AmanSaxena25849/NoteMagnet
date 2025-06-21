from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_note, name='create_note'),
    path('view/<str:note_id>/', views.view_note, name="view_note"),
    path('edit/<str:note_id>/', views.edit_note, name="edit_note"),
    path('delete/', views.delete_note, name="delete_note"),
    
    path('all-notes/', views.all_notes, name="all_notes"),
    
    path('bookmark/<str:note_id>/', views.bookmark_note, name="bookmark"),
    path('remove-bookmark/<str:note_id>/', views.remove_bookmark, name="remove_bookmark"),
    
    path("like-note/<str:note_id>", views.like_note, name="like_note"),
    path("remove-like/<str:note_id>", views.remove_like, name="remove_like"),
    
    path("add-comment/<str:note_id>", views.add_comment, name="add_comment"),
    path("remove-comment/<str:note_id>/<str:comment_id>", views.remove_comment, name="remove_comment"),
    
    path('add-like/<str:comment_id>', views.like_comment , name="like"),
    path('add-dislike/<str:comment_id>', views.dislike_comment , name="dislike"),
    
    path('about-us', views.about_us, name="about_us")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)