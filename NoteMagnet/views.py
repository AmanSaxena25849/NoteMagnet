from django.shortcuts import render
from notes.models import Notes

def home(request):
    if request.user:
        user_id = request.user.id
        my_notes = Notes.objects.filter(author = user_id, )[:2]
    else:
        my_notes = []
    return render(request, "notes.html", {"my_notes":my_notes})