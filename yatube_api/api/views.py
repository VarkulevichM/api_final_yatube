from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.permissions import AuthorOrReadOnly
from api.serializers import CommentSerializer
from api.serializers import FollowSerializer
from api.serializers import GroupSerializer
from api.serializers import PostSerializer
from posts.models import Group
from posts.models import Post
from posts.models import User


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AuthorOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):

        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        queryset = post.comments.all()

        return queryset

    def perform_create(self, serializer):

        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("following__username",)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        user = get_object_or_404(User,  username=self.request.user)
        queryset = user.follower.all()

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
