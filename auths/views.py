from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import SignUpForm, UserProfileForm
from django.contrib.auth import login, authenticate
from accounts.models import UserProfile
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('userProfile')
    else:
        form = SignUpForm()
    return render(request, 'auths/signup.html', {'form': form})

def userProfile(request):
    form = UserProfileForm()
    return render (request, 'auths/user-profile.html', {'form': form})

def baseConnect(request):
    users = UserProfile.objects.all()
    return render(request, 'auths/base-connect2.html', {'users': users})


    
    


