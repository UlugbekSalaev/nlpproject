from django.contrib import admin
from .models import APILog


@admin.register(APILog)
class APILogAdmin(admin.ModelAdmin):
    list_display = ('method', 'client_ip', 'timestamp')
    search_fields = ('method', 'request_text', 'client_ip')
    list_filter = ('method', 'timestamp')
    ordering = ('-timestamp',)
