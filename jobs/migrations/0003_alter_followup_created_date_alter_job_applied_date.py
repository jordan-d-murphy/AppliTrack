# Generated by Django 5.0.3 on 2024-03-14 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_followup_description_alter_followup_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 14, 2, 19, 34, 38303), verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='job',
            name='applied_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 14, 2, 19, 34, 32783), verbose_name='date applied'),
        ),
    ]
