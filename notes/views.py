from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import NotesForm
from .models import Notes, Tags

# Create your views here.
@login_required
def create_note(request):
    if request.method == 'POST':
        tag_list = request.POST.getlist('tags')
        data = request.POST.copy()
        data['author'] = request.user.id 
        form = NotesForm(data, request.FILES)
        
        if form.is_valid():
            note = form.save(commit=False)
            
            if not request.FILES.get('note_image'):
                note.note_image = "note_image/note_default.png"
            
            note.save()
            for tag_name in tag_list:
                tag, created = Tags.objects.get_or_create(tag_name = tag_name)
                note.tag.add(tag)
            messages.success(request, "Your note has been created successfully!")
            return redirect('my_notes')
            
        else:
            print(form.errors)
    else:        
        form = NotesForm()
        
    return render(request, "notes/create_note.html", {"form": form})


def view_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id)
    return render(request, 'notes/view_note.html', {'note':note})


@login_required
def delete_note(request):
    if request.method == "POST":
        note_id = request.POST.get("note_id")
        try:
            note = Notes.objects.get(id=note_id)
            note.delete()
            messages.success(request, "Note deleted successfully!")
            return redirect("all_notes")
        except Notes.DoesNotExist:
            messages.error(request, "Note not found!")
            return redirect(f"view_note/{note_id}")
    else:
        messages.error(request, "Something went wrong, please try again.")
        return redirect("home")
       

@login_required
def my_notes(request, order="-created_at"):
    user_id = request.user.id
    my_notes = Notes.objects.filter(author_id=user_id).order_by(order).prefetch_related('tag')
    return render(request, "notes/my_notes.html", {"my_notes":my_notes})


def all_notes(request, order="-created_at"):
    all_notes = Notes.objects.filter(public=True).order_by(order).prefetch_related('tag')
    return render(request, "notes/all_notes.html", {"all_notes":all_notes})




    