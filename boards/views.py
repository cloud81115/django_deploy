from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Topic
from .forms import NewTopicForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from django.core.paginator import Paginator
from django.db.models import Q
from comment.forms import CommentForm
# Create your views here.

def home(request):
	boards = Board.objects.all()
	recent_topics = Topic.objects.all().order_by('-published_at')[:5]
	return render(request, 'home.html', {'boards':boards, 'recent_topics':recent_topics})
def topic_list(request, pk):
	board = get_object_or_404(Board, pk=pk)
	topic_list = board.topics.all().order_by('-published_at')

	query = request.GET.get('q')
	if query:
		topic_list = topic_list.filter(
			Q(subject__icontains=query)|
			Q(content__icontains=query)|
			Q(published_by__first_name__icontains=query)|
			Q(published_by__username__icontains=query)
			).distinct()

	paginator = Paginator(topic_list, 5)
	page_num = request.GET.get('page',1)#get url頁面參數
	page_of_topic_list = paginator.get_page(page_num)


	return render(request, 'topic_list.html', {'topic_list':topic_list,'board':board, 'page_of_topic_list':page_of_topic_list})

@login_required(login_url='/login/')
def new_topic(request, pk):
	board = get_object_or_404(Board, pk=pk)
	# user = User.objects.first()
	if request.method =='POST':
		form = NewTopicForm(request.POST or None)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.board = board
			topic.published_by = request.user
			topic.save()
			# topic_content = Topic.objects.create(subject = form.cleaned_data.get('subject'),
			# 	content = form.cleaned_data.get('content'),
			# 	board = board,
			# 	puplished_by = user)
			return redirect('topic_list', pk=board.pk)
		# form = NewTopicForm(request.POST)
		# if form.is_valid():
		# 	topic = form.save(commit=False)
		# 	topic.board = board
		# 	topic.published_by = user
	else:
		form = NewTopicForm()	
	return render(request, 'new_topic.html', {'board': board, 'form':form})
def topic_view(request, pk, topic_pk):
	topic_view = get_object_or_404(Topic, board__pk =pk, pk=topic_pk)
	if not request.COOKIES.get('topic_%s_readed' % topic_pk):
		topic_view.views+=1
		topic_view.save()
	
	topic_view_content_type = ContentType.objects.get_for_model(topic_view)
	comments = Comment.objects.filter(content_type=topic_view_content_type, object_id=topic_view.pk)

	#初始data
	topic_content_type = ContentType.objects.get_for_model(topic_view)
	data = {}
	data['content_type'] = topic_content_type
	data['object_id'] = topic_pk
	comment_form = CommentForm(initial=data)
	#
	if request.method =='POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			comment = Comment()
			comment.user = request.user
			comment.text = comment_form.cleaned_data['text']
			obj_id = comment_form.cleaned_data['object_id']
			comment.object_id = obj_id

			c_content_type = comment_form.cleaned_data['content_type']#拿到topic這個model
			content_type = ContentType.objects.get(model=c_content_type)
			comment.content_type = content_type
			comment.save()
			return redirect('topic_view', pk, topic_pk)

	response = render(request, 'topic_view.html',{'topic_view':topic_view, 'comments':comments,'comment_form':comment_form})
	response.set_cookie('topic_%s_readed' % topic_pk, 'true')
	return response


def edit_topic(request,pk,topic_pk):
	topic_view = get_object_or_404(Topic, board__pk =pk, pk=topic_pk)
	board = get_object_or_404(Board, pk=pk)
	
	#加入instance將資料顯示於form上
	form = NewTopicForm(request.POST or None,instance=topic_view)
	if form.is_valid():
		topic = form.save(commit=False)
		topic.published_by = request.user
		topic.save()
		return redirect('topic_view', pk, topic_pk)
	return render(request, 'edit_topic.html',{'board':board,'form':form,'topic_view':topic_view})

def delete_topic(request,pk,topic_pk):
	topic_view = get_object_or_404(Topic, board__pk =pk, pk=topic_pk)
	topic_view.delete()
	return redirect('topic_list', pk)