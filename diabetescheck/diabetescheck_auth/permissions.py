from rest_framework import permissions


class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'POST' or request.method == 'DELETE':
            return True
        return super(
            IsAuthenticatedOrCreate, self).has_permission(request, view)
