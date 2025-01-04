from django.urls import path
from apps.core import views

urlpatterns = [
    path('home', views.home, name='home'),
]
