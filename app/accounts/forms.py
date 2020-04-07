from django import forms
from datetime import date
from .models import *
from django.utils.translation import gettext_lazy as _

current_year = date.today().year

def get_year_choices(plus=0):
    choices = [(x, x) for x in range(1940, current_year+1+plus)]
    choices.reverse()
    choices.insert(0, ('NA', _('Still planning')))
    choices.insert(1, ("Target", _("Target")))
    return choices

def get_start_year_choices(plus=0):
    choices = get_year_choices(plus)
    return choices

def get_end_year_choices(plus=0):
    choices = get_year_choices(plus)
    choices.insert(1, ('Present', _('Present')))
    return choices

class BasicInfoForm(forms.ModelForm):
    status = forms.CharField(widget=forms.RadioSelect(attrs={'class': 'custom-control-input'}, choices=CurrentStatus.choices))
    
    class Meta:
        model = BasicInfo
        fields = (
            'name',
            'status',
            'country_origin', 
            'country_study_abroad',
            # 'living_city'
        )

class ProfileImageForm(forms.ModelForm):
    image = forms.ImageField()
    
    class Meta:
        model = ProfileImage
        fields = ['image']


class StudyAbroadForm(forms.ModelForm):
    education = forms.ModelChoiceField(
        queryset=Education.objects.filter(is_study_abroad=True)
    )

    class Meta:
        model = StudyAbroad
        fields = ('education',)
    
class StudyAbroadEducationForm(forms.ModelForm):
    # status = forms.CharField(widget=forms.RadioSelect(attrs={'class': 'custom-control-input'}, choices=EducationStatus.choices))
    start_year = forms.ChoiceField(choices=get_start_year_choices())
    end_year = forms.ChoiceField(choices=get_end_year_choices(10))

    class Meta:
        model = Education
        fields = ('school', 'major', 'start_year', 'end_year')

class AboutForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea())
    
    class Meta:
        model = About
        fields = ('body',)

class EducationForm(forms.ModelForm):
    # status = forms.CharField(widget=forms.RadioSelect(attrs={'class': 'custom-control-input'}, choices=EducationStatus.choices))
    start_year = forms.ChoiceField(choices=get_start_year_choices())
    end_year = forms.ChoiceField(choices=get_end_year_choices(10))

    class Meta:
        model = Education
        fields = ('is_study_abroad', 'school', 'major', 'start_year', 'end_year')
        
class WorkExperienceForm(forms.ModelForm):
    # status = forms.CharField(widget=forms.RadioSelect(attrs={'class': 'custom-control-input'}, choices=WorkStatus.choices))
    start_year = forms.ChoiceField(choices=get_start_year_choices())
    end_year = forms.ChoiceField(choices=get_end_year_choices())

    class Meta:
        model = WorkExperience
        fields = ('company', 'position', 'start_year', 'end_year')
        
class ScholarshipForm(forms.ModelForm):
    start_year = forms.ChoiceField(choices=[(x, x) for x in range(1940, current_year+4)])
    end_year = forms.ChoiceField(choices=[(x, x) for x in range(1940, current_year+10)])

    class Meta:
        model = Scholarship
        fields = ('organization', 'title', 'start_year', 'end_year')


class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ('title', 'url')
        
class ProfileForm(forms.ModelForm):
    birthday = forms.ChoiceField(choices=[(x, x) for x in range(1940, current_year)])
    
    class Meta:
        model = Profile
        fields = ('gender', 'birthday')