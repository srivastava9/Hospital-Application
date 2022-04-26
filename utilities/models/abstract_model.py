import uuid
from django.db import models


def get_str_uuid():
    """Get Str UUID"""
    return uuid.uuid4().hex


class PrimarykeyField(models.CharField):
    """Override PrimaryKeyField."""

    def __init__(self, **kwargs):
        """Init method."""
        kwargs["help_text"] = "Primary Key Field for Object"
        kwargs["primary_key"] = True
        kwargs["editable"] = False
        kwargs["default"] = get_str_uuid
        kwargs["max_length"] = 48
        super().__init__(**kwargs)


class AbstractBaseModel(models.Model):
    """Abstract Model."""

    id = PrimarykeyField()
    created_at = models.DateTimeField(verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated At", auto_now=True)
    metadata = models.JSONField(default=dict, blank=True)

    class Meta:
        """Meta Class."""

        abstract = True
