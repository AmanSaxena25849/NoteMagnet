from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Count
from .forms import NotesForm, EditNoteForm
from .models import Notes, Tags, Comments
from django.db import transaction
from django.core.cache import cache
from .tasks import send_note_notification

# Create your views here.
@login_required
@transaction.atomic
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
            
            if note.notifications == True:
                users = request.user.following.all()
                send_note_notification.delay(title=note.title,
                                            message=note.content, users=list(users.values_list("email", flat=True)),
                                            author=request.user.username)
            
            messages.success(request, "Your note has been created successfully!")
            return redirect('dashboard')
            
        else:
            print(form.errors)
    else:        
        form = NotesForm()
        
   
        
    return render(request, "notes/create_note.html", {"form": form})



def view_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id)
    tags = note.tag.all()
    is_following = False
    liked = False
    
    #code to add view and follow
    if request.user.is_authenticated:
        note.views_count.add(request.user)
        is_following = request.user.following.filter(id=note.author.id).exists()
        liked = request.user.like.filter(id=note_id).exists()
    
    query = Q()
    for i, tag in enumerate(tags[:2]): 
        if i == 0:
            query = Q(title__icontains=tag.tag_name) | Q(content__icontains=tag.tag_name)
        else:
            query = query | Q(title__icontains=tag.tag_name) | Q(content__icontains=tag.tag_name)
    
    query = query | Q(content__icontains="the")        
    comments = note.comments.all()
    related_notes = Notes.objects.filter(query).exclude(title=note.title)
    
    return render(request, 'notes/view_note.html', {'note':note, 'comments':comments, 'related_notes':related_notes[0:2], 'is_following':is_following, 'liked':liked})



@login_required
@transaction.atomic
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
@transaction.atomic
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
    
    filter_map = {
        "-created_at": "newest first",
        "-title": "title (A-Z)",
        "title": "title (A-Z)",
        "views_count": "most popular"
    }
    filter_label= filter_map.get(order, "Newest First")
    
    if query:
        all_notes = Notes.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))   
    else:
        all_notes = Notes.objects.filter(public=True).prefetch_related('tag')
    
    if "views_count" in order:
        popular_notes = cache.get('popular_note')
        if popular_notes:
            print("from_cache")
            all_notes = popular_notes
        else:
            print("cache_set")
            all_notes = all_notes.annotate(num_views=Count("views_count"))
            order = order.replace("views_count", "-num_views")
            all_notes = all_notes.order_by(order)
            cache.set('popular_note', all_notes, timeout=3600)


    return render(request, "notes/all_notes.html", {"all_notes":all_notes, "filter_label":filter_label})



@login_required
def bookmark_note(request, note_id:str):
    if request.method == "POST":
        note = Notes.objects.get(id=note_id)
        request.user.bookmark.add(note)
        messages.success(request, "Note bookmarked.")
        return redirect('view_note', note_id=note_id)
    
    else:
        messages.error(request, "Failed to add to Bookmark.")
        return redirect('view_note', note_id=note_id)
    

   
@login_required  
def remove_bookmark(request, note_id:str):
    if request.method == "POST":
        note = Notes.objects.get(id=note_id)
        request.user.bookmark.remove(note)
        messages.success(request, "Note removed from bookmarks.")
        return redirect('view_note', note_id=note_id)
    
    else:
        messages.error(request, "Failed to remove from Bookmarks.")
        return redirect('view_note', note_id=note_id)



@login_required
def like_note(request, note_id:str):
    if request.method == "POST":
        note = Notes.objects.get(id=note_id)
        request.user.like.add(note)
        messages.success(request, "Note liked.")
        return redirect('view_note', note_id=note_id)
    
    else:
        messages.error(request, "Failed to like the note.")
        return redirect('view_note', note_id=note_id)



@login_required  
def remove_like(request, note_id:str):
    if request.method == "POST":
        note = Notes.objects.get(id=note_id)
        request.user.like.remove(note)
        messages.success(request, "Note removed from likes.")
        return redirect('view_note', note_id=note_id)
    
    else:
        messages.error(request, "Failed to remove from likes.")
        return redirect('view_note', note_id=note_id)



@login_required
@transaction.atomic
def add_comment(request, note_id:str):
    note = get_object_or_404(Notes, id=note_id)

    if request.method == "POST": 
        Comments.objects.create(note=note, author=request.user, comment=request.POST.get("comment"))
        
        comments = note.comments.all()
        return render(request, "notes/view_note_partials/comment.html", {"comments":comments, "note": note })

    messages.error(request, "Failed to add the comment!")
    return redirect("view_note", note_id=note.id)
   

    
@login_required
@transaction.atomic
def remove_comment(request, note_id:str, comment_id:str): 
    if request.method == "POST":
        
        comment = get_object_or_404(Comments, id=comment_id)
        comment.delete()
        
        note = get_object_or_404(Notes, id=note_id)
        comments = note.comments.all()
        
        return render(request, "notes/view_note_partials/comment.html", {"comments": comments, "note": note })
    else:
        messages.error(request, "Failed to remove comment!")
        return redirect('view_note', note_id=note_id)



@login_required
def like(request, comment_id:str):
    if request.method == 'POST':
        comment = get_object_or_404(Comments, id=comment_id)
        user = request.user
        status = ""
        
        if user in comment.liked_by.all():
            comment.liked_by.remove(user)  
        else:
            comment.liked_by.add(user)     
            comment.disliked_by.remove(user)
            status = "liked"
        
            
        return render(request, "notes/view_note_partials/like_dislike.html", {"status":status, "comment":comment})
    
    
    
@login_required
def dislike(request, comment_id:str):
    if request.method == 'POST':
        comment = get_object_or_404(Comments, id=comment_id)
        user = request.user
        status = ""
        
        if user in comment.disliked_by.all():
            comment.disliked_by.remove(user)  
        else:
            comment.disliked_by.add(user)     
            comment.liked_by.remove(user)
            status = "disliked"
        
            
        return render(request, "notes/view_note_partials/like_dislike.html", {"status":status, "comment":comment})
    
    
    
def about_us(request):
    return render(request, "notes/about_us.html")    