from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, reverse
from .models import *
from .forms import *
from accounts.models import Follow


# Create your views here.
class InquiryView(LoginRequiredMixin, TemplateView):
    template_name = 'inquiry/inquiry.html'

    def get_context_data(self, **kwargs):
        user = self.request.user        
        context = {
            'ask_list': self.get_ask_list(user)
        }
        return context
    
    def get_ask_list(self, user):
        ask_list = []
        asks = Ask.objects.all()[:10]
        for ask in asks:
            school_tags = list(AskTagSchool.objects.filter(ask=ask).values_list('body', flat=True))
            print(school_tags)
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

class InquiryDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'inquiry/inquiry-detail.html'
    form_class = AskCommentForm

    def get_context_data(self, **kwargs):
        ask_id = kwargs['id']
        ask = Ask.objects.get(id=ask_id)

        comments = AskComment.objects.filter(ask=ask)

        status_enum = AskTagStatus.objects.filter(ask=ask)
        status_tags = []
        for status in status_enum:
            if status.body == 'FU':
                status_tags.append('Future Student')
            elif status.body == 'CU':
                status_tags.append('Current Student')
            elif status.body == 'AL':
                status_tags.append('Alumni')
            
        home_country_tags = AskTagHomeCountry.objects.filter(ask=ask)
        study_abroad_country_tags = AskTagStudyAbroadCountry.objects.filter(ask=ask)
        school_tags = AskTagSchool.objects.filter(ask=ask)
        major_tags = AskTagMajor.objects.filter(ask=ask)

        start_year_tag = AskTagStartYear.objects.get(ask=ask)
        end_year_tag = AskTagEndYear.objects.get(ask=ask)

        user = self.request.user
        
        try:
            following = Follow.objects.get(follower=user, followed=ask.user)
        except Follow.DoesNotExist:
            following = None

        context = {
            'ask': ask,
            'comments': comments,
            'comment_form': self.form_class(),
            'status_tags': status_tags,
            'home_country_tags': home_country_tags,
            'study_abroad_country_tags': study_abroad_country_tags,
            'school_tags': school_tags,
            'major_tags': major_tags,
            'start_year_tag': start_year_tag,
            'end_year_tag': end_year_tag,
            'following': following
        }
        return context

class InquiryLikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        ask = Ask.objects.get(pk=kwargs['id'])
        try:
            like = AskLike.objects.get(user=user, ask=ask)
            like.delete()
        except AskLike.DoesNotExist:
            AskLike(user=user, ask=ask).save()
            
        return redirect('/inquiry/')

class InquiryCommentView(LoginRequiredMixin, View):
    form_class = AskCommentForm
    template_name = 'feed/feed.html'
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        ask = Ask.objects.get(pk=kwargs['id'])
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.ask = ask
            comment.save()
            
        return redirect(reverse('inquiry:detail', kwargs={'id': kwargs['id']}))
    
class InquiryCommentLikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        comment = AskComment.objects.get(pk=kwargs['comment_id'])
        try:
            like = AskCommentLike.objects.get(user=user, comment=comment)
            like.delete()
        except AskCommentLike.DoesNotExist:
            AskCommentLike(user=user, comment=comment).save()
            
        return redirect(reverse('inquiry:detail', kwargs={'id': kwargs['ask_id']}))


class FollowView(LoginRequiredMixin, View):
    def post(self, request, pk=None, *args, **kwargs):
        follower = request.user
        account_to_follow = get_object_or_404(User, username=kwargs['username'])
        
        follow = Follow(follower=follower, followed=account_to_follow)
        follow.save()
        
        return redirect(reverse('inquiry:detail', kwargs={'id': kwargs['id']}))
