from employees import models as employee_models
from employees import permissions as employee_permissions
from employees import serializers as employee_serializers
from rest_framework import permissions
from rest_framework import serializers
from rest_framework import viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    """Allows for employee CRUD operations"""
    queryset = employee_models.Employee.objects.all()
    permission_classes = (
        employee_permissions.CanList,
        employee_permissions.IsOwnerOrManager
    )

    def get_serializer_class(self) -> serializers.ModelSerializer:
        """
        Employee rank determines which serializer to use

        Returns:
            ModelSerializer
        """
        if self.request.user.rank == 'Management':
            return employee_serializers.ManagerSerializer
        return employee_serializers.EmployeeSerializer
