from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    # path(r'^home/$', views.index, name='home'),
    path(r'home/', views.index, name='home'),
    path(r'', views.index, name='home'),
    path(r'login/', views.login, name='login'),
    path(r'register/', views.register, name='register'),
]
