from django.core.exceptions import FieldError, ImproperlyConfigured
from django.db import models
from demo.cipher_field.cipher import Cipher
from django.utils.functional import cached_property

__all__ = [
    'CipherField',
    'CipherCharField',
    'CipherTextField',
]


class CipherField(models.Field):
    description = 'Encrypt your field'
    _internal_type = 'CipherField'

    def __init__(self, token=None, *args, **kwargs):

        if kwargs.get('primary_key'):
            raise ImproperlyConfigured(
                "%s does not support primary_key=True."
                % self.__class__.__name__
            )
        if kwargs.get('unique'):
            raise ImproperlyConfigured(
                "%s does not support unique=True."
                % self.__class__.__name__
            )
        if kwargs.get('db_index'):
            raise ImproperlyConfigured(
                "%s does not support db_index=True."
                % self.__class__.__name__
            )

        if not token:
            self.cipher = None
            self.token = token
        else:
            self.cipher = Cipher(token)
            self.token = token
        super(CipherField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return self._internal_type

    @cached_property
    def validators(self):
        self.__dict__['_internal_type'] = super(
            CipherField, self
        ).get_internal_type()
        try:
            return super(CipherField, self).validators
        finally:
            del self.__dict__['_internal_type']

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['token'] = self.token
        return name, path, args, kwargs

    def get_db_prep_value(self, value, connection, prepared=False):
        if self.token is None:
            return value
        return self.cipher.encrypt(value)

    def from_db_value(self, value, expression, connection):
        if self.token is None:
            return value
        return self.cipher.decrypt(value)

    def db_type(self, connection):
        return 'text'


def get_prep_lookup(self):
    raise FieldError("{} '{}' does not support lookups".format(
        self.lhs.field.__class__.__name__, self.lookup_name))


for name, lookup in models.Field.class_lookups.items():
    if name != 'isnull':
        lookup_class = type('CipherField' + name, (lookup,), {
            'get_prep_lookup': get_prep_lookup
        })
        CipherField.register_lookup(lookup_class)


class CipherCharField(CipherField, models.CharField):
    pass

    def db_type(self, connection):
        return 'char'

class CipherTextField(CipherField, models.TextField):
    pass

    def db_type(self, connection):
        return 'text'
