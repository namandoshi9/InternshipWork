# Generated by Django 5.0.1 on 2024-03-14 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_alter_trip_trip_name_packages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='trip_name',
        ),
        migrations.DeleteModel(
            name='Packages',
        ),
    ]