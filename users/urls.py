from django.urls import path
from . import views

urlpatterns = [
    path("home", views.user_home, name="user_home"),
    path("", views.user_home, name="user_home"),
    path("mydiet", views.user_diet, name="user_diet"),
    path("profile", views.user_profile, name="user_profile"),
    path("teacher/home", views.teacher_home, name="teacher_home"),
    path("teacher/students", views.teachers_students, name="teachers_students"),
    path(
        "teacher/students/",
        views.teachers_students_info,
        name="teachers_students_info",
    ),
    path("teacher/profile", views.teacher_profile, name="teacher_profile"),
    path("student/message", views.message_view_student, name="message_view_student"),
    path("teacher/message", views.message_view_teacher, name="message_view_teacher"),
    path(
        "teacher/message/send", views.message_teacher_send, name="message_teacher_send"
    ),
]
