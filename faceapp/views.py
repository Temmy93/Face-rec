from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from faceapp.forms import (
    StudentRegistrationForm, StudentLoginForm, AdminRegistrationForm,
    AdminLoginForm, CourseForm, StudentImageUpload, AdminImageUpload, CheckStudentMatric,
    CourseRegForm
)
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
    return render(request, 'student_profile.html', {"form": form, 'courses_registered': request.user.courses_registered.all()})


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
    # if not request.user.is_authenticated or not isinstance(request.user, Admin):
    #   return redirect("admin_login")
    # return render(request, 'admin_profile.html')


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
            return render(request.Student.objects.get(matric_number=matric_number))
    form = CheckStudentMatric()
    return render(request, 'admin_profile.html', {'form': form})


# Student"s course registration

def course_portal(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = CourseRegForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("student_profile")
    form = CourseRegForm(instance=request.user)
    return render(request, 'coursereg.html', {'form': form, 'courses': courses})


#students = Student.objects.all()
# for student in students:
    # print(student.course_set.all())
    # print(students)
