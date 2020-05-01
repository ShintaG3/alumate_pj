from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import *
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from urllib.parse import urlencode, urlparse, parse_qs
from django.urls import reverse
from django.http import JsonResponse


# Create your views here.
class PeopleView(LoginRequiredMixin, TemplateView):
    template_name = 'people/people.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        followings_id = Follow.objects.filter(follower=user).values_list('followed', flat=True)
        all_basic_info = BasicInfo.objects.exclude(user=user).exclude(user__id__in=followings_id)
        all_educations = Education.objects.all()
        home_country_options = all_basic_info.values_list('country_origin__name', flat=True).distinct()
        study_abroad_country_options = all_basic_info.values_list('country_study_abroad__name', flat=True).distinct()
        school_options = all_educations.values_list('school__name', flat=True).distinct()
        major_options = all_educations.values_list('major', flat=True).distinct()
        context = super().get_context_data(**kwargs)
        context = {
            'result': all_basic_info,
            'home_country_options': home_country_options,
            'study_abroad_country_options': study_abroad_country_options,
            'school_options': school_options,
            'major_options': major_options,
            'searched': False
        }
        return context


def update_result(request, *args, **kwargs):
    query_params = {}
    for key in request.POST.keys():
        value = request.POST.getlist(key)
        query_params[key.replace('[]', '')] = value

    # relative_url = '{}?{}'.format((reverse('people:index')), urlencode(query_params))
    followings_id = Follow.objects.filter(follower=request.user).values_list('followed', flat=True)
    search_result = get_search_result(query_params, request.user).exclude(user__id__in=followings_id)
    return render(request, 'people/result.html', context={'result': search_result, 'searched': True})

def get_search_result(query_params, user):
    search_result = BasicInfo.objects.exclude(user=user)
    search_result_education = Education.objects.all()
    query_keys = query_params.keys()
    education_filter = False
    for key in query_keys:
        value_list = query_params.get(key)
        # basic info
        if key == 'status':
            search_result = search_result.filter(status__in=value_list)
        elif key == 'home_countries':
            search_result = search_result.filter(country_origin__name__in=value_list)
        elif key == 'study_abroad_countries':
            search_result = search_result.filter(country_study__name__abroad__in=value_list)
        
        # education
        elif key == 'school':
            search_result_education = search_result_education.filter(school__name__in=value_list)
            education_filter = True
        elif key == 'major':
            search_result_education = search_result_education.filter(major__name__in=value_list)
            education_filter = True
        elif key == 'start_year':
            lower_bound = int(value_list[0][0:4])
            upper_bound = int(value_list[1][0:4])
            if lower_bound == 1980 and upper_bound == 2030:
                continue
            search_result_education = search_result_education.filter(
                start_year__gte=lower_bound, 
                start_year__lte=upper_bound)
            education_filter = True
        elif key == 'end_year':
            lower_bound = int(value_list[0][0:4])
            upper_bound = int(value_list[1][0:4])
            if lower_bound == 1980 and upper_bound == 2030:
                continue
            search_result_education = search_result_education.filter(
                start_year__gte=lower_bound, 
                start_year__lte=upper_bound)
            education_filter = True
    
    if not education_filter:
        return search_result
    search_result_education_users = set(search_result_education.values_list('user', flat=True))
    search_result = search_result.filter(user__in=search_result_education_users)
    return search_result


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