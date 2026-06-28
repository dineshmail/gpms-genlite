from django.db import models
from dashboard.models import Department


class MaintenanceRequest(models.Model):

    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Critical", "Critical"),
    ]

    STATUS_CHOICES = [
        ("Open", "Open"),
        ("Assigned", "Assigned"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    request_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
    )

    machine_name = models.CharField(
        max_length=150,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    reported_by = models.CharField(
        max_length=100,
    )

    problem_description = models.TextField()

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="Medium",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Open",
    )

    assigned_engineer = models.CharField(
        max_length=100,
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.request_id} - {self.machine_name}"