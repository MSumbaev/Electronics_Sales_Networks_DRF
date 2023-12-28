from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    """User может и обновлять и удалять только свой продукт и звено сети"""
    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False
