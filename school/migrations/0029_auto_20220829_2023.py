# Generated by Django 2.2 on 2022-08-29 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0028_auto_20220829_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='pay',
        ),
        migrations.AddField(
            model_name='payment',
            name='foodpay',
            field=models.FloatField(default=2, null=True),
        ),
    ]
