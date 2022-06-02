from django.db import models
from django.contrib.auth.models import User

import datetime


class Tag(models.Model):
    title = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title


class TaskFolder(models.Model):
    title = models.CharField(max_length=300)
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    deadline = models.DateTimeField(default=datetime.datetime.today)
    finished = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    folder = models.ForeignKey(TaskFolder, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return self.title
