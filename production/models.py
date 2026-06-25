from django.db import models
#nothing

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Issue(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]

    issue_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Open'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.issue_id:
            last_issue = Issue.objects.order_by("-id").first()

            if last_issue:
                last_id = int(last_issue.issue_id.replace("ISS", ""))
                new_id = last_id + 1
            else:
                new_id = 1

            self.issue_id = f"ISS{new_id:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.issue_id} - {self.title}"



class ProductionUpdate(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    update_date = models.DateField()

    activity = models.CharField(max_length=200)

    quantity = models.PositiveIntegerField(default=0)

    remarks = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.department} - {self.activity}"



class AssetStock(models.Model):
    asset_name = models.CharField(max_length=200)

    quantity = models.PositiveIntegerField(default=0)

    remarks = models.TextField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.asset_name} ({self.quantity})"