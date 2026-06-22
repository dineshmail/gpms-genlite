from django.contrib import admin
from .models import Department ,Issue ,ProductionUpdate , AssetStock

admin.site.register(Department)
admin.site.register(Issue)
admin.site.register(ProductionUpdate)
admin.site.register(AssetStock)