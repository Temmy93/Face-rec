from django.contrib.auth.backends import BaseBackend
from django.db.models import Q
from faceapp.models import Student, Admin


class StudentAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, user_category=None):
        if username is None or password is None or user_category != "student":
            return
        try:
            student = Student.objects.filter(
                Q(email=username) | Q(matric_number=username)).first()
            if student is None:
                raise Student.DoesNotExist(
                    f"<Student {username}> Does not exist")
        except Student.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            return
        else:
            if student.check_password(password) and student.is_active:
                return student

    def get_user(self, user_id):
        try:
            return Student.objects.get(id=user_id)
        except Student.DoesNotExist:
            return None


class AdminAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, user_category=None):
        if username is None or password is None or user_category != "admin":
            return
        try:
            admin = Admin.objects.filter(
                Q(email=username) | Q(staff_number=username)).first()
            if admin is None:
                raise Admin.DoesNotExist(f"<Admin {username}> Does not exist")
        except Admin.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            return
        else:
            if admin.check_password(password) and admin.is_active:
                return admin

    def get_user(self, user_id):
        try:
            return Admin.objects.get(id=user_id)
        except Admin.DoesNotExist:
            return None
