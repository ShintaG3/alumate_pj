from django.shortcuts import render, redirect
from accounts.models import *
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from urllib.parse import urlencode, urlparse, parse_qs
from django.urls import reverse


# Create your views here.
class PeopleView(LoginRequiredMixin, View):
    template_name = 'people/people.html'

    def get(self, request, *args, **kwargs):
        if (request.GET): # when user queried search
            print('searched')
            result = self.get_search_result(request.GET)
            searched = True
        else:
            result = BasicInfo.objects.all()
            searched = False

        context = {
            'result': result,
            'country_options': Country.objects.all(),
            'school_options': School.objects.all(),
            'major_options': Major.objects.all(),
            'searched': searched
        }
        return render(request, self.template_name, context=context)


    def post(self, request, *args, **kwargs):
        query_params = {}
        for key in request.POST.keys():
            value = request.POST.getlist(key)
            query_params[key.replace('[]', '')] = value

        relative_url = '{}?{}'.format((reverse('people:index')), urlencode(query_params))
        
        return redirect(relative_url)

    def get_search_result(self, query_params):
        search_result = BasicInfo.objects.all()
        search_result_education = Education.objects.all()
        for key in query_params.keys():
            value_str = query_params.get(key)
            value_list = value_str.replace('[', '').replace(']', '').replace('\'', '').split(', ')

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
                lower_bound = int(value_list[0][0:3])
                upper_bound = int(value_list[1][0:3])
                search_result_education = search_result_education.filter(
                    start_year__gte=lower_bound, 
                    start_year__lte=upper_bound)
            if key == 'end_year':
                lower_bound = int(value_list[0][0:3])
                upper_bound = int(value_list[1][0:3])
                search_result_education = search_result_education.filter(
                    start_year__gte=lower_bound, 
                    start_year__lte=upper_bound)

        print(search_result)
        print(search_result_education)
        search_result_education_users = search_result_education.values_list('user', flat=True)
        search_result = search_result.filter(user__in=search_result_education_users)
        return search_result