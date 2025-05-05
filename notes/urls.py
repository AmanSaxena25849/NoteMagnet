from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_note, name='create_note'),
    path('view/<str:note_id>/', views.view_note, name="view_note"),
    path('delete/', views.delete_note, name="delete_note"),
    
    path('my_notes/', views.my_notes, name="my_notes"),
    path('my_notes/<str:order>/', views.my_notes, name="my_notes_order"),
    
    path('all_notes/', views.all_notes, name="all_notes"),
    path('all_notes/<str:order>/', views.all_notes, name="all_notes_order"),
]
