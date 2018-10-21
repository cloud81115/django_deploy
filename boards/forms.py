from django.forms import  Textarea, ModelForm,TextInput
from .models import Topic
class NewTopicForm(ModelForm):
	class Meta:
		model = Topic
		fields = ['subject','content']
		# widgets = {
		# 	'subject' : TextInput(attrs={'class':'form-control'}),
  #           'content': Textarea(attrs={'class':'form-control'}),
  #       }