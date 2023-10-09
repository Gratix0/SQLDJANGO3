from django.contrib import admin
from django.urls import path
from basket.views import *


urlpatterns = [
    path('<int:id>', return_profile),
]
