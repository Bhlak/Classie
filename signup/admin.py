from django.contrib import admin
from .models import Student
from .models import Lecturer

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "email", "password"]

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "email"]