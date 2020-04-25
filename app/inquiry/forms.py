from .models import AskComment
from django import forms

class AskCommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea())
    
    class Meta:
        model = AskComment
        fields = ['body', ]
