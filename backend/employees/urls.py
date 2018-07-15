from django.urls import include, path
from employees import views as employee_views
from rest_framework import routers

app_name = 'employees'

router = routers.DefaultRouter()
router.register('employees', employee_views.EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
