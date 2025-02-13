import uuid
from django.db import models

from apps.redirects.constants import PREFIX_FOR_REDIRECT
from apps.common.fields import IDField
from apps.common.models import BaseModel


class RedirectRule(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    redirect_url = models.URLField()
    is_private = models.BooleanField(default=False)
    redirect_identifier = IDField(PREFIX_FOR_REDIRECT)

    def __str__(self):
        return self.redirect_identifier
