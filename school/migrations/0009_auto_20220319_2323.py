# Generated by Django 2.2 on 2022-03-19 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_auto_20220319_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='when_made',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
