
from django import forms
from .models import Post, PostComment

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea())
    
    class Meta:
        model = Post
        fields = ['body', 'image']


class PostCommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea())
    
    class Meta:
        model = PostComment
        fields = ['body', ]