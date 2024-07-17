from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsultaMargemAthenasViewSet

router = DefaultRouter()
router.register(r'consultas', ConsultaMargemAthenasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
