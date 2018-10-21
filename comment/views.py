from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from boards.models import Topic
from .models import Comment
from comment.forms import CommentForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def reply(request, pk, topic_pk):
	topic = get_object_or_404(Topic, board__pk =pk, pk=topic_pk)
	topic_content_type = ContentType.objects.get_for_model(topic)
	data = {}
	data['content_type'] = topic_content_type
	data['object_id'] = topic_pk
	comment_form = CommentForm(initial=data)
	

	return render(request, 'reply.html',{'topic':topic, 'comment_form':comment_form})

# def update_comment(request):
# 	comment_form = CommentForm(request.POST)
# 	if comment_form.is_valid():
# 		comment = Comment()
# 		comment.user = request.user
# 		comment.text = comment_form.cleaned_data['text']
# 		obj_id = comment_form.cleaned_data['object_id']
# 		comment.object_id = obj_id

# 		c_content_type = comment_form.cleaned_data['content_type']#拿到topic這個model
# 		content_type = ContentType.objects.get(model=c_content_type)
# 		comment.content_type = content_type
# 		comment.save()
# 		return redirect('home')



		


	
	


