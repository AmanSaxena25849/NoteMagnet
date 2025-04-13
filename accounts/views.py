from django.shortcuts import render, redirect
from .forms import SignupForm

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'])
            form.save()
            return redirect("redirect")
        else:
            print(form.errors)
    else:
        form = SignupForm()
        
    return render(request, "accounts/signup.html", {"form": form})
 

def redirect_page(request):
    return render(request, "accounts/redirect.html")
    