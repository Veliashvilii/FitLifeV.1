from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import models

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
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    username = request.POST["username"]
    birthday = request.POST["birthday"]
    gender = request.POST["gender"]
    password = request.POST["password"]
    repassword = request.POST["repassword"]
    profile_picture = request.POST["profile_picture"]

    if password != "":
      if password == repassword:
        # Match the passwords
        if User.objects.filter(username=username).exists():
          # Match the username from database. So you can't use this username.
          return render(request, 'users/profile.html', {"error":"This username is already taken. Please choose another username."})
        else:
          # Doesn't match the username from databas. So you can use this username.
          # Update request.user
          request.user.first_name = first_name
          request.user.last_name = last_name
          request.user.email = email
          request.user.username = username
          request.user.set_password(password)
          request.user.save()
          # Create or update user_profile
          user_profile, created = models.UserExtra.objects.get_or_create(user=request.user)
          user_profile.phone_number = phone
          user_profile.birth_date = birthday
          user_profile.gender = gender
          if profile_picture:
              user_profile.profile_picture = profile_picture
          user_profile.save()
        return render(request, 'users/home.html')
      else:
        # Not match the passwords
        return render(request, 'users/profile.html', {"error":"Passwords do not match. Please enter matching passwords."})
    else:
      # Passwords equals zero. No Input!
      if User.objects.filter(username=username).exists():
          # Match the username from database. So you can't use this username.
          return render(request, 'users/profile.html', {"error":"This username is already taken. Please choose another username."})
      else:
          # Doesn't match the username from databas. So you can use this username.
          # Update request.user
          request.user.first_name = first_name
          request.user.last_name = last_name
          request.user.email = email
          request.user.username = username
          request.user.save()
          # Create or update user_profile
          user_profile, created = models.UserExtra.objects.get_or_create(user=request.user)
          user_profile.phone_number = phone
          user_profile.birth_date = birthday
          user_profile.gender = gender
          if profile_picture:
              user_profile.profile_picture = profile_picture
          user_profile.save()
          return render(request, 'users/home.html')
  else:
    pass
