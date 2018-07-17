from employees import models as employee_models
from employees import permissions as employee_permissions
from employees import serializers as employee_serializers
from rest_framework import permissions
from rest_framework import serializers
from rest_framework import viewsets

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import list_route


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

    @list_route(
        methods=('GET',),
        url_path='me'
    )
    def current_employee(self, request: Request) -> Response:
        """
        Retrieves the employee associated with the user in the request

        Args:
            request: Request object

        Returns:
            Response object
        """
        serializer = self.get_serializer_class()
        serializer = serializer(request.user, context={'request': request})
        return Response(serializer.data)
