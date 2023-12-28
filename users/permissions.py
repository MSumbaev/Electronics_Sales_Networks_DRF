from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    """User может просматривать и обновлять только свой профиль"""
    def has_object_permission(self, request, view, obj):
        if request.user.username == obj.username:
            return True
        return False
