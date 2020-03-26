from django import forms
from .models import UserProfile, Goal

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
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