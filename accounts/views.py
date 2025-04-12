from django.shortcuts import render
from .forms import SignupForm

# Create your views here.

def signup(request):
    form = SignupForm
    return render(request, "accounts/signup.html", {"form": form})
 
