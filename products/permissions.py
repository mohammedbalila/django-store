from rest_framework import permissions


class IsUserOrAdminOrReadOnly(permissions.BasePermission):
    """
    User permission to only allow users or admin to edit it.
    """   
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user

class IsUserOrAdmin(permissions.BasePermission):
    """
    User permission to only allow users or admin.
    """   
    def has_object_permission(self, request, view, obj):
        return request.user or request.user.is_staff

class IsAdmin(permissions.BasePermission):
    """
    User permission to only allow admin.
    """   
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff

class IsUser(permissions.BasePermission):
    """
    User permission to only allow users.
    """   
    def has_object_permission(self, request, view, obj):
        return request.user