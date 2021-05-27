from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.http import HttpResponseRedirect 
# Create your views here.
def index(request):
    return render(request, 'pages/index.html')
def login(request):
    return render(request, 'pages/login.html')
