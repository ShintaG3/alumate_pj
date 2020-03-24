from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import SignUpForm, BaseInfoForm, UserLoginForm
from django.contrib.auth import login as auth_login, authenticate, logout
from accounts.models import UserProfile, Follow, BaseInfo
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView


def baseInquiry(request):
    if request.method == 'POST':
        form = BaseInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auths:baseConnect')
    else:
        form = BaseInfoForm()
    return render (request, 'auths/base-inquiry.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('auths:baseInquiry')
    else:
        form = SignUpForm()
    return render(request, 'auths/register.html', {'form': form})

def loginUser(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            # print(request.session.get_session_cookie_age())
            request.session.set_expiry(0)
            # print(request.session.get_session_cookie_age())
        user = authenticate(username=username, password=password)
        auth_login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "auths/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def baseConnect(request):
    user1 = User.objects.get(username=request.user.username)
    futures = BaseInfo.objects.filter(status='future')[:4]
    students = BaseInfo.objects.filter(status='student')[:4]
    alumnis = BaseInfo.objects.filter(status='alumni')[:4]
    context = {
        'futures': futures,
        'students': students,
        'alumnis': alumnis
    }
    return render(request, 'auths/base-connect.html', context=context)

def follow(request):
    followed_id = request.GET.get('follow', None)
    followed = BaseInfo.objects.get(id=followed_id).user
    follower = User.objects.get(username=request.user.username)
    follow = Follow.objects.create(follower=follower, followed=followed)
    data = {
        'success': followed_id
    }
    return JsonResponse(data)
