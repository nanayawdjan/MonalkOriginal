# Generated by Django 2.2 on 2022-09-13 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0043_auto_20220912_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentextra',
            name='updatingtime',
        ),
    ]
