from rest_framework import permissions
from rest_framework.views import Request, View

class IsAdminOrOwner(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return (request.user.is_authenticated and request.user.is_superuser) or request.user.id == view.kwargs.get("user_id")