from django.db import models
from dashboard.models import Department

class Machine(models.Model):

    STATUS_CHOICES = [
        ("Running", "Running"),
        ("Breakdown", "Breakdown"),
        ("Maintenance", "Maintenance"),
    ]

    machine_code = models.CharField(
        max_length=20,
        unique=True,
    )

    machine_name = models.CharField(
        max_length=150,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    location = models.CharField(
        max_length=100,
    )

    manufacturer = models.CharField(
        max_length=100,
        blank=True,
    )

    model_number = models.CharField(
        max_length=100,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Running",
    )

    def __str__(self):
        return f"{self.machine_code} - {self.machine_name}"
    

class Engineer(models.Model):

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    engineer_code = models.CharField(
        max_length=20,
        unique=True,
    )

    engineer_name = models.CharField(
        max_length=100,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active",
    )

    def __str__(self):
        return f"{self.engineer_code} - {self.engineer_name}"
    
class SparePart(models.Model):

    CATEGORY_CHOICES = [
        ("Electrical", "Electrical"),
        ("Mechanical", "Mechanical"),
        ("Hydraulic", "Hydraulic"),
        ("Pneumatic", "Pneumatic"),
        ("Consumable", "Consumable"),
    ]

    part_code = models.CharField(
        max_length=20,
        unique=True,
    )

    part_name = models.CharField(
        max_length=150,
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
    )

    stock_quantity = models.PositiveIntegerField(
        default=0,
    )

    minimum_stock = models.PositiveIntegerField(
        default=5,
    )

    unit = models.CharField(
        max_length=20,
        default="Nos",
    )

    supplier = models.CharField(
        max_length=150,
        blank=True,
    )

    def __str__(self):
        return f"{self.part_code} - {self.part_name}"
    
    
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
    def save(self, *args, **kwargs):
     if not self.request_id:
         last_request = MaintenanceRequest.objects.order_by("-id").first()

         if last_request and last_request.request_id:
             last_number = int(last_request.request_id.replace("MNT", ""))
         else:
             last_number = 0

         self.request_id = f"MNT{last_number + 1:04d}"

     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.request_id} - {self.machine_name}"
