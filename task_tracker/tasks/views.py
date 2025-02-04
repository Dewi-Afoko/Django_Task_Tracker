from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Task


# Create your views here.
def get_tasks(request):
    tasks = Task.objects.all()
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

def create_task(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        date_due = request.POST.get("date_due") or None

        Task.objects.create(name=name, description=description, date_due=date_due)

        return redirect("task-list")
    
    return render(request, "tasks/create_task.html")

@require_POST
def delete_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)
    task.delete()

    return redirect("task-list")