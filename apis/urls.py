from rest_framework.routers import DefaultRouter
from django.urls import path, include
from apis.views.user_view import UserRegistrationView, UserListView
from rest_framework_simplejwt.views import (TokenRefreshView, TokenObtainPairView)

router = DefaultRouter()
router.register(r'user', UserRegistrationView, basename='user-registration')
router.register(r'users', UserListView, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
