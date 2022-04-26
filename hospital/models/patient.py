from django.db import models
from django.utils.translation import gettext_lazy as _
from .hospitals import Doctor, Hospital
from utilities.models import AbstractBaseModel


def PatientContactDetailDefaults():
    return {"email": None, "personal_phone": None}


def EmergencyContactDetailDefault():
    return {"name": None, "phone1": None, "phone2": None, "relation": None}


class SexChoice(models.TextChoices):
    """Choices for Sex."""

    MALE = "MALE", _("Male")
    FEMALE = "FEMALE", _("FEMALE")
    OTHERS = "OTHERS", _("OTHERS")


class Patient(AbstractBaseModel):
    """Model Class for Patients."""

    name = models.CharField(_("Name of Patient"), max_length=128)
    address = models.CharField(_("Address of Patient"), max_length=256)
    sex = models.CharField(
        choices=SexChoice.choices,
        verbose_name=_("Sex of Patient"),
        default=SexChoice.MALE,
        max_length=8,
    )
    contact_details = models.JSONField(
        _("Contact Details of Doctor"),
        default=PatientContactDetailDefaults,
        null=True,
        blank=True,
    )
    emergency_contact_details = models.JSONField(
        _("Emergency Contact Details of Patient"),
        default=EmergencyContactDetailDefault,
        null=True,
        blank=True,
    )
    # Foreign Keys.
    hospital = models.ForeignKey(
        to=Hospital,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Hospital Of Patient"),
    )

    # A Patient can have more than one doctor
    # but one main doctor can be there which primarly look after him/her
    # Other Doctors will be joined through appointments.
    main_doctor = models.ForeignKey(
        to=Doctor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Main Doctor of Patient"),
    )

    def __str__(self):
        return "{self.name} - {self.hospital}"


class PatientBasicRecords(AbstractBaseModel):
    """Models Class for Basic Record of Patient."""

    """
    This contain basic medical records of patient 
    E.g - disease,weight,age,height, previous records etc
    Each Patient will have one basic record model 
    which will be created while registering the patient 
    this can be further updated by doctor.
    """
    patient = models.OneToOneField(
        to=Patient, on_delete=models.CASCADE, related_name="basic_record"
    )
    weight = models.IntegerField(
        _("Weight of Patient (in Kilos)"),
        null=True,
        blank=True,
    )
    age = models.IntegerField(
        _("Age of Patient"),
        null=True,
        blank=True,
    )
    height = models.IntegerField(
        _("Height of Patient (in cms)"),
        null=True,
        blank=True,
    )

    @property
    def bmi(self):
        """Get BMI of Patient."""
        return (self.weight * 10000) / (self.height**2)

    # Below fields contains data of basic visit form
    # which patient fill like stomach pain, eye checkup etc.
    purpose_of_visit = models.TextField(
        _("Purpose of Visit of Patient to Hospital"), null=True, blank=True
    )
    current_medications = models.TextField(
        _("Current Medicines Taking(If Any)"), null=True, blank=True
    )
    previous_diseases = models.TextField(
        _("Previous Diseases of Patient"), null=True, blank=True
    )
    previous_medications = models.TextField(
        _("Previous Medicines Taken/Operations Performed Etc."), null=True, blank=True
    )

    class Meta:
        verbose_name = _("Patient Basic Medical Record")
        verbose_name_plural = _("Patient Basic Medical Records")

    def __str__(self):
        return f"Basic Record - {self.patient}"
