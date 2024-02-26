from rest_framework import permissions
from django.contrib.auth import get_user_model
from users.models import User


class IsManageAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.user.is_authenticated:
            a = ["Shop Admin", "Category Admin", "Product Admin"]
            try:
                user_roles = request.user.role.values_list('title', flat=True)
                return any(i in user_roles for i in a)
            except Exception as e:
                pass
