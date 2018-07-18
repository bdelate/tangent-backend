from rest_framework import permissions


class CanListCreateDelete(permissions.BasePermission):
    """
    Managers have full permissions. Non managers are not allowed to
    list, create or delete employees.
    """

    def has_permission(self, request, view) -> bool:
        """
        The user has permission if they are authenticated and are either
        a Manager or the action is not one of list, create, destroy

        Args:
            request: request object
            view: view from which the permission is being checked

        Returns:
            A boolean indicating if the user has permission
        """
        if not request.user.is_authenticated:
            return False

        if request.user.rank == 'Management':
            return True

        if view.action in ['list', 'create', 'destroy']:
            return False

        return True


class IsOwnerOrManager(permissions.BasePermission):
    """
    Managers have full permissions. Non managers are only allowed to
    access and update their own employee instance
    """

    def has_object_permission(self, request, view, obj) -> bool:
        """
        Check that the user is a manager or is accessing their own
        employee instance.

        Args:
            request: request object
            view: view from which the permission is being checked

        Returns:
            A boolean indicating if the user can access the employee instance
        """
        return obj == request.user or request.user.rank == 'Management'
