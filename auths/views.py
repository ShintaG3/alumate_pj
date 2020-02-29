from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import SignUpForm, UserProfileForm
from django.contrib.auth import login, authenticate
from accounts.models import UserProfile, Follow
from django.http import JsonResponse
from django.contrib.auth.models import User
# Create your views here.
def userProfile(request):
    form = UserProfileForm()
    return render (request, 'auths/user-profile.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('auths:userProfile')
    else:
        form = SignUpForm()
    return render(request, 'auths/signup.html', {'form': form})


def baseConnect(request):
    futures = UserProfile.objects.filter(status='future')[:4]
    students = UserProfile.objects.filter(status='student')[:4]
    alumnis = UserProfile.objects.filter(status='alumni')[:4]
    context = {
        'futures': futures,
        'students': students,
        'alumnis': alumnis
    }
    return render(request, 'auths/base-connect2.html', context=context)

def follow(request):
    followed_id = request.GET.get('follow', None)
    followed = UserProfile.objects.get(id=followed_id).user
    follower = User.objects.get(username=request.user.username)
    follow = Follow.objects.create(follower=follower, followed=followed)
    data = {
        'success': followed_id
    }
    return JsonResponse(data)