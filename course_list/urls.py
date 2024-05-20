from django.urls import path
from .views import ClistAPIView

urlpatterns = [
    path('courses/', ClistAPIView.as_view(), name ='course_list'),
]
