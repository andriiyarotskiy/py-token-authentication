from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        if bool(
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
        ):
            return True
        if request.user.is_staff and request.method == "DELETE":
            return True
        if request.user and request.user.is_staff:
            return True
        return False
