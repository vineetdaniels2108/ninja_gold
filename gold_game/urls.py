from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('gold', views.farm_earn),
    path('reset',views.reset)
]