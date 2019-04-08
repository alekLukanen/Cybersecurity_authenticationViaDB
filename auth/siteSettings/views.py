from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from siteSettings.models import SiteSettings
from siteSettings.serializers import SiteSettingsSerializer

# Create your views here.
class SiteSettingsView(ModelViewSet):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        TokenHasReadWriteScope, 
    ]

