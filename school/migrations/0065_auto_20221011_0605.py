# Generated by Django 2.2 on 2022-10-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0064_auto_20221011_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='pay',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True),
        ),
    ]
