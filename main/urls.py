from django.urls import path
from main.views import index, about, contact, success, welcome, register

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contact/', contact),
    path('welcome/', welcome),
    path('success', success),
    #path('login/', login),
    path('register/', register),
]