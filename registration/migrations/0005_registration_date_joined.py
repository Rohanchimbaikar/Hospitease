# Generated by Django 5.0.2 on 2024-03-07 03:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_alter_registration_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
