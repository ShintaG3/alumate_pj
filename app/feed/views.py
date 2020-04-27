from django.contrib.auth.models import User
from django.db.models import Q
from django.views import View
from django.views.generic.base import TemplateView
from accounts.models import Country, School, Major
from .models import *
from .forms import *
from inquiry.models import *
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Follow
import json

class FeedView(LoginRequiredMixin, TemplateView):
    template_name = 'feed/feed.html'
    permission_required = ''

    def get_context_data(self, **kwargs):
        user = self.request.user
        try:
            basic_info = BasicInfo.objects.get(user=user)
            country1 = Country.objects.get(name=basic_info.country_origin)
            country2 = Country.objects.get(name=basic_info.country_study_abroad)
            school_options = School.objects.filter(Q(country=country1) | Q(country=country2))
        except BasicInfo.DoesNotExist:
            school_options = School.objects.all()
        context = {
            'new_post_form': PostForm(),
            'comment_form': PostCommentForm(),
            'post_list': self.get_post_list(user),
            'country_options': Country.objects.all(),
            'school_options': school_options,
            'major_options': Major.objects.all(),
            'ask_list': self.get_ask_list(user)
        }
        return context

    def get_post_list(self, user):
        posts = Post.objects.all()[:10]
        post_list = []
        
        for post in posts:
            try:
                liked = PostLike.objects.get(user=user, post=post)
            except PostLike.DoesNotExist:
                liked = None
            try:
                following = Follow.objects.get(follower=user, followed=post.user)
            except Follow.DoesNotExist:
                following = None
            
            post_list.append({
                'value': post,
                'liked': liked,
                'user_following': following
            })
        return post_list
    
    def get_ask_list(self, user):
        ask_list = []
        asks = Ask.objects.all()[:10]
        for ask in asks:
            school_tags = list(AskTagSchool.objects.filter(ask=ask).values_list('body__name', flat=True))
            school_tags_str = ', '.join(school_tags)

            try:
                liked = AskLike.objects.get(user=user, ask=ask)
            except AskLike.DoesNotExist:
                liked = None

            ask_list.append({
                'value': ask,
                'liked': liked,
                'school_tag': school_tags_str,
            })

        return ask_list

class PostView(LoginRequiredMixin, View):
    form_class = PostForm
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('/feed/')
        
class PostCommentView(LoginRequiredMixin, View):
    form_class = PostCommentForm
    template_name = 'feed/feed.html'
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        post = Post.objects.get(pk=kwargs['id'])
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.post = post
            comment.save()
            
        return redirect('/feed/')


class PostLikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        post = Post.objects.get(pk=kwargs['id'])
        try:
            like = PostLike.objects.get(user=user, post=post)
            like.delete()
        except PostLike.DoesNotExist:
            PostLike(user=user, post=post).save()
            
        return redirect('/feed/')
    
class PostCommentLikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        comment = PostComment.objects.get(pk=kwargs['id'])
        try:
            like = PostCommentLike.objects.get(user=user, comment=comment)
            like.delete()
        except PostCommentLike.DoesNotExist:
            PostCommentLike(user=user, comment=comment).save()
            
        return redirect('/feed/')


class AskView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        data = json.loads(request.body)
        
        print(data)

        ask = Ask.objects.create(user=user, title=data['title'], body=data['body'])
        
        for tag in data.get('status', []):
            if tag == 'FU':
                AskTagStatus.objects.create(ask=ask, body=CurrentStatus.FUTURE_STUDENT)
            elif tag == 'CU':
                AskTagStatus.objects.create(ask=ask, body=CurrentStatus.CURRENT_STUDENT)
            elif tag == 'AL':
                AskTagStatus.objects.create(ask=ask, body=CurrentStatus.ALUMNI)
        
        for tag in data.get('home_countries', []):
            country = Country.objects.get(name=tag)
            AskTagHomeCountry.objects.create(ask=ask, body=country)
        for tag in data.get('study_abroad_countries', []):
            country = Country.objects.get(name=tag)
            AskTagStudyAbroadCountry.objects.create(ask=ask, body=country)
        for tag in data.get('schools', []):
            print(tag)
            school = School.objects.filter(name=tag).first()
            AskTagSchool.objects.create(ask=ask, body=school)
        for tag in data.get('majors', []):
            major = Major.objects.get(name=tag)
            AskTagMajor.objects.create(ask=ask, body=major)
        
        AskTagStartYear.objects.create(ask=ask, lower_bound=doubleStrToInt(data['start_year'][0]), upper_bound=doubleStrToInt(data['start_year'][1][0:4]))
        AskTagEndYear.objects.create(ask=ask, lower_bound=doubleStrToInt(data['end_year'][0]), upper_bound=doubleStrToInt(data['end_year'][1][0:4]))

        return JsonResponse({'success': 'sucess'})

def doubleStrToInt(str):
    int_str = str[0:4]
    return int(int_str)


class AskLikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        ask = Ask.objects.get(pk=kwargs['id'])
        try:
            like = AskLike.objects.get(user=user, ask=ask)
            like.delete()
        except AskLike.DoesNotExist:
            AskLike(user=user, ask=ask).save()
            
        return redirect('/feed/')