from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, BaseInfoForm, UserLoginForm, SignUpForm
from django.contrib.auth import login, authenticate, logout
from accounts.models import UserProfile, Follow, BaseInfo
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class BaseInquiryView(FormView):
    template_name = "auths/base-inquiry.html"
    form_class = BaseInfoForm
    success_url = reverse_lazy('auths:baseConnect')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SignupView(FormView):
    template_name = "auths/register.html"
    form_class = SignUpForm
    success_url = reverse_lazy('auths:baseInquiry')
    
    def form_valid(self, form):
        form.save()
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password1'])
        login(self.request, user)
        return super().form_valid(form)

class LoginView(FormView):
    template_name = "auths/login.html"
    form_class = UserLoginForm
    success_url = '/feed/'

    def form_valid(self, form):
        next = self.request.GET.get('next')
        cd = form.cleaned_data
        if not cd['remember_me']:
            self.request.session.set_expiry(0)
        user = authenticate(self.request, username=cd['username'], password=cd['password'])
        if (user is not None):
            login(self.request, user)
            if next and next != '/':
                return redirect(next)
        return super().form_valid(form)


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
