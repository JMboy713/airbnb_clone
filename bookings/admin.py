from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "kind",
        "user",
        "room",
        "experience",
        "checkin",
        "checkout",
        "experience_time",
        "guests",
    )
    list_filter=("kind",)
