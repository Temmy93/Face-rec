from django.contrib import admin
from .models import Student, Admin, Course
# Register your models here.

admin.site.register(Student),
admin.site.register(Admin)