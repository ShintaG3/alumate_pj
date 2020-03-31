from django.contrib.auth.models import User
from django.views import View
from .models import Post
from .forms import PostForm, PostCommentForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin

class PostView(LoginRequiredMixin, View):
    template_name = 'feed/feed.html'
    form_class = PostForm
    permission_required = ''

    def get(self, request, *args, **kwargs):
        object_list = Post.objects.all()
        post_form = self.form_class()
        comment_form = PostCommentForm()
        context = {
            'post_form': post_form,
            'comment_form': comment_form,
            'posts': object_list
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return HttpResponseRedirect(self.request.path_info) # redirect to the same page


class PostCommentView(LoginRequiredMixin, View):
    form_class = PostCommentForm
    template_name = 'feed/feed.html'
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.post = get_object_or_404(Post, pk=kwargs['post_id'])
            comment.save()
            return HttpResponseRedirect('/feed/')
