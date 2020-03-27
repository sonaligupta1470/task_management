from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TaskModelForm, CommentForm
from .models import Task, Comment
from django.contrib.auth.models import User


def list_view(request):
    template_name = "task/list_task.html"
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, template_name, context)


def detail_view(request, task_id):
    template_name = "task/task_detail.html"
    obj = get_object_or_404(Task, id=task_id)
    context = {"object": obj}
    context["users"] = User.objects.all()
    context["status_choices"] = Task._meta.get_field("status").choices
    obj.editable = False
    if request.user == obj.task_creator:
        obj.editable = True
    obj.status_edit = False
    if request.user in obj.assigned_to.all():
        obj.status_edit = True
    comment_obj = Comment.objects.filter(task=obj)
    for comment in comment_obj:
        comment.editable = False
        if request.user == comment.creator:
            comment.editable = True
    context["comments"] = comment_obj
    return render(request, template_name, context)


@login_required
def create_view(request):
    template_name = "task/create_task.html"
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_creator = request.user
            task.save()
            form.save_m2m()
            messages.success(request, f"{task.task_name} is successfully created.")
            return redirect("/task/")
    form = TaskModelForm(None)
    context = {"form": form}
    return render(request, template_name, context)


@login_required
def edit_view(request, task_id):
    template_name = "task/task_detail.html"
    context = {}
    obj = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        print(request.POST)
    return render(request, template_name, context)


@login_required
def delete_view(request, task_id):
    template_name = ""
    context = {}
    return render(request, template_name, context)


@login_required
def comment_add_view(request, task_id, user_id):
    template_name = "task/task_detail.html"
    context = {}
    obj = get_object_or_404(Task, id=task_id)
    context["object"] = obj
    comment_obj = Comment.objects.filter(task=obj)
    print("comment obj >>> ", comment_obj)
    context["comments"] = comment_obj
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data["comment"]
            if comment:
                user_obj = get_object_or_404(User, id=user_id)
                p = Comment(comment=comment, task=obj, creator=user_obj)
                p.save()
    else:
        form = CommentForm()
        context["form"] = form
    return render(request, template_name, context)


@login_required
def comment_edit_view(request, task_id, user_id, comment_id):
    template_name = "task/task_detail.html"
    context = {}
    return render(request, template_name, context)


@login_required
def comment_delete_view(request, task_id, user_id, comment_id):
    template_name = "task/task_detail.html"
    context = {}
    return render(request, template_name, context)
