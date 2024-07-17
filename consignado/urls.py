from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsignatariaViewSet, ConsultaMargemAthenasViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'consignatarias', ConsignatariaViewSet)
router.register(r'consultas', ConsultaMargemAthenasViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
