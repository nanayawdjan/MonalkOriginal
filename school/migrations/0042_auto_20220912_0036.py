# Generated by Django 2.2 on 2022-09-11 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0041_auto_20220905_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='fee',
            field=models.FloatField(null=True),
        ),
    ]
