from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class SiteSettings(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    parameter = models.TextField(max_length=500, blank=True)
    value = models.TextField(max_length=200, blank=True)
    lastName = models.TextField(max_length=200, blank=True)

    class Meta:
        ordering = ('created', )
