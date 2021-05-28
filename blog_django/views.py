from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages



# Create your views here.
def index(request):

    return render(request, 'pages/index.html')
        
    
def login(request):
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
