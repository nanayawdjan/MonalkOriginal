# Generated by Django 2.2 on 2022-08-30 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0037_studentextra_checkifpaidterm'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='schoolfee',
            field=models.FloatField(null=True),
        ),
    ]