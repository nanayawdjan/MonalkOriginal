# Generated by Django 2.2 on 2022-10-06 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0053_auto_20221004_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentextra',
            name='are_they_considered',
        ),
        migrations.RemoveField(
            model_name='studentextra',
            name='are_they_two',
        ),
        migrations.RemoveField(
            model_name='studentextra',
            name='complete_pay_daily',
        ),
        migrations.RemoveField(
            model_name='studentextra',
            name='do_they_pay_all',
        ),
        migrations.RemoveField(
            model_name='studentextra',
            name='do_they_pay_at_all',
        ),
        migrations.RemoveField(
            model_name='studentextra',
            name='take_bus',
        ),
    ]