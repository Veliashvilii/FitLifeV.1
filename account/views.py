from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import CustomUser
from users.models import UserExtra

# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return render(request, "users/home.html")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_user:
                return render(request, "users/home.html", {"user": request.user})
            else:
                # Teachers Login Here
                return render(
                    request, "users/teachersHome.html", {"user": request.user}
                )
        else:
            return render(
                request, "account/login.html", {"error": "Email or Password Incorrect!"}
            )
    return render(request, "account/login.html")


def user_register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if CustomUser.objects.filter(username=username).exists():
                return render(
                    request,
                    "account/register.html",
                    {
                        "error": "This username is already taken. Please choose another username."
                    },
                )
            else:
                if CustomUser.objects.filter(email=email).exists():
                    return render(
                        request,
                        "account/register.html",
                        {
                            "error": "This email address is already registered. Please use a different email address."
                        },
                    )
                else:
                    user = CustomUser.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                        is_user=True,
                    )
                    user_extra = UserExtra.objects.create(user_id=user.id)
                    user.save()
                    return render(request, "account/login.html")
        else:
            return render(
                request,
                "account/register.html",
                {"error": "Passwords do not match. Please enter matching passwords."},
            )
    else:
        return render(request, "account/register.html")


def user_logout(request):
    logout(request)
    return redirect("/")


def user_forgot(request):
    return render(request, "account/forgot.html")
