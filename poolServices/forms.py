from django.forms import ModelForm
from .models import review

class ReviewForm(ModelForm):
	class Meta:
		model = review
		fields = ['name','location','comments']