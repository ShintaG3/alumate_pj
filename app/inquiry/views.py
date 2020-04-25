from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, reverse, render
from .models import Ask, AskLike, AskComment, AskCommentLike, AskTagStatus, AskTagHomeCountry, AskTagStudyAbroadCountry, AskTagSchool, AskTagMajor, AskTagStartYear, AskTagEndYear
from .forms import AskCommentForm
from accounts.models import Follow
import json


# Create your views here.
class InquiryView(LoginRequiredMixin, TemplateView):
    template_name = 'inquiry/inquiry.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        
        home_country_options = set(AskTagHomeCountry.objects.all().values_list('body', flat=True))
        study_abroad_country_options = set(AskTagStudyAbroadCountry.objects.all().values_list('body', flat=True))
        country_options = home_country_options.union(study_abroad_country_options)
        school_options = set(AskTagSchool.objects.all().values_list('body', flat=True))
        major_options = set(AskTagMajor.objects.all().values_list('body', flat=True))

        context = {
            'country_options': country_options,
            'school_options': school_options,
            'major_options': major_options,
            'ask_list': self.get_ask_list(user)
        }
        return context
    
    def get_ask_list(self, user):
        ask_list = []
        asks = Ask.objects.all()[:10]
        for ask in asks:
            school_tags = list(AskTagSchool.objects.filter(ask=ask).values_list('body', flat=True))
            school_tags_str = ', '.join(school_tags)

            try:
                liked = AskLike.objects.get(user=user, ask=ask)
            except AskLike.DoesNotExist:
                liked = None

            ask_list.append({
                'value': ask,
                'liked': liked,
                'school_tag': school_tags_str,
                'searched': False
            })

        return ask_list


def update_result(request, *args, **kwargs):
    query_dict = json.loads(request.body)
    user = request.user

    search_result = get_search_result(query_dict, user)
    ask_list = []

    for ask in search_result:
        school_tags = list(AskTagSchool.objects.filter(ask=ask).values_list('body', flat=True))
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
    
    context = {
        'ask_list': ask_list,
        'searched': True,
        'results': search_result.count()
    }

    return render(request, 'inquiry/result.html', context=context)

def get_search_result(query_params, user):
    search_result = Ask.objects.all()
    for key in query_params.keys():
        value_list = query_params.get(key)
        if not value_list:
            continue
        
        ask_id_list = None
        if key == 'status':
            ask_id_list = AskTagStatus.objects.filter(body__in=value_list).values_list('ask__id', flat=True)
        elif key == 'home_countries':
            ask_id_list = AskTagHomeCountry.objects.filter(body__in=value_list).values_list('ask__id', flat=True)
        elif key == 'study_abroad_countries':
            ask_id_list = AskTagStudyAbroadCountry.objects.filter(body__in=value_list).values_list('ask__id', flat=True)
        elif key == 'schools':
            ask_id_list = AskTagSchool.objects.filter(body__in=value_list).values_list('ask__id', flat=True)
        elif key == 'majors':
            ask_id_list = AskTagMajor.objects.filter(body__in=value_list).values_list('ask__id', flat=True)
        elif key == 'start_year':
            lower_bound = int(value_list[0][0:4])
            upper_bound = int(value_list[1][0:4])
            ask_id_list = AskTagStartYear.objects.filter(lower_bound__gte=lower_bound, upper_bound__lte=upper_bound).values_list('ask__id', flat=True)
        elif key == 'end_year':
            lower_bound = int(value_list[0][0:4])
            upper_bound = int(value_list[1][0:4])
            ask_id_list = AskTagEndYear.objects.filter(lower_bound__gte=lower_bound, upper_bound__lte=upper_bound).values_list('ask__id', flat=True)

        if ask_id_list:
            search_result = search_result.filter(id__in=ask_id_list)

    return search_result

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
