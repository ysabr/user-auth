from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('register/', views.register),
    path('login/', views.my_Login),
    path('dashboard/', views.dashboard),
]
