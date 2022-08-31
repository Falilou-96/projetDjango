from django.db import models
from django.contrib import admin


class Client(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    phone = models.IntegerField(max_length=30)
    adresse = models.CharField(max_length=40)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'phone', 'adresse')
    list_filter = ('nom',)
    search_fields = ['nom', 'phone']
