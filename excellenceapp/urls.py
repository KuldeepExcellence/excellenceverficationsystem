from django.contrib import admin
from django.urls import path,include
from excellenceapp import views

urlpatterns = [
    path('verify',views.verify,name="verify"),
    path("",views.home,name="home")
]
