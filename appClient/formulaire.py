from django.contrib import admin

from django.forms import ModelForm
from .models import Client


class ClientAdminForm(ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'email']