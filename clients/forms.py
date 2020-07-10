from django.forms import ModelForm
from .models import *

class repair_form(ModelForm):
	class Meta:
		model = repair_request
		fields = ['name','number','email','message']

class client_form(ModelForm):
	class Meta:
		model = new_client
		fields = ['name','number','email','message']