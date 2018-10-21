from django.urls import path, re_path
from . import views


urlpatterns = [
	re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply, name='reply'),
	# path('update_comment', views.update_comment, name='update_comment')
]