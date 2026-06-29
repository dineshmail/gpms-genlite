from django.contrib import admin
from .models import Machine, MaintenanceRequest


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):

    list_display = (
        "machine_code",
        "machine_name",
        "department",
        "location",
        "manufacturer",
        "model_number",
        "status",
    )

    list_filter = (
        "department",
        "status",
        "manufacturer",
    )

    search_fields = (
        "machine_code",
        "machine_name",
        "manufacturer",
        "model_number",
    )

    ordering = (
        "machine_code",
    )

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

    readonly_fields = (
        "request_id",
    )