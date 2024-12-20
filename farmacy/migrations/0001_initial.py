# Generated by Django 5.1.1 on 2024-11-03 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('pharmacy_name', models.CharField(max_length=20)),
                ('license_number', models.CharField(max_length=6, unique=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qrcodes/')),
            ],
        ),
    ]
