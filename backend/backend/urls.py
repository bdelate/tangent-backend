from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token


# API documentation
documentation = include_docs_urls(
    title='Employee Management System',
    public=False,
    permission_classes=[])

urlpatterns = [
    path('', documentation),
    path('api/', include('employees.urls', namespace='employees')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('obtain-auth-token/', obtain_jwt_token),
    path('admin/', admin.site.urls),
]
