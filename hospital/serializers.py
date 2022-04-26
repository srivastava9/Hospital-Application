from rest_framework import serializers
from hospital.models.appointments import Appointment

from hospital.models.hospitals import Doctor


from .models import Patient, PatientBasicRecords


class PatientRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientBasicRecords
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class AppointmentDataSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = "__all__"

    def create(self, validated_data):
        """Create Appointment."""
        doctor = self.context["view"].kwargs.get("doctor_id")
        patient = self.context["view"].kwargs.get("patient_id")
        appointment_on = validated_data.get("appointment_on")
        purpose_of_visit = validated_data.get("purpose_of_visit")
        return Appointment.objects.create(
            doctor_id=doctor,
            patient_id=patient,
            appointment_on=appointment_on,
            purpose_of_visit=purpose_of_visit,
        )


class PatientDataSerializers(serializers.ModelSerializer):
    """Serializer Class for Patients."""

    patient_id = serializers.CharField(
        read_only=True, source="id"
    )  # Unique Id of Patient
    patient_record = serializers.SerializerMethodField()
    main_doctor = serializers.SerializerMethodField()
    appointment_data = serializers.SerializerMethodField()

    def get_patient_record(self, obj):
        """Return patient Records"""
        return PatientRecordSerializer(obj.basic_record).data

    def get_main_doctor(self, obj):
        """Return Main Doctor data."""
        return DoctorSerializer(obj.main_doctor).data

    def get_appointment_data(self, obj):
        """Return Appointment Data."""
        return AppointmentDataSerializer(obj.appointments, many=True).data

    class Meta:
        model = Patient
        fields = (
            "patient_id",
            "name",
            "address",
            "sex",
            "contact_details",
            "emergency_contact_details",
            "patient_record",
            "main_doctor",
            "appointment_data",
        )
