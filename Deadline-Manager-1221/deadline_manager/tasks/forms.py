from django.forms import ModelForm
from .models import Tag, Task, TaskFolder


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['title']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "text",
            "deadline",
            "folder",
            "tags",
        ]


class TaskFolderForm(ModelForm):
    class Meta:
        model = TaskFolder
        fields = [
            "title",
            "tags"
        ]