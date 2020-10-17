from django.urls import path

from . import views

urlpatterns = [
    path('sockets', views.index, name='index')
]
