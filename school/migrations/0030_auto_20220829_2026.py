# Generated by Django 2.2 on 2022-08-29 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0029_auto_20220829_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='foodpay',
        ),
        migrations.AddField(
            model_name='payment',
            name='pay',
            field=models.FloatField(default=2, null=True),
        ),
    ]
