from django.shortcuts import render, redirect
from .forms import IssueForm


def create_issue(request):

    if request.method == "POST":

        form = IssueForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = IssueForm()

    return render(
        request,
        "production/create_issue.html",
        {"form": form},
    )