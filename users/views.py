from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def user_home(request):
  return render(request, 'users/home.html')

def user_diet(request):
  return render(request, 'users/mydiet.html')

def user_profile(request):
  return render(request, 'users/profile.html')
