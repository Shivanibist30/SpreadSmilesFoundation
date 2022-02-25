"""DjangoOne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from home.views import home
from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Admin Harry IceCreams"  #login title,nav bar title
admin.site.site_title = "Admin Harry"  #
admin.site.index_title = "Welcome to Harry IceCreams" #nav bar ke niche

urlpatterns = [
    path('admin/', admin.site.urls), 
    path("", views.home, name='home' ),
    path('overview', views.overview, name="overview" ),
    path('contact', views.cont, name="contact" ),
    path('contribute', views.contribute, name="contribute" ),
    path('join', views.join, name="join" ),
    path('vision', views.vision, name="vision" ),
    path('founder', views.founder, name="founder" ),
    path('awards', views.awards, name="awards" ),
    path('team', views.team, name="team" ),


]
