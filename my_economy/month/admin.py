from django.contrib import admin
from .models import Month

@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    # display_list = []
    filter_list = ['year']
    search_fields = ['month', 'year']
