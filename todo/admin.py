from django.contrib import admin
from .models import TODO

# admin.site.register

@admin.register(TODO)
class TODOAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date')  # Fields visible in admin
    list_filter = ('user',)  # filters to make navigation easier