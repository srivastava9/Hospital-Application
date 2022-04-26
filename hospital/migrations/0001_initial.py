# Generated by Django 3.2.7 on 2022-04-26 21:33

from django.db import migrations, models
import django.db.models.deletion
import hospital.models.hospitals
import hospital.models.patient
import utilities.models.abstract_model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', utilities.models.abstract_model.PrimarykeyField(default=utilities.models.abstract_model.get_str_uuid, editable=False, help_text='Primary Key Field for Object', max_length=48, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('metadata', models.JSONField(blank=True, default=dict)),
                ('name', models.CharField(max_length=128, verbose_name='Name of Doctor')),
                ('education', models.JSONField(blank=True, default=dict, null=True, verbose_name='Educational Qualification of Doctor')),
                ('experience', models.JSONField(blank=True, default=dict, null=True, verbose_name='Work Experience of Doctor')),
                ('contact_details', models.JSONField(blank=True, default=hospital.models.hospitals.ContactDetailDefault, null=True, verbose_name='Contact Details of Doctor')),
                ('active', models.BooleanField(default=True, verbose_name='Is Active in this Hospital')),
                ('specializations', models.JSONField(blank=True, default=dict, null=True, verbose_name='Specializations of Doctor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', utilities.models.abstract_model.PrimarykeyField(default=utilities.models.abstract_model.get_str_uuid, editable=False, help_text='Primary Key Field for Object', max_length=48, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('metadata', models.JSONField(blank=True, default=dict)),
                ('name', models.CharField(max_length=128, verbose_name='Name of Hospital')),
                ('address', models.CharField(max_length=256, verbose_name='Address of Hospital')),
                ('no_beds', models.IntegerField(blank=True, null=True, verbose_name='Number of Beds')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', utilities.models.abstract_model.PrimarykeyField(default=utilities.models.abstract_model.get_str_uuid, editable=False, help_text='Primary Key Field for Object', max_length=48, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('metadata', models.JSONField(blank=True, default=dict)),
                ('name', models.CharField(max_length=128, verbose_name='Name of Patient')),
                ('address', models.CharField(max_length=256, verbose_name='Address of Patient')),
                ('sex', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], default='MALE', max_length=8, verbose_name='Sex of Patient')),
                ('contact_details', models.JSONField(blank=True, default=hospital.models.patient.PatientContactDetailDefaults, null=True, verbose_name='Contact Details of Doctor')),
                ('emergency_contact_details', models.JSONField(blank=True, default=hospital.models.patient.EmergencyContactDetailDefault, null=True, verbose_name='Emergency Contact Details of Patient')),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.hospital', verbose_name='Hospital Of Patient')),
                ('main_doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.doctor', verbose_name='Main Doctor of Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PatientBasicRecords',
            fields=[
                ('id', utilities.models.abstract_model.PrimarykeyField(default=utilities.models.abstract_model.get_str_uuid, editable=False, help_text='Primary Key Field for Object', max_length=48, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('metadata', models.JSONField(blank=True, default=dict)),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='Weight of Patient (in Kilos)')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Age of Patient')),
                ('height', models.IntegerField(blank=True, null=True, verbose_name='Height of Patient (in cms)')),
                ('purpose_of_visit', models.TextField(blank=True, null=True, verbose_name='Purpose of Visit of Patient to Hospital')),
                ('current_medications', models.TextField(blank=True, null=True, verbose_name='Current Medicines Taking(If Any)')),
                ('previous_diseases', models.TextField(blank=True, null=True, verbose_name='Previous Diseases of Patient')),
                ('previous_medications', models.TextField(blank=True, null=True, verbose_name='Previous Medicines Taken/Operations Performed Etc.')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='basic_record', to='hospital.patient')),
            ],
            options={
                'verbose_name': 'Patient Basic Medical Record',
                'verbose_name_plural': 'Patient Basic Medical Records',
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctors', to='hospital.hospital', verbose_name='Hospital of Doctor'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', utilities.models.abstract_model.PrimarykeyField(default=utilities.models.abstract_model.get_str_uuid, editable=False, help_text='Primary Key Field for Object', max_length=48, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('metadata', models.JSONField(blank=True, default=dict)),
                ('appointment_on', models.DateTimeField(verbose_name='Appointed Date and Time')),
                ('purpose_of_visit', models.TextField(blank=True, null=True, verbose_name='Purpose of Appointment')),
                ('doctor_remark', models.TextField(blank=True, null=True, verbose_name='Remark of Doctor after Appointment')),
                ('medication_remark', models.TextField(blank=True, null=True, verbose_name='Medicines Suggested after Appointment')),
                ('test_remark', models.TextField(blank=True, null=True, verbose_name='Test Suggested after Appointment')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='appointments', to='hospital.doctor', verbose_name='Doctor for Appointment')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='appointments', to='hospital.patient', verbose_name='Patient for Appointment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
