# Generated by Django 2.2 on 2022-09-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0047_payment_schoolfees'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='debt',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
