# Generated by Django 5.0.1 on 2024-03-08 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetailsTab',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=255, null=True)),
                ('lname', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(max_length=55, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('dob', models.DateField(null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('userrole', models.CharField(max_length=10, null=True)),
                ('idprooftype', models.CharField(max_length=20, null=True)),
                ('idproofnumber', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.userdetailstab'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.userdetailstab'),
        ),
        migrations.AlterField(
            model_name='members',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.userdetailstab'),
        ),
    ]
