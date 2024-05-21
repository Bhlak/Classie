from django.contrib import admin
from .models import Student
# from .models import Lecturer
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "matric_no", "level", "department"]

# Register your models here.
# @admin.register(Lecturer)
# class lectureradmin(admin.ModelAdmin):
#     list_display = ["full_name", "title", "email","lecID", "passwordd"]

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "full_name", "is_staff", "is_active"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active"
            )}
        ),
    )

    search_fields = ("email",)
    ordering = ("email",)
admin.site.register(CustomUser, CustomUserAdmin)