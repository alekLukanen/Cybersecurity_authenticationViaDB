from rest_framework import serializers
from siteSettings.models import SiteSettings

class SiteSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteSettings
        fields = ("parameter", "value", "optional_extra", )
        
