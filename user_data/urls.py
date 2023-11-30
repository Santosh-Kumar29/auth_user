from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apis.urls')),
    path('gateway/', include('api_gateway.urls')),
    path('api/docs/', include('apis.swagger')),
]
