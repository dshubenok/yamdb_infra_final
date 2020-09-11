from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission


class IsAdminPermission(IsAuthenticated):

    def has_permission(self, request, view):
        is_authenticated = super(IsAdminPermission, self).has_permission(request, view)
        return bool(is_authenticated and (request.user.is_superuser or request.user.role == request.user.ADMIN))


class ReadOnlyPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS)


class IsAuthorOrReadOnlyPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and (
                obj.author == request.user or request.user.role == request.user.MODERATOR
                or request.user.role == request.user.ADMIN or request.user.is_superuser
        )
