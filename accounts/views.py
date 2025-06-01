import os
from allauth.account.utils import send_email_confirmation
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from allauth.account.models import  get_user_model
from .forms import DashboardForm
from django.contrib import messages
from notes.models import Notes
from django.db import transaction
from django.contrib.admin.views.decorators import staff_member_required
from .tasks import send_notification

# Create your views here.

@login_required
def reauth_with_email(request):
    """Sends confirmation mail to user upon signup. 
    Returns:
       redirects user to home page.
    """
    send_email_confirmation(request, request.user, signup=False)
    return redirect('home')
    
    
@login_required
def dashboard(request):
    user_id = request.user.id
    my_notes = Notes.objects.filter(author=user_id).order_by('-created_at').prefetch_related('tag')
    liked_notes = request.user.like.all()
    bookmarks = request.user.bookmark.all()
    following_authors = request.user.following.all()
    
    return render(request, 'account/dashboard.html', {'my_notes':my_notes, "liked_notes":liked_notes, "bookmarks":bookmarks,"following_authors":following_authors })  

    
@login_required
@transaction.atomic    
def profile(request):
    """view for showing and updating user profile. 

    Args:
        request (_type_): request object

    Returns:
        renders user profile.
    """
    user =request.user
    
    if request.method == 'POST':
        #for keeping old user profile image.
        if user.profile_image:
            old_image = user.profile_image.path
        else:
            old_image = None
            
        form = DashboardForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            #for updaing user profile image if its changed.
            if old_image and 'profile_image' in request.FILES:
                if os.path.isfile(old_image):
                    os.remove(old_image)

            form.save()
            messages.success(request, "Your bio has been successfully updated!")
            return redirect('profile')
        
    else:
        form = DashboardForm(initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'username': request.user.username,
            'age': request.user.age,
            'email': request.user.email,
            'bio': request.user.bio,
            })
        
    return render(request, "account/profile.html", {"form":form})


@login_required
def confirm_account_delete(request):
    return render(request, 'account/confirm_account_delete.html')


@login_required
@transaction.atomic 
def delete_account(request):
    if request.method == "POST": 
        user:str = request.user
        UserModel = get_user_model()
        UserModel.objects.get(username=user).delete()
        messages.success(request, "Your account has been successfully deleted!")
        return redirect('home')
    else:
        messages.error(request, "Incorrect deletion request. Please try again.")
        return redirect('dashboard')


def author_page(request, author_id):
    author = get_user_model().objects.get(id=author_id)
    authors_notes = Notes.objects.filter(author=author_id, public=True).order_by('-created_at').prefetch_related('tag')
    is_following = False
    
    if request.user.is_authenticated:
        is_following = request.user.following.filter(id=author.id).exists()
        
    return render(request, "account/author_page.html", {"author":author, "author_notes":authors_notes, "is_following":is_following})   


@login_required
def follow_author(request, author_id):
    if request.method == 'POST':
        author = get_user_model().objects.get(id=author_id)
        request.user.following.add(author)
        messages.success(request, f"You followed {author.username}")
        return redirect(author_page, author_id=author_id)
    else:
        messages.error(request, "Failed to follow.")
        return redirect(author_page, author_id=author_id)   


@login_required
def unfollow_author(request, author_id):
    if request.method == 'POST':
        author = get_user_model().objects.get(id=author_id)
        request.user.following.remove(author)
        messages.success(request, f"You unfollowed {author.username}")
        return redirect(author_page, author_id=author_id)
    else:
        messages.error(request, "Failed to unfollow.")
        return redirect(author_page, author_id=author_id)   
    

@staff_member_required
def send_bulk_notifications(request):
    """sends notication to all users by staff members."""
    if request.method == "POST":
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        send_notification.delay(subject, message)
        messages.success(request, "Notification is being sent in the background.")
        return redirect('home')
    
    return render(request, "account/send_notifcation.html")
        
 