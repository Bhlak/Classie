from django.contrib import admin
from django.urls import path, include
from signup.views import RegisterAPIView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('signup.urls')),
    path('signin/', include('signin.urls')),
    path('lecturersignup/', RegisterAPIView.as_view(), name='lecturersignup')
]
