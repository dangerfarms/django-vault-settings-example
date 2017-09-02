from django_vault.client import VaultSecretsClient


VAULT_HOSTNAME = 'vault.vault'
VAULT_NAMESPACE = 'secret/wc-api'

secrets = VaultSecretsClient(VAULT_NAMESPACE, VAULT_HOSTNAME)
