from django.contrib import admin
from .models import Clist, Department
# Register your models here.
@admin.register(Clist)
class ClistAdmin(admin.ModelAdmin):
    list_display = ('year', 'course_title', 'course_code','faculty')
    search_fields = ('course_title', 'course_code')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','dep_code','faculty', 'display_courses')
    search_fields = ('name','faculty')
   
    def display_courses(self, obj):
        return ", ".join(course.course_title for course in obj.courses.all())
    display_courses.short_description = 'Courses'