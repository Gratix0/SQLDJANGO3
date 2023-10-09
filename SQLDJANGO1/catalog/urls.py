
from django.contrib import admin
from django.urls import path
from basket.views import *


urlpatterns = [
    path('<int:id>', return_Catalog),
    path('catalog/', return_CatalogCatalog),
    path('catalog/Add/', return_CatalogCatalogAdd),
    path('vivod/', return_CatalogVivodTovara),
    path('vivod/change/', return_CatalogVivodTovaraIzmenenie),
    path('tech/', return_CatalogTechPodderjka),
]
