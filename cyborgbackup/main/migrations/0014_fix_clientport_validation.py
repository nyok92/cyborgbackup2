# Generated by Django 2.2.23 on 2021-05-22 16:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0013_client_port'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitystream',
            name='setting',
        ),
        migrations.AlterField(
            model_name='client',
            name='port',
            field=models.PositiveIntegerField(blank=True, default=22,
                                              validators=[django.core.validators.MinValueValidator(1),
                                                          django.core.validators.MaxValueValidator(65535)]),
        ),
    ]
