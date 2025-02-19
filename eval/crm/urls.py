from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.my_Login, name = 'login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
