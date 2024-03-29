# Generated by Django 5.0.1 on 2024-03-14 08:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_remove_cart_transportation_remove_cart_trip_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSPages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('details', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('city', models.CharField(max_length=45)),
                ('image', models.ImageField(upload_to='trip_images/')),
                ('description', models.CharField(max_length=255)),
                ('start_place', models.CharField(max_length=45)),
                ('end_place', models.CharField(max_length=45)),
                ('pickup_point', models.CharField(max_length=45)),
                ('drop_point', models.CharField(max_length=45)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('duration_days', models.IntegerField()),
                ('category', models.CharField(max_length=45)),
                ('cost', models.CharField(max_length=100)),
                ('gst_charge', models.CharField(max_length=100)),
                ('cms_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.cmspages')),
                ('transportation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.transportation')),
            ],
        ),
    ]
