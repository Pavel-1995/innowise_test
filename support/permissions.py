from rest_framework import permissions


class IsAdminOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        SAFE_METHODS = ("DELETE", "UPDATE")
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_staff)
        return bool(request.user and request.user.is_authenticated)
