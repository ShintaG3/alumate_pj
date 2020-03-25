from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import SignUpForm, BaseInfoForm, UserLoginForm
from django.contrib.auth import login, authenticate, logout
from accounts.models import UserProfile, Follow, BaseInfo
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views import View


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
            raw_password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('auths:baseInquiry')
    else:
        form = SignUpForm()
    return render(request, 'auths/register.html', {'form': form})


class LoginView(View):
    template_name = "auths/login.html"
    form_class = UserLoginForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        next = request.GET.get('next')
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if not cd['remember_me']:
                request.session.set_expiry(0)
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if (user is not None):
                login(request, user)
                if next and next != '/':
                    return redirect(next)
                return redirect('feed:feed')
        return render(request, self.template_name, {'form': form})


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
