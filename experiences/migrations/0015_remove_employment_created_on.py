# Generated by Django 3.2 on 2022-07-19 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0014_alter_employment_start_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employment',
            name='created_on',
        ),
    ]
