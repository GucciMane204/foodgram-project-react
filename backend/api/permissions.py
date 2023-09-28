from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """Разрешение изменять и удалять объекты только автору,
    всем остальным доступно лишь чтение."""

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.method in SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """Разрешание изменять и удалять данные только админу,
    всем остальным доступно лишь чтение."""

    def has_permission(self, request, view):
        return (
            True
            if request.method in SAFE_METHODS
            else request.user and request.user.is_superuser
        )
