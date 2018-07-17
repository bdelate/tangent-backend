from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('api/', include('employees.urls', namespace='employees')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('obtain-auth-token/', obtain_jwt_token),
    path('admin/', admin.site.urls),
]
