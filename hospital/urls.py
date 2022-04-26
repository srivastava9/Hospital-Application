from django.urls import path
from .views import *

app_name = "hospital"
urlpatterns = [
    path(
        "<str:hospital_id>/patients", PatientListView.as_view(), name="List Of Patients"
    ),
    path("<str:hospital_id>/doctors", DoctorListView.as_view(), name="List Of Doctors"),
    path(
        "<str:hospital_id>/patients/<str:patient_id>",
        PatientRecordView.as_view(),
        name="Get Patient Record",
    ),
    path(
        "<str:hospital_id>/patients/<str:patient_id>/doctors/<str:doctor_id>/appointments",
        GetAndCreateAppointment.as_view(),
        name="Get And Create Appointments",
    ),
]
