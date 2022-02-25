from django.http import request
from django.shortcuts import render,HttpResponse
from home.models import Contact,Contribute,Joinus
from datetime import datetime
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"home.html")



def cont(request):
    if request.method =='POST':
         name=request.POST.get('name')
         email=request.POST.get('email')
         issue=request.POST.get('issue')
         contact=Contact(name=name,email=email,issue=issue,date=datetime.today())
         contact.save()
         messages.success(request,'Your response recorded')

   
    return render(request,"contact.html")

def services(request):
    return render(request,"service.html")



def contribute(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        contribution=request.POST.get('contribution')
        center=request.POST.get('center')
        contrib=Contribute(name=name,email=email,contact=contact,contribution=contribution,center=center,date=datetime.today())
        contrib.save()
        

    return render(request,"contribute.html")

def join(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        reason=request.POST.get('reason')
        state=request.POST.get('state')
        city=request.POST.get('city')
        DOB=request.POST.get('DOB')
        gender=request.POST.get('gender')
        occupation=request.POST.get('occupation')
        Join=Joinus(name=name,email=email,contact=contact,reason=reason,state=state,city=city,DOB=DOB,occupation=occupation,gender=gender,Request_date=datetime.today())
        Join.save()

    return render(request,"join.html")

def overview(request):
    return render(request,"overview.html")

def team(request):
    return render(request,"team.html")

def awards(request):
    return render(request,"awards.html")

def vision(request):
    return render(request,"vision.html")

def founder(request):
    return render(request,"founder.html")


