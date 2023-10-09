from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basket/', include("basket.urls")),
    path('profile/', include("Profile.urls")),
    path('API/', include("API.urls")),
    path('catalog/', include("catalog.urls")),zzzx
]
