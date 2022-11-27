from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "GOCEJ's Library"

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'prn', 'branch']
    search_fields = ['name', 'prn', 'branch']
    list_filter = ['branch']



admin.site.register(Student, StudentAdmin)
admin.site.register(Entry)