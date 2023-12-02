from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import models
from .models import UserExtra, TeacherExtra

# Create your views here.


def user_home(request):
    return render(request, "users/home.html")


def user_diet(request):
    return render(request, "users/mydiet.html")


def user_profile(request):
    user = request.user
    user_extra = UserExtra.objects.get(user=user)
    if request.method == "GET":
        return render(
            request,
            "users/profile.html",
            {
                "user": user,
                "user_extra": user_extra,
            },
        )
    elif request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")

        phone_number = request.POST.get("phone_number")
        birth_date = request.POST.get("birth_date")
        gender = request.POST.get("gender")
        profile_picture = request.FILES.get("profile_picture")

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.save()

        user_extra.phone_number = phone_number
        user_extra.birth_date = birth_date
        user_extra.gender = gender
        if profile_picture:
            user_extra.profile_picture = profile_picture
        user_extra.save()

        return render(
            request,
            "users/profile.html",
            {
                "user": user,
                "user_extra": user_extra,
            },
        )


def teacher_home(request):
    return render(request, "users/teachersHome.html")


def teachers_students(request):
    return render(request, "users/teachersStudent.html")


def teacher_profile(request):
    if request.method == "GET":
        user = request.user
        # Kullanıcının TeacherExtra kaydını alın, eğer yoksa oluşturun.
        teacher_extra, created = TeacherExtra.objects.get_or_create(
            user=user, defaults={}
        )
        return render(
            request,
            "users/teachersProfile.html",
            {
                "user": user,
                "teacher_extra": teacher_extra,
            },
        )
