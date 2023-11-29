from django.contrib import admin
from .models import Genre, MovieType, Cinema, CinemaRoom, Movie, Showday, Customer, Ticket, Discount, VerifierDevice, VerifierDeviceType, Verifier, RoomSeat, Offer
# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name", "description"]
    list_filter = ("name", "description")
    ordering = ("name", "description")
    fieldsets = (
        ("Genre", {
            "fields": ("name", "description")
        }),
    )

class MovieTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name", "description"]
    list_filter = ("name", "description")
    ordering = ("name", "description")
    fieldsets = (
        ("Movie Type", {
            "fields": ("name", "description")
        }),
    )




admin.site.register(Genre)
admin.site.register(MovieType)
admin.site.register(Cinema)
admin.site.register(CinemaRoom)
admin.site.register(RoomSeat)
admin.site.register(Movie)
admin.site.register(Showday)
admin.site.register(Customer)
admin.site.register(Ticket)
admin.site.register(Discount)
admin.site.register(VerifierDeviceType)
admin.site.register(VerifierDevice)
admin.site.register(Verifier)
admin.site.register(Offer)


