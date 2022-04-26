from django.db import models
from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import timedelta
from constants import ERR_MSG_APPOINTMENT_DATE, ERR_MSG_DOCTOR_APPOINTMENT_ALREADY_SET

from hospital.models.patient import Patient
from .hospitals import ContactDetailDefault, Doctor, Hospital
from utilities.models import AbstractBaseModel


class Appointment(AbstractBaseModel):
    """Model Class for Appointment between Patient and Doctors."""

    # Foreign Keys
    # In on_delete restrict is used to prevent data loss if a doctor or patient models is deleted

    doctor = models.ForeignKey(
        to=Doctor,
        verbose_name=_("Doctor for Appointment"),
        on_delete=models.RESTRICT,
        related_name="appointments",
    )
    patient = models.ForeignKey(
        to=Patient,
        verbose_name=_("Patient for Appointment"),
        on_delete=models.RESTRICT,
        related_name="appointments",
    )

    # Datetime field
    appointment_on = models.DateTimeField(_("Appointed Date and Time"))

    # Data related to appointment
    purpose_of_visit = models.TextField(
        _("Purpose of Appointment"), null=True, blank=True
    )
    doctor_remark = models.TextField(
        _("Remark of Doctor after Appointment"), null=True, blank=True
    )
    medication_remark = models.TextField(
        _("Medicines Suggested after Appointment"), null=True, blank=True
    )
    test_remark = models.TextField(
        _("Test Suggested after Appointment"), null=True, blank=True
    )

    def save(self, *args, **kwargs):
        """Applies some check before registering an Appointment."""
        if self.appointment_on >= timezone.now():
            # Checks whether doctor appointment is already there in set timezone,
            # for simplicity we are taking 30 minutes before and after any previous appointment as buffer
            if Appointment.objects.filter(
                doctor=self.doctor,
                appointment_on__range=(
                    self.appointment_on - timedelta(minutes=30),
                    self.appointment_on + timedelta(minutes=30),
                ),
            ).exists:
                raise ValidationError(ERR_MSG_DOCTOR_APPOINTMENT_ALREADY_SET)
            return super().save(*args, **kwargs)
        raise ValidationError(ERR_MSG_APPOINTMENT_DATE)
