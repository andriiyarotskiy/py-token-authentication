from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        supported_delete = hasattr(view, "destroy")
        if request.method == "DELETE":
            if not supported_delete:
                return True
            return bool(request.user and request.user.is_staff)
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        if request.user and request.user.is_staff:
            return True
        return False
