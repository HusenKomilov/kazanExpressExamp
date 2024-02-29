from rest_framework import permissions
from django.contrib.auth import get_user_model
from users.models import User


class IsProductAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.user.is_authenticated:
            try:
                if request.user.role.filter(title="Product Admin"):
                    return True
            except Exception as e:
                pass


class IsCategoryAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.user.is_authenticated:
            try:
                if request.user.role.filter(title="Category Admin"):
                    return True
            except Exception as e:
                pass


class IsShopAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.user.is_authenticated:
            try:
                if request.user.role.filter(title="Shop Admin"):
                    return True
            except Exception as e:
                pass
