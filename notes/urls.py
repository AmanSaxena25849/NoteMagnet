from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_note, name='create_note'),
    path('view/<str:note_id>', views.view_note, name="view_note"),
    path('my_notes/', views.my_notes, name="my_notes")
]
