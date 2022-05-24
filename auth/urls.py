from django.contrib import admin
from django.urls import path,include
from .views import registrationview,authentication

urlpatterns = [
    path('registration/',registrationview),
    path('authorization/',authentication),
]