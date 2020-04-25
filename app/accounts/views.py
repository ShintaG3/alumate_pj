from django.shortcuts import get_object_or_404, redirect, render
from .forms import BasicInfoForm, ProfileImageForm, EducationForm, StudyAbroadForm, AboutForm, WorkExperienceForm, ScholarshipForm, SocialLinkForm, ProfileForm, StudyAbroadEducationForm
from .models import BasicInfo, Goal, StudyInterest, About, Education, WorkExperience, Major, Scholarship, SocialLink, Follow, ProfileImage, Profile, StudyAbroad
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from message.forms import DirectMessageForm


# Create your views here.
class BaseInquiryView(LoginRequiredMixin, FormView):
    template_name = 'account/base-inquiry.html'
    form_class = BasicInfoForm
    success_url = '/feed/'
    
    def form_valid(self, form):
        basic_info = form.save(commit=False)
        basic_info.user = self.request.user
        basic_info.save()
        return super().form_valid(form)

class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'account/account.html'
   
    def get_context_data(self, **kwargs):
        account = get_object_or_404(User, username=kwargs['username'])
        has_edit_permission = self.request.user == account

        try:
            basic_info = BasicInfo.objects.get(user=account)
        except BasicInfo.DoesNotExist:
            basic_info = None
            
        try:
            profile_image = ProfileImage.objects.get(user=account)
        except ProfileImage.DoesNotExist:
            profile_image = None

        goals = Goal.objects.filter(user=account).values_list('body', flat=True)
        study_interests = StudyInterest.objects.filter(user=account).values_list('body', flat=True)
        goals_str = ",".join(list(goals))
        study_interests_str = ",".join(list(study_interests))
        
        try:
            about = About.objects.get(user=account)
        except About.DoesNotExist:
            about = None
        
        educations = Education.objects.filter(user=account)
        workexperiences = WorkExperience.objects.filter(user=account)
        exp_history = self.get_exp_history(educations, workexperiences)
        
        scholarships = Scholarship.objects.filter(user=account)
        scholarship_history = self.get_scholarship_history(scholarships)
        
        social_links = SocialLink.objects.filter(user=account)
        social_link_lists = self.get_social_link_lists(social_links)
        
        try:
            profile = Profile.objects.get(user=account)
        except Profile.DoesNotExist:
            profile = None
        
        try:
            following = Follow.objects.get(follower=self.request.user, followed=account)
        except Follow.DoesNotExist:
            following = None
        
        followers = Follow.objects.filter(followed=account)
        followings = Follow.objects.filter(follower=account)
        
        try:
            study_abroad = StudyAbroad.objects.get(user=account)
        except StudyAbroad.DoesNotExist:
            study_abroad = None

        new_message_form = DirectMessageForm()
        
        context = {
            'account_user': account,
            'has_edit_permission': has_edit_permission,
            'basic_info': basic_info,
            'profile_image': profile_image,
            'profile_image_form': ProfileImageForm(),
            'education_already_added': educations,
            'study_abroad': study_abroad,
            'study_abroad_choice_form': StudyAbroadForm(),
            'study_abroad_new_form': StudyAbroadEducationForm(),
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
            'is_following': following,
            'followers': followers,
            'followings': followings,
            'new_message_form': new_message_form
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
            elif j >= n:
                history.append(
                {
                    'is_work': False,
                    'value': educations[i],
                    'form': EducationForm(instance=educations[i])
                })
                i += 1
            elif educations[i].start_year == 'Target':
                history.insert(0, 
                {
                    'is_work': False,
                    'value': educations[i],
                    'form': EducationForm(instance=educations[i])
                })
                i += 1
            elif workexperiences[i].start_year == 'Target':
                history.insert(0, 
                {
                    'is_work': True,
                    'value': workexperiences[i],
                    'form': WorkExperienceForm(instance=workexperiences[i])
                })
                j += 1
            elif educations[i].end_year > workexperiences[j].end_year:
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
                                
class BasicInfoUpdateView(LoginRequiredMixin, View):
    form_class = BasicInfoForm
    
    def post(self, request, *args, **kwargs):
        user = request.user
        try:
            basic_info = BasicInfo.objects.get(user=user)
        except BasicInfo.DoesNotExist:
            basic_info = None
        form = self.form_class(request.POST, instance=basic_info)
        
        if form.is_valid:
            basic_info = form.save(commit=False)
            basic_info.user = request.user
            basic_info.save()
        return redirect('/accounts/' + request.user.username)


class UploadProfileImageView(LoginRequiredMixin, View):
    form_class = ProfileImageForm
    
    def post(self, request, *args, **kwargs):
        user = request.user
        
        try:
            profile_image = ProfileImage.objects.get(user=user)
            if request.POST.get('delete') is not None:
                profile_image.delete()
                return redirect('/accounts/' + user.username)
        except ProfileImage.DoesNotExist:
            profile_image = None
        
        form = self.form_class(request.POST, request.FILES, instance=profile_image)
        
        if form.is_valid():
            profile_image = form.save(commit=False)
            profile_image.user = user
            profile_image.save()

        return redirect('/accounts/' + user.username)

class CreateStudyAbroad(LoginRequiredMixin, View):
    form_class = EducationForm
    
    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(request.POST)
        
        if form.is_valid:
            education = form.save(commit=False)
            education.user = user
            education.is_study_abroad = True
            education.save()
            
            try:
                study_abroad = StudyAbroad.objects.get(user=user)
                study_abroad.education = education
            except StudyAbroad.DoesNotExist:
                study_abroad = StudyAbroad(user=user, education=education)
            study_abroad.save()
                
            study_abroad.save()
        
        return redirect('/accounts/' + user.username)


class SelectStudyAbroad(LoginRequiredMixin, View):
    form_class = StudyAbroadForm
    
    def post(self, request, *args, **kwargs):
        user = request.user
        try:
            study_abroad_info = StudyAbroad.objects.get(user=user)
        except StudyAbroad.DoesNotExist:
            study_abroad_info = None
        form = self.form_class(request.POST, instance=study_abroad_info)
        
        if form.is_valid:
            study_abroad_info = form.save(commit=False)
            study_abroad_info.user = user
            study_abroad_info.save()
        return redirect('/accounts/' + user.username)

class GoalUpdateView(LoginRequiredMixin, View):
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

    
class StudyInterestUpdateView(LoginRequiredMixin, View):
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


class AboutUpdateView(LoginRequiredMixin, View):
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
    
class EducationUpdateView(LoginRequiredMixin, View):
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
            try:
                Major.objects.get(name=education.major)
            except Major.DoesNotExist:
                Major.objects.create(name=education.major)
            if education.start_year == "Target":
                education.end_year = "Target"
            education.save()
        
        return redirect('/accounts/' + user.username)


class WorkExperienceUpdateView(LoginRequiredMixin, View):
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
            if workexp.start_year == "Target":
                workexp.end_year = "Target"
            workexp.save()
        
        return redirect('/accounts/' + user.username)
    

class ScholarShipView(LoginRequiredMixin, View):
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


class SocialLinkView(LoginRequiredMixin, View):
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

class ProfileView(LoginRequiredMixin, View):
    form_class = ProfileForm
    
    def post(self, request, pk=None, *args, **kwargs):
        user = request.user
        
        try:
            profile = Profile.objects.get(user=user)
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

class FollowView(LoginRequiredMixin, View):
    def post(self, request, pk=None, *args, **kwargs):
        follower = request.user
        account_to_follow = get_object_or_404(User, username=kwargs['username'])
        
        follow = Follow(follower=follower, followed=account_to_follow)
        follow.save()
        
        return redirect('/accounts/' + account_to_follow.username)


class UnfollowView(LoginRequiredMixin, View):
    def post(self, request, pk=None, *args, **kwargs):
        follower = request.user
        account_to_unfollow = get_object_or_404(User, username=kwargs['username'])
        
        try:
            follow = get_object_or_404(Follow, follower=follower, followed=account_to_unfollow)
            follow.delete()
            return redirect('/accounts/' + account_to_unfollow.username)
        except Follow.DoesNotExist:
            return redirect('/accounts/' + account_to_unfollow.username)
            
        