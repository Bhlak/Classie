from django.contrib import admin
from .models import Assignment, Submission

@admin.register(Assignment)
class AsignmentAdmin(admin.ModelAdmin):
    model = Assignment
    list_display = ('question', 'deadline')
    search_fields = ('question', )

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    model = Submission
    list_display = ('id', 'text', 'matric_no', 'assignment')
    search_fields = ('matric_no', )