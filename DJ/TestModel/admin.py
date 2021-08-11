from django.contrib import admin
from TestModel.models import Test, Contact, Tag


class TagInline(admin.TabularInline):
    model = Tag


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
