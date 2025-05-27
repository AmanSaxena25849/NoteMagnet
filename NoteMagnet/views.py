from django.shortcuts import render
from notes.models import Notes
from django.core.cache import cache

def home(request):
    if request.user:
        user_id = request.user.id
        my_notes = Notes.objects.filter(author = user_id, )[:3]
        all_notes = cache.get('cached_all_notes')
        popular_notes = cache.get('cached_popular_notes')
        
        if all_notes and popular_notes:
            print('from cache')
            pass
        else: 
            all_notes = Notes.objects.filter(public=True)[:6]
            popular_notes = Notes.objects.filter(public=True).order_by('views_count')[:3]
            cache.set('cached_all_notes',all_notes, timeout=3600)
            cache.set('cached_popular_notes',popular_notes, timeout=3600)
            print("cached")
    else:
        my_notes = []
    return render(request, "notes.html", {"my_notes":my_notes, "all_notes":all_notes, "popular_notes":popular_notes})