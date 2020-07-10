from django.shortcuts import render, redirect
from .models import *
from .forms import ReviewForm

def home(request):
	services = MonthlyService.objects.all()
	reviews = review.objects.order_by('-id')[:3]
	return render(request, 'poolServices/home.html', {'services':services,'reviews':reviews})

def services_page(request):
	services = MonthlyService.objects.all()
	return render(request, 'poolServices/services.html', {'services':services})

def createReview(request):
	if request.method == "GET":
		return render(request,'poolServices/createReview.html', {'form':ReviewForm()})
	else:
		form = ReviewForm(request.POST)
		newReview = form.save()
		return redirect('createReview')

def review_page(request):
	reviews = review.objects.all()
	return render(request, 'poolServices/reviews.html', {'reviews':reviews})