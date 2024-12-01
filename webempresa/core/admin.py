from typing import Any
from django.contrib import admin

# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj= None):
        if request.user.groups.filter(name="Personal").exists():
            return ('key', 'name')
        else:
            return ()