
from django import forms
from .models import Post, PostComment, Ask

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


class AskForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Ask
        fields = ['title', ]