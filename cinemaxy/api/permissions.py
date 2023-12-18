from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser
from .models import Ticket


class IsVerifierOrAdminOrReadOnly(IsAdminUser):
    """
    The request is authenticated as a verifier of , or is a read-only request.
    """
    def has_permission(self, request, view):
        admin_permission = super().has_permission(request, view)
        return (
            request.method in SAFE_METHODS or
            admin_permission or
            request.user.is_verifier
        )
    def has_object_permission(self, request, view, obj):
        admin_permission = super().has_object_permission(request, view, obj)
        return (
            request.method in SAFE_METHODS or
            admin_permission or
            request.user.is_verifier
        )


class HasTicket(BasePermission):
    """
    The request is authenticated as a user who has a ticket.
    """
    def has_permission(self, request, view):

        return request.user.has_ticket
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            request.user.is_staff
        )
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)
