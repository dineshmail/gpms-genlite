from django.urls import path
from .views import create_issue
from django.urls import include, path

urlpatterns = [
    path(
        "create/",
        create_issue,
        name="create_issue",
    ),
    
    path(
    "issues/",
    include("production.urls")
),
]