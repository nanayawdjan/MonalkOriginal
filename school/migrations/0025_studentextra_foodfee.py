# Generated by Django 2.2 on 2022-08-29 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0024_auto_20220829_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='foodfee',
            field=models.FloatField(default=2, null=True),
        ),
    ]
