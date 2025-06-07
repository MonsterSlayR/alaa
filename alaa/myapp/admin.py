
from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_preview', 'active', 'order')
    list_editable = ('active', 'order')
    list_filter = ('active',)
    prepopulated_fields = {'modal_id': ('title',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'icon', 'modal_id', 'active', 'order')
        }),
        ('Modal Content', {
            'fields': ('modal_title', 'modal_description', 'title_top' ,'modal_features', 'title_left',
                      'modal_pricing_left','title_right' ,'modal_pricing_right','url')
        }),
    )

admin.site.register(Service, ServiceAdmin)