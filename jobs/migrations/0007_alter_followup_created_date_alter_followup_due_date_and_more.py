# Generated by Django 5.0.3 on 2024-03-14 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_followup_created_date_alter_followup_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 14, 3, 5, 56, 602185), verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='due date'),
        ),
        migrations.AlterField(
            model_name='job',
            name='applied_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 14, 3, 5, 56, 596710), verbose_name='date applied'),
        ),
    ]
