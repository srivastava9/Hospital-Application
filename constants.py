from django.utils.translation import gettext_lazy as _

ERR_MSG_TEMPLATE_ENVVAR_NOT_FOUND = _("Cannot find environment variable {var_name}")
ERR_MSG_APPOINTMENT_DATE = _("Appointment Date should be of after today's date")
ERR_MSG_DOCTOR_APPOINTMENT_ALREADY_SET = (
    "Doctor Appointment is already present in set datetime"
)
