from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import ProfileUpdateForm
from accounts.models import Profile

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("index")
    else:
        form = UserCreationForm()

    return render(request, "accounts/register.html", {"form": form})   

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form}) 

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def profile(request):
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, "Profile has been updated!")
            return redirect("profile")
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        "p_form": p_form
    }
    return render(request, "accounts/profile.html", context)