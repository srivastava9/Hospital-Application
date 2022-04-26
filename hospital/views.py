from django.shortcuts import render
from html5lib import serialize
from rest_framework import generics
from constants import ERR_MSG_ID_INVALID

from hospital.models import Patient
from hospital.models.appointments import Appointment
from hospital.models.hospitals import Doctor
from hospital.serializers import (
    AppointmentDataSerializer,
    DoctorSerializer,
    PatientDataSerializers,
    PatientSerializer,
)
from utilities.exceptions import get_object_or_invalid

# Create your views here.
class PatientListView(generics.ListAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        return Patient.objects.filter(hospital_id=self.kwargs.get("hospital_id"))


class DoctorListView(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        return Doctor.objects.filter(hospital_id=self.kwargs.get("hospital_id"))


class PatientRecordView(generics.RetrieveAPIView):
    serializer_class = PatientDataSerializers

    def get_object(self):
        return get_object_or_invalid(
            Patient,
            id=self.kwargs.get("patient_id"),
            error_message=ERR_MSG_ID_INVALID.format("Patient"),
        )


class GetAndCreateAppointment(generics.ListCreateAPIView):
    serializer_class = AppointmentDataSerializer

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.kwargs.get("patient_id"))
