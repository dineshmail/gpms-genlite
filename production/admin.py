from django.contrib import admin
from .models import Department, Issue, ProductionUpdate, AssetStock

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = (
"issue_id",
"title",
"department",
"priority",
"status",
"created_at",
)

list_filter = (
    "department",
    "priority",
    "status",
)

search_fields = (
    "issue_id",
    "title",
)
@admin.register(ProductionUpdate)
class ProductionUpdateAdmin(admin.ModelAdmin):
    list_display = (
"department",
"activity",
"quantity",
"update_date",
)
@admin.register(AssetStock)
class AssetStockAdmin(admin.ModelAdmin):
    list_display = (
"asset_name",
"quantity",
"updated_at",
)
