# Generated by Django 5.0.1 on 2024-03-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstType', '0002_userprofile_age_userprofile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
