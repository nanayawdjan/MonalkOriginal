# Generated by Django 2.2 on 2022-10-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0058_auto_20221006_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='payment_method',
            field=models.CharField(choices=[('Pay_Per_Day', 'Pay Per Day'), ('School_Fees_Aside', 'School Fees Aside')], max_length=40, null=True),
        ),
    ]
