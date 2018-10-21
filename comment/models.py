from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.utils.html import mark_safe
from markdown import markdown
# Create your models here.
class Comment(models.Model):
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	
	text = models.TextField()
	comment_time = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		truncated_text = Truncator(self.text)
		return truncated_text.chars(30)
	def get_last_comment(self):
		 Comment.objects.filter(comments__board=self).order_by('-comment_time').first()
	def get_text_as_markdown(self):
		return mark_safe(markdown(self.text, safe_mode='escape'))
