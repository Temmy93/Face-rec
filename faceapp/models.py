from pathlib import Path
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, UserManager


def get_student_upload_path(instance, filename):
    ext = Path(filename).suffix
    return f'student_faces/{instance.matric_number}{ext}'


def get_admin_upload_path(instance, filename):
    ext = Path(filename).suffix
    return f'admin_faces/{instance.staff_number}{ext}'


class Admin(AbstractBaseUser):

    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    staff_number = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=11)
    img = models.ImageField(upload_to=get_admin_upload_path)

    USERNAME_FIELD = "staff_number"
    objects = UserManager()

    def get_full_name(self):
        return f"{self.surname} {self.firstname}"

    @property
    def is_staff(self):
        return False

    def has_module_perms(self, *args, **kwargs):
        return False

    def get_img_url(self):
        if not self.img:
            return "/static/images/face1.jpg"
        return self.img.url


class Student(AbstractBaseUser):

    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    matric_number = models.CharField(max_length=100, unique=True, null = True)
    department = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=11)
    img = models.ImageField(upload_to=get_student_upload_path)

    USERNAME_FIELD = "matric_number"
    objects = UserManager()

    def get_full_name(self):
        return f"{self.surname} {self.firstname}"

    @property
    def is_staff(self):
        return False

    def has_module_perms(self, *args, **kwargs):
        return False

    def get_img_url(self):
        if not self.img:
            return "/static/images/face1.jpg"
        return self.img.url




class Course(models.Model):
    
    student_matric_number = models.ManyToManyField(Student)
    course_code = models.CharField(max_length= 15)
    course_title = models.CharField(max_length = 100, null = True)

#student.course._set.all
    def get_courses(self):
        return f"{self.student.course_set.all()}"