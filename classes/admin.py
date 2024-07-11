from django.contrib import admin
from .models import Classes

@admin.register(Classes)
class ClassAdmin(admin.ModelAdmin):
    model = Classes
    list_display = ('code', 'display_courses')
    search_fields = ('code', )


    def display_courses(self, obj):
        return ", ".join(course.course_title for course in obj.courses.all())