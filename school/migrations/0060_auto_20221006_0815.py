# Generated by Django 2.2 on 2022-10-06 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0059_auto_20221006_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='carpay',
            field=models.FloatField(blank=True, null=True),
        ),
    ]