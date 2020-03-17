from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from accounts.models import UserProfile, current_status, BaseInfo

def status_select():
    return current_status

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Re-enter Password'
        }
    ))

    class Meta:
        model = User
        fields = ('email','username', 'password1', 'password2')

class UserInformationUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', )

class BaseInfoForm(forms.ModelForm):
    country = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'country'
            }
    ))

    school = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'school'
            }
    ))

    course = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'course'
            }
    ))

    status = forms.ChoiceField(
        choices=status_select,
        widget=forms.RadioSelect(
            attrs={
                'class': 'form-control',
                'placeholder': 'status'
            }
        )
    )

    year_of_abroad_study = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Year of abroad study',
                "class": "form-control",
                "value": 2010
            }
        )
    )

    job_before_abroad_study = forms.CharField(
        required=False,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Job before studying abroad'
            }
        )
    )

    job_after_abroad_study = forms.CharField(
        required=False,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Job after studying abroad'
            }
        )
    )

    class Meta:
        model = BaseInfo
        fields = ('status', 'country', 'school', 'course', 'year_of_abroad_study', 'job_before_abroad_study', 'job_after_abroad_study')
