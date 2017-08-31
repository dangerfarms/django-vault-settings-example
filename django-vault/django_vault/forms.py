from django.forms import forms

from django_vault.client import VaultSecretsClient


class RedisForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RedisForm, self).__init__(*args, **kwargs)

        client = VaultSecretsClient('secrets')
        keys = client.all
        for key in keys:
            self.fields[key] = forms.CharField()
