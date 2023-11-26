from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.user_login, name="user_login"),
    path('register', views.user_register, name="user_register"),
    path('forgot', views.user_forgot, name="user_forgot"),
    path('logout', views.user_logout, name="user_logout"), 
    path('users/', include('users.urls')),
]
