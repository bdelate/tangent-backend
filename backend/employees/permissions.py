from rest_framework import permissions


class CanList(permissions.BasePermission):
    """
    Checks if the user is allowed to request a list of employees
    """

    def has_permission(self, request, view) -> bool:
        """
        If the user is authenticated and is either a manager or superuser,
        then they are allowed to request a list of all employees

        Args:
            request: request object
            view: view from which the permission is being checked

        Returns:
            A boolean granting / denying permission to list all employees
        """
        if not request.user.is_authenticated:
            return False

        if view.action == 'list':
            return request.user.rank == 'Management' or request.user.is_superuser
        return True


class IsOwnerOrManager(permissions.BasePermission):
    """
    Checks if the user is allowed to access a specific employee instance
    """

    def has_permission(self, request, view) -> bool:
        """
        Users must be authenticated to access a specific employee instance

        Args:
            request: request object
            view: view from which the permission is being checked

        Returns:
            A boolean indicating if the user is authenticated
        """
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj) -> bool:
        """
        To access an employee instance, the user must be one of:
        owner, manager, super user

        Args:
            request: request object
            view: view from which the permission is being checked

        Returns:
            A boolean indicating if the user can access the employee instance
        """
        return (obj == request.user
                or request.user.rank == 'Management'
                or request.user.is_superuser)
