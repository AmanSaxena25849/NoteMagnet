from django.shortcuts import render
from notes.models import Notes

def home(request):
    if request.user:
        user_id = request.user.id
        my_notes = Notes.objects.filter(author = user_id, )[:2]
        all_notes = Notes.objects.filter(public=True)[:6]
        popular_notes = Notes.objects.filter(public=True).order_by('views_count')[:3]
    else:
        my_notes = []
    return render(request, "notes.html", {"my_notes":my_notes, "all_notes":all_notes, "popular_notes":popular_notes})