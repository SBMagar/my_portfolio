# Generated by Django 3.2 on 2024-05-01 09:48

import datetime
from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='School Name')),
                ('level', models.CharField(blank=True, max_length=255, verbose_name='Level')),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(default=datetime.datetime.now)),
                ('description', mdeditor.fields.MDTextField(blank=True, verbose_name='Description')),
                ('town', models.CharField(blank=True, max_length=255, verbose_name='City/Town')),
                ('url', models.URLField(blank=True, max_length=255, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Company Name')),
                ('position', models.CharField(blank=True, max_length=255, verbose_name='Position')),
                ('start_year', models.CharField(default='2020', max_length=255, verbose_name='Start Year')),
                ('start_month', models.CharField(default='January', max_length=255, verbose_name='Start Month')),
                ('end_year', models.CharField(blank=True, max_length=255, verbose_name='End Year')),
                ('end_month', models.CharField(blank=True, max_length=255, verbose_name='End Month')),
                ('current_status', models.BooleanField(default=False, verbose_name='Currently Working')),
                ('end_date_value', models.CharField(blank=True, max_length=255, verbose_name='End Date')),
                ('description', mdeditor.fields.MDTextField(blank=True, verbose_name='Description')),
                ('town', models.CharField(blank=True, max_length=255, verbose_name='City/Town')),
                ('url', models.URLField(blank=True, max_length=255, verbose_name='URL')),
            ],
        ),
    ]
