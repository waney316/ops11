from rest_framework.permissions import BasePermission
from apps.permission.verify import verify_permission


class ApiRBACPermission(BasePermission):

    def has_permission(self, request, view):
        username = request.user.username
        path = request.META["PATH_INFO"] # uri
        method = request.method
        return verify_permission(username, path, method)