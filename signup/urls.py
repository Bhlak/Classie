from django.urls import path
from .views import RegisterAPIView

urlpatterns = [
    path('lecturersignup/', RegisterAPIView.as_view(), name='lecturersignup'),]