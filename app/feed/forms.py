
from django import forms
from .models import Post

class FeedPostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea())
    
    class Meta:
        model = Post
        fields = ['body', 'image']