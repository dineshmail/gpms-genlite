from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from production.models import (
    Department,
    Issue,
    ProductionUpdate,
    AssetStock
)
@login_required
def dashboard(request):
    return render(
        request,
        "dashboard/index.html"
    )

def home(request):

    open_issues = Issue.objects.exclude(status="Closed")[:10]

    recent_updates = ProductionUpdate.objects.order_by("-created_at")[:10]

    context = {
        "department_count": Department.objects.count(),
        "issue_count": Issue.objects.count(),
        "production_count": ProductionUpdate.objects.count(),
        "asset_count": AssetStock.objects.count(),

        "open_issues": open_issues,
        "recent_updates": recent_updates,
    }

    return render(request, "dashboard/home.html", context)