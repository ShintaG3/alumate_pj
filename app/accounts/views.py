from django.shortcuts import get_object_or_404, redirect, render
from .forms import BasicInfoForm
from .models import BasicInfo, Goal, StudyInterest
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import FormView


# Create your views here.
class AccountView(TemplateView):
    template_name = 'account/account.html'
    
    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=kwargs['username'])
        try:
            basic_info = BasicInfo.objects.get(user=user)
        except BasicInfo.DoesNotExist:
            basic_info = None
        goals = Goal.objects.filter(user=user).values_list('body')
        study_interests = StudyInterest.objects.filter(user=user).values_list('body')
        goals_str = ",".join(goals)
        study_interests_str = ",".join(study_interests)
        
        context = {
            'user': user,
            'basic_info': basic_info,
            'basic_info_form': BasicInfoForm(instance=basic_info),
            'goals': goals,
            'goals_values': goals_str,
            'study_interests': study_interests,
            'study_interests_values': study_interests_str,
        }
        return context


class BasicInfoUpdateView(View):
    form_class = BasicInfoForm
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid:
            basic_info = form.save(commit=False)
            basic_info.user = request.user
            basic_info.save()
        return redirect('/accounts/' + request.user.username)
