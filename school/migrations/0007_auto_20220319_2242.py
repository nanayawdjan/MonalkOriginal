# Generated by Django 2.2 on 2022-03-19 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20220318_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='cl',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='present_status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='roll',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
