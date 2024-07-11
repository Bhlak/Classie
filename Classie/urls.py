from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('signup.urls')),
    path('auth/', include('signin.urls')),
    path('classes/', include('classes.urls')),
    path('announcements/', include('announcements.urls'))
    path('courses/', include('courses.urls')),
    path('assignments/', include('assignment.urls'))
]