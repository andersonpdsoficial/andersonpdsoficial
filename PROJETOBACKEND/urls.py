from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/consignataria/', include('consignataria.urls')),
    path('api/servidor/', include('servidor.urls')),
    path('api/consulta/', include('consulta.urls')),
    path('api/reserva/', include('reserva.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
