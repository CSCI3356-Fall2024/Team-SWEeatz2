from django.contrib import admin
from .models import Campaign

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'created_at', 'points')
    search_fields = ('title',)
    list_filter = ('start_date', 'end_date')