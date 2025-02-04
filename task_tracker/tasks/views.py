from django.shortcuts import render, redirect, get_object_or_404
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