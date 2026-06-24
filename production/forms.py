from django import forms
from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue

        fields = [
            "issue_id",
            "department",
            "title",
            "description",
            "priority",
            "status",
        ]