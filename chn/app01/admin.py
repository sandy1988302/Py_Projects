from django.contrib import admin
from app01.models import BaiduNews


class BaiduNewsAdmin(admin.ModelAdmin):
    list_display = ('category', 'news_rank', 'title')  # list
    search_fields = ('title',)
    fieldsets = (
        ['Main', {
            'fields': ('category', 'news_rank', 'title'),
        }],
        ['Advance', {
            'classes': ('link',),  # CSS
            'fields': ('crawling_time',),
        }]
    )


admin.site.register(BaiduNews, BaiduNewsAdmin)
