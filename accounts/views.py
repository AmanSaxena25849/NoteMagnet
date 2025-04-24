import os
from allauth.account.utils import send_email_confirmation
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from allauth.account.models import EmailAddress
from .forms import DashboardForm

# Create your views here.

@login_required
def reauth_with_email(request):
    send_email_confirmation(request, request.user, signup=False)
    return redirect('home')
    
    
    
def dashboard(request):
    user =request.user
    
    if request.method == 'POST':
        if user.profile_image:
            old_image = user.profile_image.path
        else:
            old_image = None
            
        form = DashboardForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            if form.is_valid():
                if old_image and 'profile_image' in request.FILES:
                    if os.path.isfile(old_image):
                        os.remove(old_image)

            form.save()
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
        
    return render(request, "account/dashboard.html", {"form":form})