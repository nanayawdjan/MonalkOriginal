# Generated by Django 2.2 on 2022-08-29 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0034_auto_20220829_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='foodfee',
            field=models.FloatField(null=True),
        ),
    ]
