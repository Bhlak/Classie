from django.contrib import admin
from django.urls import path
from . import views
from rest_framework import routers
from signup.views import RegisterAPIView 

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('studentsignup/', views.SignUpView.as_view()),
    path('lecturersignup/', RegisterAPIView.as_view(), name='lecturersignup')
]