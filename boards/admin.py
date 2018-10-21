from django.contrib import admin
from .models import Board, Topic
# Register your models here.
# admin.site.register(Board)
@admin.register(Board)
class BoardTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
@admin.register(Topic)
# admin.site.register(Topic)
class TopicTypeAdmin(admin.ModelAdmin):
	list_display = ('id','subject', 'content')