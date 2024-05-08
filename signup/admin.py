from django.contrib import admin
from .models import Lecturer

# Register your models here.
@admin.register(Lecturer)
class lectureradmin(admin.ModelAdmin):
    list_display = ["full_name", "title", "email","lecID", "passwordd"]