from django.shortcuts import render, redirect
from django.db import models
from .models import Admin, Student
from django.contrib.auth import login, authenticate, logout
from django.contrib import auth
from django.contrib import messages
from .forms import StudentRegistrationForm, StudentLoginForm, AdminRegistrationForm, AdminLoginForm


def index(request):
    return render(request, 'index.html')

# Students Views


def student_signup(request):
    if request.user.is_authenticated and isinstance(request.user, Student):
        return redirect("student_profile")
    form = StudentRegistrationForm()
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            login(request, student,
                  backend="faceapp.backends.StudentAuthenticationBackend")
            return redirect('student_profile')
    return render(request, 'student_signup.html', {"form": form})


def student_login(request):
    if request.user.is_authenticated and isinstance(request.user, Student):
        return redirect("student_profile")
    form = StudentLoginForm()
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            student = form.save()
            login(request, student,
                  backend="faceapp.backends.StudentAuthenticationBackend")
            return redirect("student_profile")
    return render(request, 'student_login.html', {"form": form})


def student_profile(request):
    if not request.user.is_authenticated or not isinstance(request.user, Student):
        return redirect("student_login")
    return render(request, 'student_profile.html')


def student_portal(request):
    if request.user.is_authenticated and isinstance(request.user, Student):
        return redirect("student_profile")
    return render(request, 'student_portal.html')


def logout_all(request):
    logout(request)
    return redirect("index")


# Admin Views
def admin_signup(request):
    if request.user.is_authenticated and isinstance(request.user, Admin):
        return redirect("admin_profile")
    form = AdminRegistrationForm()
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            admin = form.save()
            login(request, admin,
                  backend="faceapp.backends.AdminAuthenticationBackend")
            return redirect('admin_profile')
    return render(request, 'admin_signup.html', {"form": form})


def admin_login(request):
    if request.user.is_authenticated and isinstance(request.user, Admin):
        return redirect("admin_profile")
    form = AdminLoginForm()
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            admin = form.save()
            login(request, admin,
                  backend="faceapp.backends.AdminAuthenticationBackend")
            return redirect("admin_profile")
    return render(request, 'admin_login.html', {"form": form})


def admin_profile(request):
    print(request.user.is_authenticated, request.user)
    if not request.user.is_authenticated or not isinstance(request.user, Admin):
        return redirect("admin_login")
    return render(request, 'admin_profile.html')


def admin_portal(request):
    if request.user.is_authenticated and isinstance(request.user, Admin):
        return redirect("admin_profile")
    return render(request, 'admin_portal.html')
