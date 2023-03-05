from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


v1_router = DefaultRouter()

v1_router.register(r'v1/posts', PostViewSet, basename='post')
v1_router.register(r'v1/groups', GroupViewSet, basename='group')
v1_router.register(r'v1/follow', FollowViewSet, basename='follow')
v1_router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments',
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
