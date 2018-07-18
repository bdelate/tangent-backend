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
    """
    Allows for employee CRUD operations

    list:
    List all employees. Only available to managers.

    create:
    Create a new employee. Only available to managers.

    current_employee:
    Retrieve the employee instance for the currently logged in user.

    read:
    Retrieves the employee instance for the specified employee by id.

    update:
    Update an employee instance. All fields are required. Non managers can
    only update their own instance.

    partial_update:
    Update only the specified employee instance fields. Non managers can
    only partially update their own instance.

    delete:
    Delete an employee instance. Only available to managers.
    """
    queryset = employee_models.Employee.objects.all()
    permission_classes = (
        employee_permissions.CanListCreateDelete,
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
