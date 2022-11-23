from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet
from api.views import FollowViewSet
from api.views import GroupViewSet
from api.views import PostViewSet

router = DefaultRouter()
router.register(
    "posts", PostViewSet,
    basename="post"
)
router.register(
    r"posts/(?P<post_id>\d+)/comments",
    CommentViewSet,
    basename="comment"
)
router.register(
    "groups",
    GroupViewSet,
    basename="group"
)
router.register(
    "follow",
    FollowViewSet,
    basename="follow"
)

urlpatterns = [
    path("v1/", include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
