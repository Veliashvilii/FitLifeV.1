from django.urls import path
from . import views

urlpatterns = [
  path('', views.index,),    
  path('index', views.index),    
  path('trainers', views.trainers),    
  path('signup', views.signup),
  path('signin', views.signin),    
  path('contact', views.contact),    
  path('about', views.about),       
]
