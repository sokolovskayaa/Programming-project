from django.shortcuts import  redirect, render
from django.http import HttpResponse, Http404
from django.db.models import Count
from django.contrib import messages
from django.urls import reverse

from .models import Task, TaskFolder, Tag
from .forms import TagForm, TaskForm, TaskFolderForm


def all_folders(request):
	if request.user.is_authenticated:
		if request.GET.get('tag'):
			task_folders = TaskFolder.objects.filter(user=request.user, tags__title__in=[request.GET.get('tag')]).annotate(number_of_tasks=Count('task'))
		else:
			task_folders = TaskFolder.objects.filter(user=request.user).annotate(number_of_tasks=Count('task'))
		
		if request.method == "POST":
			task_folder_form = TaskFolderForm(request.POST)
			if task_folder_form.is_valid():
				task_folder = task_folder_form.save(commit=False)
				task_folder.user = request.user
				task_folder.save()
				task_folder_form.save_m2m()
				return redirect("task_folders")

		task_folder_form = TaskFolderForm()
		return render(request=request, template_name="task_folders.html", context={"task_folders":task_folders, "form": task_folder_form})

	return redirect("login")


def folder_tasks(request, task_folder):
	if request.user.is_authenticated:
		task_folder = TaskFolder.objects.get(id=task_folder)
		if request.GET.get('tag'):
			tasks = Task.objects.filter(user=request.user, folder=task_folder, tags__title__in=[request.GET.get('tag')])
		else:
			tasks = Task.objects.filter(user=request.user, folder=task_folder)

		if request.method == "POST":
			task_form = TaskForm(request.POST)
			if task_form.is_valid():
				task = task_form.save(commit=False)			
				task.user = request.user
				task.save()
				task_form.save_m2m()
				return redirect(reverse("tasks_by_folder", kwargs={"task_folder": task_folder.id}))
			else:
				messages.error(request, "Unsuccessful(. Fill all fields correct!")

		task_form = TaskForm()

		return render(request=request, template_name="tasks.html", context={"tasks":tasks, "task_folder":task_folder, "form": task_form})

	return redirect("login")


def delete_folder_task(request, task_folder_id):
	task = TaskFolder.objects.get(id=task_folder_id)
	if task.user == request.user:
		task.delete()
		return HttpResponse(content="success")
	else:
		return Http404()


def all_tasks(request):
	if request.user.is_authenticated:
		tasks = Task.objects.filter(user=request.user)
		if request.GET.get('tag'):
			tasks = Task.objects.filter(user=request.user, tags__title__in=[request.GET.get('tag')])
		else:
			tasks = Task.objects.filter(user=request.user)

		if request.method == "POST":
			task_form = TaskForm(request.POST)
			if task_form.is_valid():
				task = task_form.save(commit=False)			
				task.user = request.user
				task.save()
				task_form.save_m2m()
				return redirect("all_tasks")
			else:
				messages.error(request, "Unsuccessful(. Fill all fields correct!")

		task_form = TaskForm()
		return render(request=request, template_name="tasks.html", context={"tasks":tasks, "form": task_form})

	return redirect("login")


def change_task_finished(request, task_id):
	task = Task.objects.get(id=task_id)
	if task.user == request.user:
		task.finished = not task.finished
		task.save()
		return HttpResponse(content="success")
	else:
		return Http404()


def delete_task(request, task_id):
	task = Task.objects.get(id=task_id)
	if task.user == request.user:
		task.delete()
		return HttpResponse(content="success")
	else:
		return Http404()


def all_tags(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			tag_form = TagForm(request.POST)
			if tag_form.is_valid():
				tag = tag_form.save(commit=False)
				tag.user = request.user
				tag.save()
				return redirect("all_tags")
		tags = Tag.objects.filter(user=request.user)
		tag_form = TagForm()
		return render(request=request, template_name="tags.html", context={"tags":tags, "form": tag_form})

	return redirect("login")


def delete_tag(request, tag_id):
	tag = Tag.objects.get(id=tag_id)
	if tag.user == request.user:
		tag.delete()
		return HttpResponse(content="success")
	else:
		return Http404()

