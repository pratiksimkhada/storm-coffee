import datetime
from pickle import TRUE
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from .models import WebsiteInfo, SliderImages, WhyUs
from .forms import ContactForm 



def home(request):
	information = WebsiteInfo.objects.all()
	info = information[0]

	images = SliderImages.objects.all()

	time = datetime.datetime.now()	
	hour = time.strftime('%H')
	
	context={
		'info' : info,
		'images': images,
		'hour': hour,
	}
	return render(request, 'home.html', context)