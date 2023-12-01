from django.contrib import admin

from .models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subtitle', 'picture', 'is_active']
    list_display_links = ['id']
    list_editable = ['title', 'subtitle', 'picture', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'subtitle']
