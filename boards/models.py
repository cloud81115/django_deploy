from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from django.contrib.contenttypes.fields import GenericRelation
from django.shortcuts import get_object_or_404
# Create your models here.
class Board(models.Model):
	name = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Topic(models.Model):
	subject = models.CharField(max_length=255)
	content = models.TextField(max_length=4000)
	board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
	published_at = models.DateTimeField(auto_now_add=True)
	published_by = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
	views = models.PositiveIntegerField(default=0)

	topic_comment = GenericRelation(Comment, related_query_name = 'comments')#可以從Topic查comment數
	def __str__(self):
		return self.subject
	
