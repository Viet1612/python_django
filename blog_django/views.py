from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def index(request):
    return render(request, 'pages/index.html')
def login(request):
    return render(request, 'pages/login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        data = User(user_name=username, email=email, passw=password)
        data.save()
    return render(request, 'pages/register.html')