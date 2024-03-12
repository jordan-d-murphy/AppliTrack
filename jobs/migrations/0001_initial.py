# Generated by Django 5.0.3 on 2024-03-12 05:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('applied_date', models.DateTimeField(verbose_name='date applied')),
                ('favorite', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(verbose_name='date added')),
                ('due_date', models.DateTimeField(verbose_name='due date')),
                ('resolved', models.BooleanField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
        ),
    ]
