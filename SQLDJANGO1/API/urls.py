from django.contrib import admin
from django.urls import path
from basket.views import *


urlpatterns = [
    path('<int:id>', return_API),
    path('delete/', return_APIDelet),
    path('create/', return_APIAdd),
    path('update/', return_APIUpdate),
    path('read/', return_APIRead),
]
