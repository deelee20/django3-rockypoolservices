from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def repair(request):
	if request.method == "GET":
		return render(request,'clients/repair_form.html', {'form':repair_form()})
	else:
		form = repair_form(request.POST)
		repair_request = form.save()
		return redirect('home')


def new_client(request):
	if request.method == "GET":
		return render(request,'clients/new_client.html', {'form':client_form()})
	else:
		form = client_form(request.POST)
		client = form.save()
		return redirect('home')