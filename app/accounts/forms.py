from django import forms
from datetime import date
from .models import BasicInfo, CurrentStatus, About

class BasicInfoForm(forms.ModelForm):
    current_year = date.today().year
    status = forms.CharField(widget=forms.RadioSelect(choices=CurrentStatus.choices))
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