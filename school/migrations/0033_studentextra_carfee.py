# Generated by Django 2.2 on 2022-08-29 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0032_payment_carpay'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='carfee',
            field=models.FloatField(null=True),
        ),
    ]
