from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('create/', views.ClassAPI.as_view())
]