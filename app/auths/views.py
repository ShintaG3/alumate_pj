from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import SignUpForm, BaseInfoForm, UserLoginForm, SignUpForm
from django.contrib.auth import login, authenticate, logout
from accounts.models import Follow, BasicInfo, CurrentStatus
from feed.models import Post
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db.models import Q


class SignupView(FormView):
    template_name = "auths/register.html"
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:base-inquiry')

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('feed:feed')
        return render(request, self.template_name, {'form': self.form_class()}) 
  
    def form_valid(self, form):
        form.save()
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password1'])
        login(self.request, user)
        Post.objects.create(user=user,body="@" + user.username + " has joined Alumate!")
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
        get_user = User.objects.get(Q(username=cd['username']) | 
                                Q(email=cd['username'])) 
        username = get_user.username
        user = authenticate(self.request, username=username, password=cd['password'])
        if (user is not None):
            login(self.request, user)
            if next and next != '/':
                return redirect(next)
        return super().form_valid(form)


def logoutUser(request):
    logout(request)
    return redirect('/')

class BaseConnect(LoginRequiredMixin, TemplateView):
    template_name = 'auths/base-connect.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        user_basic_info = get_object_or_404(BasicInfo, user=user)
        same_home_country_users = BasicInfo.objects.filter(country_origin=user_basic_info.country_origin).exclude(user=user)
        futures = same_home_country_users.filter(status=CurrentStatus.FUTURE_STUDENT)[:4]
        students = same_home_country_users.filter(status=CurrentStatus.CURRENT_STUDENT)[:4]
        alumnis = same_home_country_users.filter(status=CurrentStatus.ALUMNI)[:4]
        context = {
            'futures': futures,
            'students': students,
            'alumnis': alumnis,
        }
        return context

class FollowView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        follower = request.user
        account_to_follow = get_object_or_404(User, id=kwargs['id'])

        try:
            Follow.objects.get(follower=follower, followed=account_to_follow)
            return JsonResponse({'data': 'already following'})
        except Follow.DoesNotExist:
            follow = Follow(follower=follower, followed=account_to_follow)
            follow.save()
            
            return JsonResponse({'data': 'success'})

def checkpwdstrength(request):
    pwd = request.GET.get('password', None)
    status = 'strong'
    try:
        validate_password(pwd)
    except ValidationError:
        status = 'weak'
    data = {
        'status': status
    }
    return JsonResponse(data)
