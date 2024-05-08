from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('student/', views.SignUpView.as_view()),
    path('lecturer/', views.LecturerView.as_view())
]