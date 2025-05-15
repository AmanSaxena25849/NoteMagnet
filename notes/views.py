from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import NotesForm, EditNoteForm
from .models import Notes, Tags
from django.core.paginator import Paginator

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
    tags = note.tag.all()
    is_following = False
    
    #code to add view and follow
    if request.user.is_authenticated:
        note.views_count.add(request.user)
        is_following = request.user.following.filter(id=note.author.id).exists()
               

    
    query = Q()
    for i, tag in enumerate(tags[:2]): 
        if i == 0:
            query = Q(title__icontains=tag.tag_name) | Q(content__icontains=tag.tag_name)
        else:
            query = query | Q(title__icontains=tag.tag_name) | Q(content__icontains=tag.tag_name)
    
    query = query | Q(content__icontains="the")        
    related_notes = Notes.objects.filter(query).exclude(title=note.title)
    
    return render(request, 'notes/view_note.html', {'note':note, 'related_notes':related_notes[0:2], 'is_following':is_following})


@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id)
    
    # retain old image to be used if not provided.
    old_image = note.note_image 
    
    if note.author == request.user:
        if request.method == 'POST':
            tag_list = request.POST.getlist('tags')
            form = EditNoteForm(request.POST, request.FILES, instance=note)
            
            if form.is_valid():
                update_note = form.save(commit=False)
                
                # If no new image uploaded, keep the old one
                if not request.FILES.get('note_image'):
                    update_note.note_image = old_image
                       
                update_note.save()
                    
                #remove old and add new tags for the note.
                note.tag.clear()
                for tag_name in tag_list:
                    tag, created = Tags.objects.get_or_create(tag_name = tag_name)
                    note.tag.add(tag)
                    
                messages.success(request, "Your note has been updated successfully!")
                return redirect('view_note', note_id=note_id)
                
            else:
                print(form.errors)
        else:
            form = EditNoteForm(instance=note)
            return render(request, "notes/edit_note.html", {'form':form, 'note':note})
    else:
        messages.error(request, "Can not edit notes from other users.")
        return redirect("view_note", note_id=note_id)



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
 


def all_notes(request):
    query = request.GET.get('search')
    order = request.GET.get('filter') or "-created_at"
    
    if query:
        all_notes = Notes.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))   
    else:
        all_notes = Notes.objects.filter(public=True).prefetch_related('tag')
        
    all_notes = all_notes.order_by(order)

    return render(request, "notes/all_notes.html", {"all_notes":all_notes})


@login_required
def bookmark_note(request, note_id):
    if request.method == "POST":
        note = Notes.objects.get(id=note_id)
        request.user.bookmark.add(note)
        messages.success(request, "Note bookmarked.")
        return redirect('view_note', note_id=note_id)
    
    else:
        messages.error(request, "Failed to add to Bookmark.")
        return redirect('view_note', note_id=note_id)
    
   
@login_required  
def remove_bookmark(request, note_id):
    if request.method == "POST":
        note = Notes.objects.get(id=note_id)
        request.user.bookmark.remove(note)
        messages.success(request, "Note removed from bookmarks.")
        return redirect('view_note', note_id=note_id)
    
    else:
        messages.error(request, "Failed to remove to Bookmark.")
        return redirect('view_note', note_id=note_id)

    