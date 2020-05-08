from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import Post, PostComment, PostLike, PostCommentLike
from .serializers import PostSerializer, PostCommentSerializer, PostLikeSerializer, PostCommentLikeSerializer

# list / create view
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self, request, *args, **kwargs):
        user = get_object_or_404(User, kwargs.pop('id'))
        return super().get_queryset().filter(user=user)

    def create(self, request):
        request.data['user'] = request.user.pk
        return super().create(request)


class PostCommentList(generics.ListCreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer

    def get_queryset(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs.pop('id'))
        return super().get_queryset().filter(post=post)

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.pk
        post = get_object_or_404(Post, id=kwargs.pop('id'))
        request.data['post'] = post.pk
        return super().create(request)


class PostLikeList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, id=kwargs.pop('id'))
        return post.likes

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.pk
        post = get_object_or_404(Post, id=kwargs.pop('id'))
        request.data['post'] = post.pk
        return super().create(request)


class PostCommentLikeList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        comment = get_object_or_404(PostComment, id=kwargs.pop('id'))
        return comment.likes

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.pk
        comment = get_object_or_404(PostComment, id=kwargs.pop('id'))
        request.data['comment'] = comment.pk
        return super().create(request)

# detail view
class PostDetail(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        obj_id = kwargs.pop('id')
        user = self.request.user
        return get_object_or_404(queryset, user=user, id=obj_id)


class PostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer

    def get_object(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        obj_id = kwargs.pop('id')
        user = self.request.user
        return get_object_or_404(queryset, user=user, id=obj_id)


class PostLikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer

    def get_object(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        obj_id = kwargs.pop('id')
        user = self.request.user
        return get_object_or_404(queryset, user=user, id=obj_id)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostCommentLike.objects.all()
    serializer_class = PostCommentLikeSerializer

    def get_object(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        obj_id = kwargs.pop('id')
        user = self.request.user
        return get_object_or_404(queryset, user=user, id=obj_id)
