from django.urls import path, include
from .views import PostMVS, CommentMVS
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('posts', PostMVS)
router.register('comments', CommentMVS)

urlpatterns = [
    path('', include(router.urls))
]
