from employees import models as employee_models
from employees import serializers as employee_serializers
from rest_framework import viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    """Allows for employee CRUD operations"""
    queryset = employee_models.Employee.objects.all()
    serializer_class = employee_serializers.EmployeeSerializer
