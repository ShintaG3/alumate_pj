from django.contrib.auth.models import User
from django.views import View
from .models import Post, PostLike
from .forms import PostForm, PostCommentForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin

class PostView(LoginRequiredMixin, View):
    template_name = 'feed/feed.html'
    form_class = PostForm
    permission_required = ''

    def get(self, request, *args, **kwargs):
        context = {
            'view': 'Post',
            'new_post_form': self.form_class(),
            'comment_form': PostCommentForm(),
            'post_list': self.get_post_list(request.user)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return HttpResponseRedirect(self.request.path_info) # redirect to the same page

    def get_post_list(self, user):
        posts = Post.objects.all()[:10]
        post_list = []
        
        for post in posts:
            try:
                liked = PostLike.objects.get(user=user, post=post)
            except PostLike.DoesNotExist:
                liked = None
            post_list.append({
                'value': post,
                'liked': liked,
            })
        return post_list
        
class PostCommentView(LoginRequiredMixin, View):
    form_class = PostCommentForm
    template_name = 'feed/feed.html'
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        post = Post.objects.get(pk=kwargs['post_id'])
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.post = post
            comment.save()
            
            return HttpResponseRedirect('/feed/')


class PostLikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        post = Post.objects.get(pk=kwargs['post_id'])
        try:
            like = PostLike.objects.get(user=user, post=post)
            like.delete()
        except PostLike.DoesNotExist:
            PostLike(user=user, post=post).save()
            
        return redirect('/feed/')