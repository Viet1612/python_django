from django.http import response
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login



# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponse("đăng nhập đi")
    else:
        return render(request, 'pages/index.html')
        
    
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is None:
            print("aaaaaaaaaaaa")
            return HttpResponse("User k tồn tại")
        auth_login(request, user)
        return render(request, 'pages/register.html')

    return render(request, 'pages/login.html')



def register(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You are now able to login')
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, "pages/register.html", {"form":form})
