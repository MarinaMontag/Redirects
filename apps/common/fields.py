from functools import partial

from django.db import models
from nanoid.resources import size

from apps.common.utils import generate_id_with_prefix


class IDField(models.CharField):
    def __init__(self, prefix: str, *args, db_collation=None, _size: int = size, **kwargs) -> None:
        self.prefix = prefix
        self._size = _size
        kwargs['default'] = partial(generate_id_with_prefix, prefix=prefix, _size=_size)
        kwargs['max_length'] = len(prefix) + _size + 1

        super().__init__(*args, db_collation, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['prefix'] = self.prefix
        kwargs['_size'] = self._size

        return name, path, args, kwargs
