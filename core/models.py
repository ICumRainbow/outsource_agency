from datetime import datetime

from django.db import models


class BaseModel(models.Model):
    """
    Base abstract Model for all other models to inherit, includes created_at field.
    """
    created_at = models.DateTimeField(verbose_name='Created at', default=datetime.now)

    class Meta:
        abstract = True
