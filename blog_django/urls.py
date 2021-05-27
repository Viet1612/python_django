from django.urls import path
from . import views

urlpatterns = [
    path(r'home/', views.index, name='home'),
    path(r'', views.index, name='home'),
    path(r'login/', views.login, name='login'),
    # path(r'register/', views.register, name='register'),
]
