from django.urls import path
from .views import create_note, view_note

urlpatterns = [
    path('create/', create_note, name='create_note'),
    path('view/<str:note_id>', view_note, name="view_note"),
]
