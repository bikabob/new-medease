# Generated by Django 5.1.1 on 2024-11-02 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_alter_hospitalmodel_doctors_patientdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdetails',
            name='doctor',
        ),
    ]