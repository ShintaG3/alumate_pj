from django import forms
from datetime import date
from .models import *

current_year = date.today().year

class BasicInfoForm(forms.ModelForm):
    current_year = date.today().year
    status = forms.CharField(widget=forms.RadioSelect(attrs={'class': 'custom-control-input'}, choices=CurrentStatus.choices))
    school_start_year = forms.ChoiceField(choices=[("*", "Still planning")]  + [(x, x) for x in range(1940, current_year+4)])
    school_end_year = forms.ChoiceField(choices=[("*", "Still planning")] + [(x, x) for x in range(1940, current_year+10)])
    
    class Meta:
        model = BasicInfo
        fields = (
            'name',
            'status',
            'country_origin', 
            'country_study_abroad', 
            'school', 
            'major', 
            'school_start_year', 
            'school_end_year', 
            'living_city'
        )
        
class AboutForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea())
    
    class Meta:
        model = About
        fields = ('body',)
        
class EducationForm(forms.ModelForm):
    # status = forms.CharField(widget=forms.RadioSelect(attrs={'class': 'custom-control-input'}, choices=EducationStatus.choices))
    start_year = forms.ChoiceField(choices=[("*", "Still planning")]  + [(x, x) for x in range(1940, current_year+4)])
    end_year = forms.ChoiceField(choices=[("*", "Still planning")] + [(x, x) for x in range(1940, current_year+10)])

    class Meta:
        model = Education
        fields = ('school', 'major', 'start_year', 'end_year')
        
class WorkExperienceForm(forms.ModelForm):
    # status = forms.CharField(widget=forms.RadioSelect(attrs={'class': 'custom-control-input'}, choices=WorkStatus.choices))
    start_year = forms.ChoiceField(choices=[("*", "Still planning")]  + [(x, x) for x in range(1940, current_year+4)])
    end_year = forms.ChoiceField(choices=[("*", "Still planning")] + [(x, x) for x in range(1940, current_year+10)])

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