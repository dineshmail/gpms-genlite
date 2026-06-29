from django.shortcuts import render, redirect
from .models import MaintenanceRequest, Machine
from .forms import MaintenanceRequestForm
from dashboard.models import Department
from django.db.models import Q
from .models import Engineer



def dashboard(request):

    context = {

        # Maintenance Requests
        "total_requests": MaintenanceRequest.objects.count(),
        "open_requests": MaintenanceRequest.objects.filter(status="Open").count(),
        "assigned_requests": MaintenanceRequest.objects.filter(status="Assigned").count(),
        "progress_requests": MaintenanceRequest.objects.filter(status="In Progress").count(),
        "completed_requests": MaintenanceRequest.objects.filter(status="Completed").count(),
        "critical_requests": MaintenanceRequest.objects.filter(priority="Critical").count(),

        # Machines
        "total_machines": Machine.objects.count(),
        "running_machines": Machine.objects.filter(status="Running").count(),
        "breakdown_machines": Machine.objects.filter(status="Breakdown").count(),
        "maintenance_machines": Machine.objects.filter(status="Maintenance").count(),

        # Recent Requests
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
from .models import Machine


def machine_list(request):

    search = request.GET.get("search", "")
    status = request.GET.get("status", "")

    machines = Machine.objects.all()

    if search:
        machines = machines.filter(
            Q(machine_code__icontains=search) |
            Q(machine_name__icontains=search) |
            Q(manufacturer__icontains=search)
        )

    if status:
        machines = machines.filter(status=status)

    context = {
        "machines": machines.order_by("machine_code"),
        "search": search,
        "status": status,
        "status_choices": Machine.STATUS_CHOICES,

        "total": Machine.objects.count(),
        "running": Machine.objects.filter(status="Running").count(),
        "breakdown": Machine.objects.filter(status="Breakdown").count(),
        "maintenance": Machine.objects.filter(status="Maintenance").count(),
    }

    return render(
        request,
        "maintenance/machine_list.html",
        context,
    )

def engineer_list(request):

    search = request.GET.get("search", "")
    status = request.GET.get("status", "")

    engineers = Engineer.objects.all()

    if search:
        engineers = engineers.filter(
            Q(engineer_code__icontains=search) |
            Q(engineer_name__icontains=search)
        )

    if status:
        engineers = engineers.filter(status=status)

    context = {

        "engineers": engineers.order_by("engineer_code"),

        "search": search,
        "status": status,

        "status_choices": Engineer.STATUS_CHOICES,

        "total": Engineer.objects.count(),
        "active": Engineer.objects.filter(status="Active").count(),
        "inactive": Engineer.objects.filter(status="Inactive").count(),
    }

    return render(
        request,
        "maintenance/engineer_list.html",
        context,
    )