from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api_gateway.views import UserGateway, UserJwtToken

router = DefaultRouter()
router.register(r'user', UserGateway, basename='users')
router.register(r'jwt', UserJwtToken, basename='users')

urlpatterns = [
    path('', include(router.urls))
]
