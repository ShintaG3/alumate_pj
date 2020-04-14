
from django import forms
from .models import Message
from django.contrib.auth.models import User


class GeneralMessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(queryset=User.objects.all())
    body = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        user_queryset = kwargs.pop('choices', User.objects.all())
        super().__init__(*args, **kwargs)
        self.fields['receiver'].queryset = user_queryset
    
    class Meta:
        model = Message
        fields = ['receiver', 'body']

class MessageForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea())
    
    class Meta:
        model = Message
        fields = ['body']
