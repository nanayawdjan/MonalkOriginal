# Generated by Django 2.2 on 2022-08-17 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0022_studentextra_checkifpaid'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='updatingtime',
            field=models.TimeField(auto_now=True),
        ),
    ]
