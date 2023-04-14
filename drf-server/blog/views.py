from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post,Comment
from .serializers import PostSerializers, CommentSerializer
# Create your views here.


class CommentMVS(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostMVS(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

