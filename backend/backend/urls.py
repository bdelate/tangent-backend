from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('employees.urls', namespace='employees')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
