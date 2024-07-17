from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsignatariaViewSet

router = DefaultRouter()
router.register(r'consignatarias', ConsignatariaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
