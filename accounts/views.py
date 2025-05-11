import os
from allauth.account.utils import send_email_confirmation
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from allauth.account.models import  get_user_model
from django.contrib.auth.models import User
from .forms import DashboardForm
from django.contrib import messages
from notes.models import Notes

# Create your views here.

@login_required
def reauth_with_email(request):
    send_email_confirmation(request, request.user, signup=False)
    return redirect('home')
    
    
@login_required
def dashboard(request):
    user_id = request.user.id
    my_notes = Notes.objects.filter(author=user_id).order_by('-created_at').prefetch_related('tag')
    return render(request, 'account/dashboard.html', {'my_notes':my_notes})  

    
@login_required    
def profile(request):
    user =request.user
    
    if request.method == 'POST':
        if user.profile_image:
            old_image = user.profile_image.path
        else:
            old_image = None
            
        form = DashboardForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            if old_image and 'profile_image' in request.FILES:
                if os.path.isfile(old_image):
                    os.remove(old_image)

            form.save()
            messages.success(request, "Your bio has been successfully updated!")
            return redirect('dashboard')
        
    else:
        form = DashboardForm(initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'username': request.user.username,
            'age': request.user.age,
            'phone_number': request.user.phone_number,
            'email': request.user.email,
            'bio': request.user.bio,
            })
        
    return render(request, "account/profile.html", {"form":form})


@login_required
def confirm_account_delete(request):
    return render(request, 'account/confirm_account_delete.html')


@login_required
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
    
    

    
 