from rest_framework import permissions
from rest_framework.views import Request, View


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, username: str) -> bool:
        return username == request.user or request.user.is_superuser
