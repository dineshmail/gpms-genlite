from django.shortcuts import render

from production.models import (
    Department,
    Issue,
    ProductionUpdate,
    AssetStock
)

def home(request):
    context = {
        "department_count": Department.objects.count(),
        "issue_count": Issue.objects.count(),
        "production_count": ProductionUpdate.objects.count(),
        "asset_count": AssetStock.objects.count(),
    }

    return render(request, "dashboard/home.html", context)