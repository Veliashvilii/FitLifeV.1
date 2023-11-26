from django.shortcuts import render
import pyrebase

# Create your views here.
from django.http import HttpResponse

def index(request):
  return render(request, 'pages/index.html')

def trainers(request):
  return render(request, 'pages/trainers.html')

def signup(request):
  return render(request, 'pages/signup.html')

def signin(request):
  return render(request, 'pages/signin.html')

def contact(request):
  return render(request, 'pages/contact.html',)

def about(request):
  image_url = "https://images.pexels.com/photos/7242918/pexels-photo-7242918.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  return render(request, 'pages/about.html', {'image_url': image_url})