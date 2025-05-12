from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_note, name='create_note'),
    path('view/<str:note_id>/', views.view_note, name="view_note"),
    path('edit/<str:note_id>/', views.edit_note, name="edit_note"),
    path('delete/', views.delete_note, name="delete_note"),
    
    path('my_notes/', views.my_notes, name="my_notes"),
    path('my_notes/<str:order>/', views.my_notes, name="my_notes_order"),
    
    path('all_notes/', views.all_notes, name="all_notes"),
    
    path('bookmark/<str:note_id>/', views.bookmark_note, name="bookmark"),
    path('remove_bookmark/<str:note_id>/', views.remove_bookmark, name="remove_bookmark"),
]
