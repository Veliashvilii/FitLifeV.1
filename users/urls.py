from django.urls import path
from . import views

urlpatterns = [
  path('home', views.user_home, name="user_home"), 
  path('mydiet', views.user_diet, name="user_diet"), 
  path('profile', views.user_profile, name="user_profile"), 
]
