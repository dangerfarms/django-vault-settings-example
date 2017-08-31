from django.contrib import admin

from django_vault.forms import RedisForm


class VaultAdmin(admin.ModelAdmin):
    form = RedisForm
