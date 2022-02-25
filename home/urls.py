from django.contrib import admin
from django.urls import path,include



urlpatterns = [
  
    path('home', include("home.urls")),
   
    path('contact', include("home.urls")),
    path('contribute', include("home.urls")),
    path('join', include("home.urls")),
    path('overview', include("home.urls")),
    path('vision', include("home.urls")),
    path('awards', include("home.urls")),
    path('team', include("home.urls")),
    path('founder', include("home.urls")),
   
]