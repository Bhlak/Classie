from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('signup.urls')),
    path('auth/', include('signin.urls')),
    path('course_list/', include('course_list.urls'))
]