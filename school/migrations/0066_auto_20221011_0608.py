# Generated by Django 2.2 on 2022-10-11 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0065_auto_20221011_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='pay',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
