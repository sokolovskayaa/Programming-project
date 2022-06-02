from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_tasks, name="all_tasks"),
    path("<int:task_folder>", views.folder_tasks, name="tasks_by_folder"),
    path("task-folders/", views.all_folders, name="task_folders"),
    path("delete-task-folder/<int:task_folder_id>/", views.delete_folder_task, name="delete_folder_task"),

    path("change-task-finished/<int:task_id>/", views.change_task_finished, name="change_task_finished"),
    path("delete-task/<int:task_id>/", views.delete_task, name="delete_task"),

    path("tags/", views.all_tags, name="all_tags"),
    path("delete-tag/<int:tag_id>/", views.delete_tag, name="delete_tag"),
]
