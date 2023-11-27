from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def user_home(request):
  return render(request, 'users/home.html')

def user_diet(request):
  return render(request, 'users/mydiet.html')

def user_profile(request):
  if request.method == "GET":
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    username = request.user.username
    is_active = request.user.is_active
    print(first_name, last_name, email, username, is_active)
    return render(request, 'users/profile.html',{
      'first_name': first_name,
      'last_name': last_name,
      'email': email,
      'username': username,
      'is_active': is_active,
    })
  elif request.method == "POST":
    pass
  else:
    pass
