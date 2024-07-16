from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/consignado/', include('consignado.urls')),
    path('api/contrib/', include('Contrib.urls')),
]
