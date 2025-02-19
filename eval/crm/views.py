from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(req):
    return render(req, '/crm/homepage.html')

def register(req):
    return render(req, '/crm/register.html')
    

def my_Login(req):
    return render(req, '/crm/login.html')

def dashboard(req):
    return render(req, '/crm/dashboard.html')
