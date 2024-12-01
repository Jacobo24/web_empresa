from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'created', 'updated')
    ordering = ('-created',)
    search_fields = ('title', 'content')
    date_hierarchy = 'created'

admin.site.register(Service, ServiceAdmin)