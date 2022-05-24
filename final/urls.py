from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('mainApp.urls')),
    path('api/', include ('auth.urls'))
]

