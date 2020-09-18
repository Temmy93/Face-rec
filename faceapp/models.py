from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, UserManager


class Admin(AbstractBaseUser):

    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    staff_number = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=11)
    img = models.ImageField(upload_to='admin_faces')

    USERNAME_FIELD = "staff_number"
    objects = UserManager()

    def get_full_name(self):
        return f"{self.surname} {self.firstname}"


class Student(AbstractBaseUser):

    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    matric_number = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=11)
    img = models.ImageField(upload_to='student_faces')

    USERNAME_FIELD = "matric_number"
    objects = UserManager()

    def get_full_name(self):
        return f"{self.surname} {self.firstname}"
