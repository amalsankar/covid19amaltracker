
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('index/<cn>',views.index, name='index'),
    path('home',views.home ,name='home'),



]
