from django.urls import path
from .views import ClistAPIView, CodeAPIView

urlpatterns = [
    
    path('courses/', ClistAPIView.as_view(), name ='course_list'),
    path('code/<str:course_code>/', CodeAPIView.as_view())
]
