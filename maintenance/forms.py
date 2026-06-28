from django import forms
from .models import MaintenanceRequest


class MaintenanceRequestForm(forms.ModelForm):

    class Meta:
        model = MaintenanceRequest

        fields = [
            "machine_name",
            "department",
            "reported_by",
            "problem_description",
            "priority",
            "status",
            "assigned_engineer",
            "remarks",
        ]