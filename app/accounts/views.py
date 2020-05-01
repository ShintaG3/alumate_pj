from django.shortcuts import get_object_or_404, redirect, render
from .forms import BasicInfoForm, ProfileImageForm, EducationForm, StudyAbroadSelectForm, AboutForm, WorkExperienceForm, ScholarshipForm, SocialLinkForm, ProfileForm, StudyAbroadEducationForm
from .models import BasicInfo, Goal, StudyInterest, About, Education, WorkExperience, Major, Scholarship, SocialLink, Follow, ProfileImage, Profile, StudyAbroad
from feed.models import Post, PostLike, PostComment, PostCommentLike
from inquiry.models import Ask, AskTagSchool, AskLike
from feed.forms import PostCommentForm
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from message.forms import DirectMessageForm
from django.urls import reverse_lazy

# Create your views here.
class BaseInquiryView(LoginRequiredMixin, FormView):
    template_name = 'account/base-inquiry.html'
    form_class = BasicInfoForm
    success_url = reverse_lazy('auths:base-connect')
    
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

        post_list = self.get_post_list(user=account)
        comment_form = PostCommentForm()

        ask_list = self.get_ask_list(user=account)
        
        context = {
            'account_user': account,
            'has_edit_permission': has_edit_permission,
            'basic_info': basic_info,
            'profile_image': profile_image,
            'education_already_added': educations,
            'study_abroad': study_abroad,
            'goals': goals,
            'goals_values': goals_str,
            'study_interests': study_interests,
            'study_interests_values': study_interests_str,
            'about': about,
            'exp_history': exp_history,
            'scholarship_history': scholarship_history,
            'social_links': social_link_lists,
            'profile': profile,
            'is_following': following,
            'followers': followers,
            'followings': followings,
            'new_message_form': new_message_form,
            'post_list': post_list,
            'comment_form': comment_form,
            'ask_list': ask_list
        }

        if has_edit_permission:
            additional_form_context = {
                'profile_image_form': ProfileImageForm(),
                'study_abroad_choice_form': StudyAbroadSelectForm(user=account),
                'study_abroad_new_form': StudyAbroadEducationForm(user=account),
                'basic_info_form': BasicInfoForm(instance=basic_info),
                'about_form': AboutForm(instance=about),
                'new_education_form': EducationForm(user=account),
                'new_work_form': WorkExperienceForm(),
                'new_scholarship_form': ScholarshipForm(),
                'new_social_link_form': SocialLinkForm(),
                'profile_form': ProfileForm(),
            }
            context = { **context, **additional_form_context }
        
        return context
    
    def get_exp_history(self, educations, workexperiences):
        m = len(educations)
        n = len(workexperiences)
        i= 0
        j = 0
        user = self.request.user
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
                    'form': EducationForm(instance=educations[i], user=user)
                })
                i += 1
            elif educations[i].start_year == 'Target':
                history.insert(0, 
                {
                    'is_work': False,
                    'value': educations[i],
                    'form': EducationForm(instance=educations[i], user=user)
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
                    'form': EducationForm(instance=educations[i], user=user)
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
    
    # this is same function as in feed
    def get_post_list(self, user):
        posts = Post.objects.filter(user=user)[:10]
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
   
    # this is same function as in feed
    def get_ask_list(self, user):
        ask_list = []
        asks = Ask.objects.filter(user=user)[:10]
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
            
            if not profile_image.image: # saved without image
                return redirect('/accounts/' + user.username)
            
            profile_image.user = user
            profile_image.save()

        return redirect('/accounts/' + user.username)

class CreateStudyAbroad(LoginRequiredMixin, View):
    form_class = EducationForm
    
    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(request.POST, user=user)
        
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
    form_class = StudyAbroadSelectForm
    
    def post(self, request, *args, **kwargs):
        user = request.user
        try:
            study_abroad_info = StudyAbroad.objects.get(user=user)
        except StudyAbroad.DoesNotExist:
            study_abroad_info = None
        form = self.form_class(request.POST, instance=study_abroad_info, user=user)
        
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


class EducationCreateView(LoginRequiredMixin, View):
    form_class = EducationForm
    
    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(request.POST, user=user)

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


class EducationUpdateView(LoginRequiredMixin, View):
    form_class = EducationForm
    
    def post(self, request, pk=None, *args, **kwargs):
        user = request.user
        education = Education.objects.get(pk=pk)
        if request.POST.get('delete') is not None:
            education.delete()
            return redirect('/accounts/' + user.username)
        
        form = self.form_class(request.POST, instance=education, user=user)

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

class PostCommentView(LoginRequiredMixin, View):
    form_class = PostCommentForm
    
    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(request.POST, request.FILES)
        post = Post.objects.get(pk=kwargs['id'])
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = user
            comment.post = post
            comment.save()
            
        return redirect('/accounts/' + kwargs['username'])


class PostLikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        post = Post.objects.get(pk=kwargs['id'])
        try:
            like = PostLike.objects.get(user=user, post=post)
            like.delete()
        except PostLike.DoesNotExist:
            PostLike(user=user, post=post).save()
            
        return redirect('/accounts/' + kwargs['username'])
    
class PostCommentLikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        comment = PostComment.objects.get(pk=kwargs['id'])
        try:
            like = PostCommentLike.objects.get(user=user, comment=comment)
            like.delete()
        except PostCommentLike.DoesNotExist:
            PostCommentLike(user=user, comment=comment).save()
            
        return redirect('/accounts/' + kwargs['username'])


class InquiryLikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        ask = Ask.objects.get(pk=kwargs['id'])
        try:
            like = AskLike.objects.get(user=user, ask=ask)
            like.delete()
        except AskLike.DoesNotExist:
            AskLike(user=user, ask=ask).save()
            
        return redirect('/accounts/' + kwargs['username'])
