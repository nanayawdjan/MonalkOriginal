# Generated by Django 2.2 on 2022-10-04 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0051_studentextra_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='are_they_considered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='are_they_two',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='complete_pay_daily',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='do_they_pay',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='do_they_pay_all',
            field=models.BooleanField(default=False),
        ),
    ]