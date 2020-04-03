from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from .models import BasicInfo, Goal, StudyInterest, About, Education, WorkExperience
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
        has_edit_permission = self.request.user == user

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
        
        educations = Education.objects.filter(user=user)
        workexperiences = WorkExperience.objects.filter(user=user)
        exp_history = self.get_exp_history(educations, workexperiences)
        
        scholarships = Scholarship.objects.filter(user=user)
        scholarship_history = self.get_scholarship_history(scholarships)
        
        social_links = SocialLink.objects.filter(user=user)
        social_link_lists = self.get_social_link_lists(social_links)
        
        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            profile = None
        
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
            'new_education_form': EducationForm(),
            'new_work_form': WorkExperienceForm(),
            'exp_history': exp_history,
            'scholarship_history': scholarship_history,
            'new_scholarship_form': ScholarshipForm(),
            'social_links': social_link_lists,
            'new_social_link_form': SocialLinkForm(),
            'profile': profile,
            'profile_form': ProfileForm(),
        }
        return context
    
    def get_exp_history(self, educations, workexperiences):
        m = len(educations)
        n = len(workexperiences)
        i= 0
        j = 0
        history = []
        while (i < m or j < n):
            if i >= m:
                history.append(
                {
                    'is_work': True,
                    'value': workexperiences[j],
                    'form': WorkExperienceForm(instance=workexperiences[j])
                })
                j += 1
            elif j >= n or educations[i].end_year > workexperiences[j].end_year:
                history.append(
                {
                    'is_work': False,
                    'value': educations[i],
                    'form': EducationForm(instance=educations[i])
                })
                i += 1
            else:
                history.append(
                {
                    'is_work': True,
                    'value': workexperiences[j],
                    'form': WorkExperienceForm(instance=workexperiences[j])
                })
                j += 1

        return history
    
    def get_scholarship_history(self, scholarships):
        history = []
        for scholarship in scholarships:
            history.append(
            {
                'value': scholarship,
                'form': ScholarshipForm(instance=scholarship)
            })
        return history
    
    def get_social_link_lists(self, social_links):
        social_link_lists = []
        for social_link in social_links:
            social_link_lists.append({
                'value': social_link,
                'form': SocialLinkForm(instance=social_link)
            })
        return social_link_lists
                                
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
        user = request.user
        try:
            about = About.objects.get(user=user)
        except About.DoesNotExist:
            about = None
        form = self.form_class(request.POST, instance=about)
        
        if form.is_valid:
            about = form.save(commit=False)
            about.user = user
            about.save()
        return redirect('/accounts/' + user.username)
    
class EducationUpdateView(View):
    form_class = EducationForm
    
    def post(self, request, pk=None, *args, **kwargs):
        user = request.user
        try:
            education = Education.objects.get(pk=pk)
            if request.POST.get('delete') is not None:
                education.delete()
                return redirect('/accounts/' + user.username)
            
        except Education.DoesNotExist:
            education = None
        
        form = self.form_class(request.POST, instance=education)
        
        if form.is_valid:
            education = form.save(commit=False)
            education.user = request.user
            education.save()
        
        return redirect('/accounts/' + user.username)


class WorkExperienceUpdateView(View):
    form_class = WorkExperienceForm
    
    def post(self, request, pk=None, *args, **kwargs):
        user = request.user
        try:
            workexp = WorkExperience.objects.get(pk=pk)
            if request.POST.get('delete') is not None:
                workexp.delete()
                return redirect('/accounts/' + user.username)
            
        except WorkExperience.DoesNotExist:
            workexp = None
        
        form = self.form_class(request.POST, instance=workexp)
       
        if form.is_valid:
            workexp = form.save(commit=False)
            workexp.user = request.user
            workexp.save()
        
        return redirect('/accounts/' + user.username)
    

class ScholarShipView(View):
    form_class = ScholarshipForm
    
    def post(self, request, pk=None, *args, **kwargs):
        user = request.user
        
        try:
            scholarship = Scholarship.objects.get(pk=pk)
            if request.POST.get('delete') is not None:
                scholarship.delete()
                return redirect('/accounts/' + user.username)
            
        except Scholarship.DoesNotExist:
            scholarship = None
        
        form = self.form_class(request.POST, instance=scholarship)
       
        if form.is_valid:
            scholarship = form.save(commit=False)
            scholarship.user = request.user
            scholarship.save()
        
        return redirect('/accounts/' + user.username)


class SocialLinkView(View):
    form_class = SocialLinkForm
    
    def post(self, request, pk=None, *args, **kwargs):
        user = request.user
        
        try:
            social_link = SocialLink.objects.get(pk=pk)
            if request.POST.get('delete') is not None:
                social_link.delete()
                return redirect('/accounts/' + user.username)
            
        except SocialLink.DoesNotExist:
            social_link = None
        
        form = self.form_class(request.POST, instance=social_link)
       
        if form.is_valid:
            social_link = form.save(commit=False)
            social_link.user = request.user
            social_link.save()
        
        return redirect('/accounts/' + user.username)

class ProfileView(View):
    form_class = ProfileForm
    
    def post(self, request, pk=None, *args, **kwargs):
        user = request.user
        
        try:
            profile = Profile.objects.get(pk=pk)
            if request.POST.get('delete') is not None:
                profile.delete()
                return redirect('/accounts/' + user.username)
            
        except Profile.DoesNotExist:
            profile = None
        
        form = self.form_class(request.POST, instance=profile)
       
        if form.is_valid:
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
        
        return redirect('/accounts/' + user.username)

