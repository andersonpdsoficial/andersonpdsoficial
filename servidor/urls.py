from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServidorViewSet

router = DefaultRouter()
router.register(r'servidores', ServidorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
