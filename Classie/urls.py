from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('signup.urls')),
    # path('login/', include('signin.urls'))
]
