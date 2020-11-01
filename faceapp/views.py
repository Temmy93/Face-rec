#import packages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
import cv2
import face_recognition
import numpy as np
import os

from faceapp.forms import (
    StudentRegistrationForm, StudentLoginForm, AdminRegistrationForm,
    AdminLoginForm, CourseForm, StudentImageUpload, AdminImageUpload, CheckStudentMatricForm,
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
    student = None
    if request.session.get("student"):
        student = Student.objects.get(matric_number=request.session.get("student"))
    form = CheckStudentMatricForm()
    if request.method == "POST":
        student = None
        form = CheckStudentMatricForm(request.POST)
        if form.is_valid():
            matric_number = form.cleaned_data.get('matric_number')
            print("matric_number")
            request.session["student"] = matric_number
            return redirect("check_student")
    return render(request, 'verify.html', {'form': form, 'student': student})


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


def authenticate(request):
    return render(request, 'verify.html')

#students = Student.objects.all()
# for student in students:
    # print(student.course_set.all())
    # print(students)


def verify(request):
    path = 'media/student_faces'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)

    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()

        #scale_percent= 50
        #width = int(img.shape[1] * scale_percent/100)
        #height = int(img.shape[0] * scale_percent/100)
        #dsize =(width, height)
        #imgS =cv2.resize(img, dsize)

        #img = cv2.rectangle (img, (x,y), (x+w, y+h), (0,255,0), 3)
        #imgS = cv2.resize(img, (int (img.shape[1]), int(img.shape[0]/2)))
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name(x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow('Webcam', img)
        cv2.waitKey(1000)
        # cv2.destroyAllWindows()

    # from admin end this is to enable the admin view the courses
    # registered by the student after the sy=tudent has been verified

    def displayRegisteredCourses(request, img):

        return render(request, 'verify.html')
