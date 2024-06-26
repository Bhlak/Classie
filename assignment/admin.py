from django.contrib import admin
from .models import Assignment

@admin.register(Assignment)
class AsignmentAdmin(admin.ModelAdmin):
    model = Assignment
    list_display = ('question', 'deadline')
    search_fields = ('question', )