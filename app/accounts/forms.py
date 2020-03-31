from django import forms
from .models import BasicInfo, current_status

class BasicInfoForm(forms.ModelForm):
    status = forms.RadioSelect(choices=current_status)
    
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