from django.contrib import admin

from local_django_vault.django_vault.forms import RedisForm


class VaultAdmin(admin.ModelAdmin):
    form = RedisForm
