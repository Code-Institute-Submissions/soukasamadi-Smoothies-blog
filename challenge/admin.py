from django.contrib import admin
from .models import Challenge


@admin.register(Challenge)
class BookAdmin(admin.ModelAdmin):
    """
    Add fields for Challenge in admin panel
    """
    list_display = ('name', 'goal', 'timestamp', 'approved')
    list_filter = ('approved', 'timestamp')
    actions = ['approve_challenge']

    def approve_challenge(self, request, queryset):
        queryset.update(approved=True)