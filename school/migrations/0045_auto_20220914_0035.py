# Generated by Django 2.2 on 2022-09-13 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0044_remove_studentextra_updatingtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='broom',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='soap',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='troll',
            field=models.BooleanField(default=False),
        ),
    ]
