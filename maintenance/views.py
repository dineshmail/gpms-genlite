from django.shortcuts import render
from .models import MaintenanceRequest


def dashboard(request):

    context = {
        "total_requests": MaintenanceRequest.objects.count(),
        "open_requests": MaintenanceRequest.objects.filter(status="Open").count(),
        "assigned_requests": MaintenanceRequest.objects.filter(status="Assigned").count(),
        "progress_requests": MaintenanceRequest.objects.filter(status="In Progress").count(),
        "completed_requests": MaintenanceRequest.objects.filter(status="Completed").count(),
        "critical_requests": MaintenanceRequest.objects.filter(priority="Critical").count(),
        "recent_requests": MaintenanceRequest.objects.order_by("-created_at")[:10],
    }

    return render(
        request,
        "maintenance/dashboard.html",
        context,
    )