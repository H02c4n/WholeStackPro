from django.db import models
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=250, null=True, blank=True)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post}--{self.comment}'