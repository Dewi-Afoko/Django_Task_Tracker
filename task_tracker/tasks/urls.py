from django.urls import path
from .views import get_tasks, mark_complete, mark_incomplete, create_task, delete_task, create_user

urlpatterns = [
    path("", get_tasks, name="task-list"),  # URL for the task list
    path("mark_complete/<int:task_id>/", mark_complete, name="mark-complete" ),
    path("mark_incomplete/<int:task_id>/", mark_incomplete, name="mark-incomplete" ),
    path("delete_task/<int:task_id>/", delete_task, name="delete-task" ),
    path("create_task/", create_task, name="create-task"),
    path("register/", create_user, name="register"),
]
