# main/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/student/', views.register_student, name='register_student'),
    path('register/tutor/', views.register_tutor, name='register_tutor'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('tutor/dashboard/', views.tutor_dashboard, name='tutor_dashboard'),
    path('hire/<int:tutor_id>/', views.hire_tutor, name='hire_tutor'),
    path('student/profile/', views.update_student_profile, name='update_student_profile'),
    path('tutor/profile/', views.update_tutor_profile, name='update_tutor_profile'),
]
