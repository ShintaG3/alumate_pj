from django.shortcuts import render, redirect
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
        all_basic_info = BasicInfo.objects.exclude(user=user)
        all_educations = Education.objects.all()
        home_country_options = all_basic_info.values_list('country_origin', flat=True).distinct()
        study_abroad_country_options = all_basic_info.values_list('country_study_abroad', flat=True).distinct()
        school_options = all_educations.values_list('school', flat=True).distinct()
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
    search_result = get_search_result(query_params, request.user)
    return render(request, 'people/result.html', context={'result': search_result, 'searched': True})

def get_search_result(query_params, user):
    search_result = BasicInfo.objects.exclude(user=user)
    search_result_education = Education.objects.all()
    for key in query_params.keys():
        value_list = query_params.get(key)
        # basic info
        if key == 'status':
            search_result = search_result.filter(status__in=value_list)
        if key == 'home_countries':
            search_result = search_result.filter(country_origin__in=value_list)
        if key == 'study_abroad_countries':
            search_result = search_result.filter(country_study_abroad__in=value_list)
        
        # education
        if key == 'school':
            search_result_education = search_result_education.filter(school__in=value_list)
        if key == 'major':
            search_result_education = search_result_education.filter(major__in=value_list)
        if key == 'start_year':
            lower_bound = int(value_list[0][0:4])
            upper_bound = int(value_list[1][0:4])
            search_result_education = search_result_education.filter(
                start_year__gte=lower_bound, 
                start_year__lte=upper_bound)
        if key == 'end_year':
            lower_bound = int(value_list[0][0:4])
            upper_bound = int(value_list[1][0:4])
            search_result_education = search_result_education.filter(
                start_year__gte=lower_bound, 
                start_year__lte=upper_bound)

    search_result_education_users = search_result_education.values_list('user', flat=True)
    search_result = search_result.filter(user__in=search_result_education_users)
    return search_result