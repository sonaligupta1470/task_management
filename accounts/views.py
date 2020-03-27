from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def register_view(request):
    template_name = "accounts/register.html"
    context = {"form": None}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have registered successfully. Please Log in.")
        else:
            messages.warning(request, "Please try later")
        return redirect("login_url")
    else:
        form = UserCreationForm()
        context["form"] = form
    return render(request, template_name, context)


def login_view(request):
    template_name = "accounts/login.html"
    context = {}
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in successfully !")
            return redirect("home")
        else:
            messages.warning(request, "Invalid credentials. Please try again!")
            return render(request, template_name, context=context)
    return render(request, template_name, context=context)


def logout_view(request):
    if request.user:
        logout(request)
        messages.success(request, "You are logged out !")
    return redirect("home")
