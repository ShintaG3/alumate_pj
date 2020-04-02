from django.shortcuts import get_object_or_404, redirect, render
from .forms import BasicInfoForm, AboutForm
from .models import BasicInfo, Goal, StudyInterest, About
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import FormView


# Create your views here.
class BaseInquiryView(FormView):
    template_name = 'account/base-inquiry.html'
    form_class = BasicInfoForm
    success_url = '/feed/'
    
    def form_valid(self, form):
        basic_info = form.save(commit=False)
        basic_info.user = self.request.user
        basic_info.save()
        return super().form_valid(form)

class AccountView(TemplateView):
    template_name = 'account/account.html'
    
    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=kwargs['username'])
        has_edit_permission = self.request.user = user

        try:
            basic_info = BasicInfo.objects.get(user=user)
        except BasicInfo.DoesNotExist:
            basic_info = None
        
        goals = Goal.objects.filter(user=user).values_list('body', flat=True)
        study_interests = StudyInterest.objects.filter(user=user).values_list('body', flat=True)
        goals_str = ",".join(list(goals))
        study_interests_str = ",".join(list(study_interests))
        
        try:
            about = About.objects.get(user=user)
        except About.DoesNotExist:
            about = None
        
        context = {
            'user': user,
            'has_edit_permission': has_edit_permission,
            'basic_info': basic_info,
            'basic_info_form': BasicInfoForm(instance=basic_info),
            'goals': goals,
            'goals_values': goals_str,
            'study_interests': study_interests,
            'study_interests_values': study_interests_str,
            'about': about,
            'about_form': AboutForm(instance=about),
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


class GoalUpdateView(View):
    def post(self, request, *args, **kwargs):
        username = kwargs['username']
        user = User.objects.get(username=username)
        
        new_goals_input_values = request.POST.get('goals')
        new_goal_set = set(new_goals_input_values.split(','))
        
        try:
            current_goals = Goal.objects.filter(user=user).values_list('body', flat=True)
            
            # Add new tags
            for new_goal in new_goal_set:
                if new_goal not in current_goals:
                    goal = Goal(user=user, body=new_goal)
                    goal.save()

            # Delete tags that are not in inputs but in db
            for current_goal in current_goals:
                if current_goal not in new_goal_set:
                    Goal.objects.get(
                        user=user,
                        body=current_goal
                    ).delete()

        except Goal.DoesNotExist:
            for new_goal in new_goal_set:
                goal = Goal(user=user, body=new_goal)
                goal.save()
        
        return redirect('/accounts/' + username)

    
class StudyInterestUpdateView(View):
    def post(self, request, *args, **kwargs):
        username = kwargs['username']
        user = User.objects.get(username=username)
        
        new_studyinterests_input_values = request.POST.get('studyInterests')
        new_studyinterests_set = set(new_studyinterests_input_values.split(','))
        
        try:
            current_studyinterests = StudyInterest.objects.filter(user=user).values_list('body', flat=True)
            
            # Add new tags
            for new_studyinterest in new_studyinterests_set:
                if new_studyinterest not in current_studyinterests:
                    studyinterest = StudyInterest(user=user, body=new_studyinterest)
                    studyinterest.save()

            # Delete tags that are not in inputs but in db
            for current_studyinterest in current_studyinterests:
                if current_studyinterest not in new_studyinterests_set:
                    StudyInterest.objects.get(
                        user=user,
                        body=current_studyinterest
                    ).delete()
        
        except StudyInterest.DoesNotExist:
            for new_studyinterest in new_studyinterests_set:
                studyinterest = StudyInterest(user=user, body=new_studyinterest)
                studyinterest.save()
        
        return redirect('/accounts/' + username)


class AboutUpdateView(View):
    form_class = AboutForm
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid:
            basic_info = form.save(commit=False)
            basic_info.user = request.user
            basic_info.save()
        return redirect('/accounts/' + request.user.username)