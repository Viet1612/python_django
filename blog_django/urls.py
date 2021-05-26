from django.urls import path
from . import views

urlpatterns = [
    path(r'home/', views.index, name='home'),
    path(r'^(?P<page_id>[0-9]+)/$', views.index, name='home'),
    path(r'login/', views.login, name='login'),
    path(r'register/', views.register, name='register'),
]
