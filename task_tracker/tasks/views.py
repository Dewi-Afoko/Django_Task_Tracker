from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib.auth.models import User


# Create your views here.
@login_required
def get_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "tasks/task_list.html", {'tasks': tasks} )

def mark_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.complete = True
    task.save()
    return redirect("task-list")

def mark_incomplete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.complete = False
    task.save()
    return redirect("task-list")

@login_required
def create_task(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        date_due = request.POST.get("date_due") or None

        Task.objects.create(user=request.user, name=name, description=description, date_due=date_due)

        return redirect("task-list")
    
    return render(request, "tasks/create_task.html")

@require_POST
def delete_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)
    task.delete()

    return redirect("task-list")


def create_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            User.objects.create_user(username=username, password=password)

            return redirect("login")
    
    return render(request, "registration/register.html")

    

