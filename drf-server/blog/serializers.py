from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField(read_only=True)
    post_id = serializers.IntegerField()
    class Meta:
        model = Comment
        fields = ['id','comment','post', 'post_id','commentor']

class PostSerializers(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title','content', 'comments', 'created_date')


