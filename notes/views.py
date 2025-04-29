from django.shortcuts import render, redirect, get_object_or_404
from .forms import NotesForm
from .models import Notes, Tags

# Create your views here.

def create_note(request):
    if request.method == 'POST':
        tag_list = request.POST.getlist('tags')
        data = request.POST.copy()
        data['auther'] = request.user.id 
        form = NotesForm(data, request.FILES)
        if form.is_valid():
            note = form.save()
            for tag_name in tag_list:
                tag, created = Tags.objects.get_or_create(tag_name = tag_name)
                note.tag.add(tag)
            return redirect('home')
            
        else:
            print(form.errors)
    else:        
        form = NotesForm()
        
    return render(request, "notes/create_note.html", {"form": form})


def view_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id)
    return render(request, 'notes/view_note.html', {'note':note})




    