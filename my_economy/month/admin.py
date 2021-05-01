from django.contrib import admin
from .models import Month

@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    # list_display = []
    list_filter = ['year']
    search_fields = ['month', 'year']
