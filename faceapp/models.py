from pathlib import Path
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, UserManager


def get_student_upload_path(instance, filename):
    ext = Path(filename).suffix
    return f'student_faces/{instance.matric_number} {instance.surname} {instance.firstname}{ext}'


def get_admin_upload_path(instance, filename):
    ext = Path(filename).suffix
    return f'admin_faces/{instance.staff_number} {instance. surname} {instance. firstname}{ext}'


class Course(models.Model):

    code = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=100, null=True)

    # student.course._set.all
    def __str__(self):
        return f"{self.code}"


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
    matric_number = models.CharField(max_length=100, unique=True, null=True)
    department = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=11)
    img = models.ImageField(upload_to=get_student_upload_path)
    courses_registered = models.ManyToManyField(Course)

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
