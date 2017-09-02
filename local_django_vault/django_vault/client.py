import os

import hvac

# options = {
#     'path': '/tmp/vault.log',
# }
# client.enable_audit_backend('file', options=options, name='somefile')


class VaultSecretsClient(object):
    """Client that overrides instance get/set/delete builtins to provide a familiar interface for accessing
    secrets, allowing local values to be swapped out in development.

    Any fields and methods declared on the instance are accessible as usual, and any other value accessed
    will interface with vault directly.

    Usage:

    >>> secrets = VaultSecretsClient('secrets')
    >>> secrets.all
    >>> secrets.DJANGO_SECRET_KEY = 'secret'
    >>> secrets.DJANGO_SECRET_KEY
    'secret'
    >>> secrets.all
    ['DJANGO_SECRET_KEY']
    >>> del secrets.DJANGO_SECRET_KEY
    >>> secrets.all

    """
    def __init__(self, namespace, hostname='vault', token=None):
        self.__dict__['namespace'] = namespace
        self.__dict__['client'] = hvac.Client(url='http://{}:8200'.format(hostname), token=token)

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]

        key = '{}/{}'.format(self.namespace, item)
        return self.client.read(key)['data']['value']

    def __setattr__(self, key, value):
        if key in self.__dict__:
            self.__dict__[key] = value
            return

        key = '{}/{}'.format(self.namespace, key)
        return self.client.write(key, value=value)

    def __delattr__(self, item):
        if item in self.__dict__:
            return

        key = '{}/{}'.format(self.namespace, item)
        return self.client.delete(key)

    @property
    def keys(self):
        resp = self.client.list(self.namespace)
        if resp:
            return resp['data']['keys']

    @property
    def values(self):
        data = {}
        for key in self.keys:
            data[key] = getattr(self, key)
        return data
