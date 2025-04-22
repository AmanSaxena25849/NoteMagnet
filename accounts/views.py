from allauth.account.utils import send_email_confirmation
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from allauth.account.models import EmailAddress

# Create your views here.

@login_required
def reauth_with_email(request):
    send_email_confirmation(request, request.user, signup=False)
    return redirect('home')
    
    
def dashboard(request):
    return render(request, "account/dashboard.html")