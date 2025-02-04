from django.urls import path
from .views import get_tasks, mark_complete

urlpatterns = [
    path("", get_tasks, name="task-list"),  # URL for the task list
    path("mark_complete/<int:task_id>/", mark_complete, name="mark-complete" )
]
