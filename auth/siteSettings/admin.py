from django.contrib import admin
from siteSettings.models import SiteSettings


# Register your models here.
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'parameter', 'value', 'optional_extra',)
    search_fields = ('id', 'parameter', )


admin.site.register(SiteSettings, SiteSettingsAdmin)
