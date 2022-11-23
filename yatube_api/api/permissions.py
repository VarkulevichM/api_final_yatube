from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    message = "Нельзя изменять или удалять чужой контент"

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
