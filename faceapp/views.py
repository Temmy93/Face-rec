from django.shortcuts import render, redirect
from django.db import models
from django.contrib.auth import login, authenticate, logout
from django.contrib import auth
from django.contrib import messages
from django import forms
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, UserManager

from faceapp.forms import StudentRegistrationForm, StudentLoginForm, AdminRegistrationForm, AdminLoginForm, CourseForm, StudentImageUpload, AdminImageUpload, CheckStudentMatric
from faceapp.models import Admin, Student, Course


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
    form = StudentImageUpload(instance=request.user)
    if request.method == "POST":
        form = StudentImageUpload(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('student_profile')
    return render(request, 'student_profile.html', {"form": form})


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
    if not request.user.is_authenticated or not isinstance(request.user, Admin):
        return redirect("admin_login")
    form = AdminImageUpload(instance=request.user)
    if request.method == "POST":
        form = AdminImageUpload(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('admin_profile')
    return render(request, 'admin_profile.html', {"form": form})
    

    #print(request.user.is_authenticated, request.user)
    #if not request.user.is_authenticated or not isinstance(request.user, Admin):
     #   return redirect("admin_login")
    #return render(request, 'admin_profile.html')


def admin_portal(request):
    if request.user.is_authenticated and isinstance(request.user, Admin):
        return redirect("admin_profile")
    return render(request, 'admin_portal.html')


# supposed to check student's authenticity from admin end by 
# displayiong student profile  and course details on admin's page
#
def check_student(request):
    if request.method == "POST":
        form = CheckStudentMatric(request.POST)
        if form.is_valid():
            matric_number = form.cleaned_data['matric_number']
            print(matric_number)
            return render (request.Student.objects.get(matric_number = matric_number))
    form = CheckStudentMatric()
    return render(request, 'admin_profile.html', {'form': form})


#Student"s course registration

def course_portal(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course_title =form.cleaned_data['course_title']
            course_code =form.cleaned_data['course_code']
            form.save()
            print(course_title, course_code)
             

    form = CourseForm()
    return render(request, 'coursereg.html', {'form': form})



#students = Student.objects.all()
#for student in students:
    #print(student.course_set.all())
    #print(students)
    