# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-30 18:05
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start Time')),
                ('end_date', models.DateTimeField(default=datetime.datetime(2016, 11, 30, 19, 5, 49, 557273), verbose_name='End Time')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=50)),
                ('number_patients', models.IntegerField(default=0)),
                ('number_patient_visits', models.IntegerField(default=0)),
                ('average_number_hospital_visits_per_patient', models.FloatField(default=0)),
                ('average_patient_stay_time', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('working_hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Hospital')),
            ],
            options={
                'verbose_name': 'Nurse',
                'verbose_name_plural': 'Nurses',
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(default='None', max_length=100)),
                ('phone_number', models.CharField(default='None', max_length=10)),
                ('insurance_id', models.CharField(default='None', max_length=10)),
                ('insurance_provider', models.CharField(default='None', max_length=30)),
                ('emergency_contact_name', models.CharField(default='None', max_length=50)),
                ('emergency_contact_phone_number', models.CharField(default='None', max_length=10)),
                ('medical_information', models.FileField(upload_to='patient_uploads/')),
                ('current_hospital_id', models.IntegerField(default=0)),
                ('is_checked_in', models.BooleanField(default=False)),
                ('avg_hospital_visit_time', models.IntegerField(default=0)),
                ('number_hospital_visits', models.IntegerField(default=0)),
                ('temp_check_in_time', models.DateTimeField(default=datetime.datetime(2016, 11, 30, 18, 5, 49, 554271))),
                ('temp_check_out_time', models.DateTimeField(default=datetime.datetime(2016, 11, 30, 18, 5, 49, 554271))),
                ('checked_in_hospital', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checked_in_hospital+', to='health.Hospital')),
                ('main_hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health.Hospital')),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription_name', models.CharField(default='None', max_length=100)),
                ('times_prescribed', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Prescription',
                'verbose_name_plural': 'Prescriptions',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('is_released', models.BooleanField(default=False)),
                ('results', models.FileField(upload_to='tests/')),
                ('issuer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='health.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='prescriptions',
            field=models.ManyToManyField(to='health.Prescription'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospitals',
            field=models.ManyToManyField(default=None, to='health.Hospital'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='health.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='hospital',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='health.Hospital'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='health.Patient'),
        ),
    ]
