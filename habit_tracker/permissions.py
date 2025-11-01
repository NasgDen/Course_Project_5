from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        print("СРАБОТАЛ PERMISSION")
        return request.user == obj.owner