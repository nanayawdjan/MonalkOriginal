# Generated by Django 2.2 on 2022-08-30 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0039_schoolfeepayment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='schoolfee',
        ),
    ]