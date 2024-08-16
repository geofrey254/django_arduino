from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from ctrl import views

urlpatterns = [
    path('serial/', views.switcherView),
]

urlpatterns = format_suffix_patterns(urlpatterns)
