from django.contrib import admin
from .models import Student
from .models import Lecturer

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "email", "password"]

# Register your models here.
@admin.register(Lecturer)
class lectureradmin(admin.ModelAdmin):
    list_display = ["full_name", "title", "email","lecID", "passwordd"]