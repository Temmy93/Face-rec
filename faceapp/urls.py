from django.urls import path

from . import views
from .views import course_portal

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/portal', views.admin_portal, name='admin_portal'),
    path('admin/signup', views.admin_signup, name='admin_signup'),
    path('admin/login', views.admin_login, name='admin_login'),
    path('admin/profile', views.admin_profile, name='admin_profile'),
    path('admin/authenticate', views.authenticate, name = 'authentication_portal'),
    path('admin/verify', views.verify, name='verify'),
    path('students/portal', views.student_portal, name='student_portal'),
    path('students/signup', views.student_signup, name='student_signup'),
    path('students/login', views.student_login, name='student_login'),
    path('logout', views.logout_all, name='logout'),
    path('students/profile', views.student_profile, name='student_profile'),
    path('admin/check_student', views.check_student, name = 'check_student'),
    path('students/course_portal', views.course_portal, name = 'course_portal'),
]
