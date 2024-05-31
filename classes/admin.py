from django.contrib import admin
from .models import Classes

@admin.register(Classes)
class ClistAdmin(admin.ModelAdmin):
    list_display = ('code',)
    # , 'courses'
    search_fields = ('code', )

    # def courses(self):
    #     return ', '.join()
