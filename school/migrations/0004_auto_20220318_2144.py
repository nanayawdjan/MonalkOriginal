# Generated by Django 2.2 on 2022-03-18 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20220318_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='cl',
            field=models.CharField(choices=[('F & B', 'F & B'), ('P.S.', 'P.S.'), ('K.S.A.', 'K.S.A.'), ('K.S.B.', 'K.S.B.'), ('K.S.C.', 'K.S.C.'), ('L.S.A.', 'L.S.A.')], default='one', max_length=10),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='date_of_admission',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='fee',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='mobile',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='residence',
            field=models.CharField(choices=[('Dwenem', 'Dwenem'), ('Mpuasu', 'Mpuasu'), ('Adamsu', 'Adamsu'), ('Bodaa', 'Bodaa'), ('Kofitia', 'Kofitia'), ('Adiokor1', 'Adiokor1'), ('Adiokor2', 'Adiokor2'), ('Zezera', 'Zezera'), ('Kwamepim', 'Kwamepim')], max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='roll',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
