from django.contrib.auth.models import User
from django.views import View
from .models import Post
from .forms import FeedPostForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

class PostView(View):
    form_class = FeedPostForm
    template_name = 'feed/feed.html'

    def get(self, request, *args, **kwargs):
        object_list = Post.objects.all()
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'posts': object_list})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return HttpResponseRedirect(self.request.path_info) # redirect to the same page
