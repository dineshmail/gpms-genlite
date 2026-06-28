from django.contrib import admin
from .models import MaintenanceRequest


@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(admin.ModelAdmin):

    list_display = (
        "request_id",
        "machine_name",
        "department",
        "priority",
        "status",
        "assigned_engineer",
        "created_at",
    )

    list_filter = (
        "department",
        "priority",
        "status",
    )

    search_fields = (
        "request_id",
        "machine_name",
        "reported_by",
    )

    ordering = (
        "-created_at",
    )