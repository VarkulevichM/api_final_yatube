from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment
from posts.models import Follow
from posts.models import Group
from posts.models import Post
from posts.models import User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ("author",)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ("author", "post")


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = '__all__'
        read_only_fields = ("user",)

    validators = [
        UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=("user", "following"),
            message="Вы уже подписаны на этого автора"
        )
    ]

    def validate(self, attrs):
        user = self.context["request"].user

        if user == attrs["following"]:
            raise serializers.ValidationError(
                "Ну нельзя же подписываться на себя, ну вы чего!"
            )

        return attrs
