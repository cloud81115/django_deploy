import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','website.settings')

import django
django.setup()

import random
from boards.models import Board, Topic
from comment.models import Comment
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from faker import Faker
from django.contrib.auth.models import User
from random import choices


fakegen = Faker()
boards =['Django','Python','Javascript','Others','css']

boards =['Django','Python','Javascript','Others','css']
def add_board():
	b = Board.objects.get_or_create(name=random.choice(boards))[0]
	b.save()
	return b

def add_topic(N=1):
	for _ in range(N):
		id = random.randint(1,2)
		board_id=add_board()
		fake_content = fakegen.sentence()
		fake_sub=fakegen.sentence()
		ap = Topic.objects.get_or_create(subject=fake_sub,board=board_id,content=fake_content
			,published_by=User.objects.get(id=id))[0]
		
	return ap

def add_comment(N=2):
	for _ in range(N):
		id = random.randint(1,2)
		fake_text=fakegen.paragraph()
		comment_id = add_topic().pk
		
		c_content_type = ContentType.objects.get_for_model(Topic)
		t = Topic.objects.all()
		f = t.first().pk
		l = t.last().pk
		for _ in range(N):
			ac = Comment.objects.get_or_create(content_type=c_content_type, object_id=random.randint(f,l), 
				text = fake_text, user = User.objects.get(id=id))[0]
		return ac
		
	


# def populate(N):
# 	for i in range(N):
# 		add_comment(10)		
		
add_topic(10)
add_comment(10)		
# reply_post(10)
# populate(10)