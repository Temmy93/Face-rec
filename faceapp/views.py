from django.shortcuts import render, redirect
from django.db import models
from .models import Admin, Student
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import StudentRegistrationForm, StudentLoginForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def admin_portal(request):
    return render(request, 'admin_portal.html')

def admin_signup(request):
    return render(request, 'admin_signup.html')

def admin_profile(request):
    return render(request, 'admin_profile.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        new = authenticate(username=username, password=password)
        if new is not None:
            auth.login(request, new)
            return render(request, "admin_profile.html")
        else:
            messages.info(request, 'Invalid Login Details, Please Sign Up')
            return redirect ('admin_login')
    else:
        return render(request, 'admin_login.html')


def rdmin_signup(request):

    if request.method == "POST":
       Firstname = request.POST["F_name"]
       Surname  = request.POST['S_name']
       username = request.POST['username']
       Staffnumber = request.POST['staff_number']
       Dept = request.POST['dept']
       email= request.POST['email']
       Phone = request.POST['phone']
       Password1 = request.POST['password1']
       Password2 = request.POST['password2']


       objects = models.Manager()


       new = Admin.objects.create(username = username, password = Password1, email = email, F_name = Firstname, S_name = Surname,)
       new.save();
       return render(request,'admin_login.html')


# Students Views
def student_signup (request):
    if request.user.is_authenticated and isinstance(request.user, Student):
        return redirect("student_profile")
    form = StudentRegistrationForm()
    if request.method =='POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_profile')
    return render(request, 'student_signup.html', {"form":form})


def student_login(request):
    if request.user.is_authenticated and isinstance(request.user, Student):
        return redirect("student_profile")
    form = StudentLoginForm()
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            student = form.save()
            login(request, student)
            return redirect("student_profile")
    return render(request, 'student_login.html', {"form":form})


def student_profile(request):
    if not request.user.is_authenticated or not isinstance(request.user, Student):
        return redirect("student_login")
    return render(request, 'student_profile.html')


def student_portal(request):
    if request.user.is_authenticated and isinstance(request.user, Student):
        return redirect("student_profile")
    return render(request, 'student_portal.html')

def student_logout(request):
    logout(request)
    return redirect("student_login")
