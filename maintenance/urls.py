from django.urls import path
from . import views

urlpatterns =[
    path("", views.dashboard, name="maintenance_dashboard"),
    path("requests/", views.request_list, name="maintenance_request_list"),
    path("requests/new/", views.create_request, name="maintenance_request_create"),
    path("requests/<int:pk>/", views.request_detail, name="maintenance_request_detail"),
    path("requests/<int:pk>/edit/",views.edit_request,name="maintenance_request_edit",),
    path("requests/<int:pk>/delete/",views.delete_request,name="maintenance_request_delete",),
    path("machines/",views.machine_list,name="machine_list",),
    path("engineers/",views.engineer_list,name="engineer_list",),
]