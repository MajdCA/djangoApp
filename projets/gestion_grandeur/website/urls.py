from django.urls import path
from . import views


urlspatterns=[
    path('', views.home_view , name="home")
]