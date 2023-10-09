from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def return_basket(responce, id):
    return HttpResponse(f'{id} Корзиночка')

def return_profile(responce, id):
    return HttpResponse(f'{id} Страница личного кабинета')

def return_API(responce, id):
    return HttpResponse(f'{id} Главная страница API')

def return_Catalog(responce, id):
    return HttpResponse(f'{id} Главная страница Catalog')

def return_CatalogCatalog(responce):
    return HttpResponse(f'{id}  страница CatalogCatalog')

def return_CatalogCatalogAdd(responce):
    return HttpResponse(f'{id}  страница CatalogCatalogAdd')

def return_CatalogVivodTovara(responce):
    return HttpResponse(f'{id}  страница VivodTovara')

def return_CatalogVivodTovaraIzmenenie(responce):
    return HttpResponse(f'{id}  страница VivodTovaraIzmenenie')

def return_CatalogTechPodderjka(responce):
    return HttpResponse(f'{id}  страница TechPodderjki')

def return_APIAdd(responce):
    return HttpResponse(f'{id}  страница добавления')

def return_APIDelet(responce):
    return HttpResponse(f'{id}  страница удаления')

def return_APIUpdate(responce):
    return HttpResponse(f'{id}  страница updaate')

def return_APIRead(responce):
    return HttpResponse(f'{id}  страница Read')
