from django.forms import ModelForm

from .models import ThreadModel, CommentModel





class ThreadForm(ModelForm):
	class Meta:
		model = ThreadModel
		fields = ['category', 'title', 'description', 'tags']



class CommentForm(ModelForm):
	class Meta:
		model = CommentModel
		fields = ['text']






