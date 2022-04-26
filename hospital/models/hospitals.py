from django.db import models
from django.utils.translation import gettext_lazy as _
from utilities.models import AbstractBaseModel


def ContactDetailDefault():
    return {"email": None, "work_phone": None, "personal_phone": None, "website": None}


class Hospital(AbstractBaseModel):
    """Model Class for Hospital."""

    name = models.CharField(_("Name of Hospital"), max_length=128)
    address = models.CharField(_("Address of Hospital"), max_length=256)
    no_beds = models.IntegerField(_("Number of Beds"), null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Doctor(AbstractBaseModel):
    """Model Class for Doctor."""

    hospital = models.ForeignKey(
        to=Hospital,
        verbose_name=_("Hospital of Doctor"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="doctors",
    )
    name = models.CharField(_("Name of Doctor"), max_length=128)
    education = models.JSONField(
        _("Educational Qualification of Doctor"), default=dict, null=True, blank=True
    )
    experience = models.JSONField(
        _("Work Experience of Doctor"), default=dict, null=True, blank=True
    )
    contact_details = models.JSONField(
        _("Contact Details of Doctor"),
        default=ContactDetailDefault,
        null=True,
        blank=True,
    )
    # Boolean if Doctor is Active in Hospital, cannot delete Doctor Model as Whole
    active = models.BooleanField(_("Is Active in this Hospital"), default=True)
    # While using postgress we can also use ArrayField for specializations
    specializations = models.JSONField(
        _("Specializations of Doctor"), default=dict, null=True, blank=True
    )

    def __str__(self):
        return f"{self.name} - {self.hospital}"
