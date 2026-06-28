from django.shortcuts import render, redirect
from .models import MaintenanceRequest
from .forms import MaintenanceRequestForm
from dashboard.models import Department
from django.db.models import Q


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
def request_list(request):

    search = request.GET.get("search", "")
    status = request.GET.get("status", "")
    priority = request.GET.get("priority", "")
    department = request.GET.get("department", "")
    sort = request.GET.get("sort", "newest")

    requests = MaintenanceRequest.objects.all()

    if search:
        requests = requests.filter(
            Q(request_id__icontains=search) |
            Q(machine_name__icontains=search) |
            Q(reported_by__icontains=search)
        )

    if status:
        requests = requests.filter(status=status)

    if priority:
        requests = requests.filter(priority=priority)

    if department:
        requests = requests.filter(department_id=department)

    if sort == "oldest":
        requests = requests.order_by("created_at")
    else:
        requests = requests.order_by("-created_at")

    context = {
        "requests": requests,
        "search": search,
        "status": status,
        "priority": priority,
        "department": department,
        "sort": sort,
        "status_choices": MaintenanceRequest.STATUS_CHOICES,
        "priority_choices": MaintenanceRequest.PRIORITY_CHOICES,
        "departments": Department.objects.all(),
    }

    return render(
        request,
        "maintenance/request_list.html",
        context,
    )
def create_request(request):

    if request.method == "POST":
        form = MaintenanceRequestForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("maintenance_request_list")

    else:
        form = MaintenanceRequestForm()

    return render(
        request,
        "maintenance/request_form.html",
        {
            "form": form,
        },
    )
def request_detail(request, pk):

    maintenance_request = MaintenanceRequest.objects.get(pk=pk)

    return render(
        request,
        "maintenance/request_detail.html",
        {
            "request": maintenance_request,
        },
    )
def edit_request(request, pk):

    maintenance_request = MaintenanceRequest.objects.get(pk=pk)

    if request.method == "POST":

        form = MaintenanceRequestForm(
            request.POST,
            instance=maintenance_request,
        )

        if form.is_valid():
            form.save()

            return redirect(
                "maintenance_request_detail",
                pk=maintenance_request.pk,
            )

    else:

        form = MaintenanceRequestForm(
            instance=maintenance_request,
        )

    return render(
        request,
        "maintenance/request_form.html",
        {
            "form": form,
        },
    )
def delete_request(request, pk):

    maintenance_request = MaintenanceRequest.objects.get(pk=pk)

    if request.method == "POST":
        maintenance_request.delete()

        return redirect(
            "maintenance_request_list"
        )

    return render(
        request,
        "maintenance/request_confirm_delete.html",
        {
            "request": maintenance_request,
        },
    )