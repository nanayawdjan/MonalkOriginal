# Generated by Django 2.2 on 2022-10-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0063_auto_20221011_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='pay',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
    ]
