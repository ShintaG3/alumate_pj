from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import SignUpForm, BaseInfoForm, UserInformationUpdateForm
from django.contrib.auth import login, authenticate
from accounts.models import UserProfile, Follow, BaseInfo
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required

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
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('auths:baseInquiry')
    else:
        form = SignUpForm()
    return render(request, 'auths/register.html', {'form': form})

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

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    form_class = UserInformationUpdateForm
    template_name = 'auths/my_account.html'
    success_url = reverse_lazy('auths:my_account')

    def get_object(self):
        return self.request.user

def follow(request):
    followed_id = request.GET.get('follow', None)
    followed = BaseInfo.objects.get(id=followed_id).user
    follower = User.objects.get(username=request.user.username)
    follow = Follow.objects.create(follower=follower, followed=followed)
    data = {
        'success': followed_id
    }
    return JsonResponse(data)