from django.urls import path
from .views import ClistAPIView, LecturerCourseAPIView, LecturerSupplementAPIView

urlpatterns = [
    path('course_list/', ClistAPIView.as_view(), name ='course_list'),
    path('lecturerset/', LecturerCourseAPIView.as_view()),
    path('courselist/', LecturerSupplementAPIView.as_view())
]
