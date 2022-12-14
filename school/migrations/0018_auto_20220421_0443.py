# Generated by Django 2.2 on 2022-04-21 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0017_auto_20220420_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='balance',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='depth',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='pay',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
