from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('login/', views.StudentLogin.as_view()),
    path('logout/', views.Logout.as_view()),
    path('testing/', views.Tester.as_view())
]