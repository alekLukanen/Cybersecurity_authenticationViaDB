from django.contrib import admin
from users.models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'firstName', 'lastName', )
    search_fields = ('id', 'firstName', 'lastName', )


admin.site.register(Profile, ProfileAdmin)
