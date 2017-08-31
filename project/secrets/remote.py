from django_vault.client import VaultSecretsClient


secrets = VaultSecretsClient('secret/wc-api')
