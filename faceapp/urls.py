from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('admin/portal', views.admin_portal, name = 'admin_portal'),
    path('admin/signup', views.admin_signup, name = 'admin_signup' ),
    path('admin/login', views.admin_login, name = 'admin_login'),
    path('admin/profile', views.admin_profile, name = 'admin_profile'),
    path('students/portal', views.student_portal, name = 'student_portal'),
    path('students/signup', views.student_signup, name = 'student_signup'),
    path('students/login', views.student_login, name = 'student_login'),
    path('students/logout', views.student_logout, name = 'student_logout'),
    path('students/profile', views.student_profile, name = 'student_profile'),
]
