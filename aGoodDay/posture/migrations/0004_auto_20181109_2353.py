# Generated by Django 2.1.3 on 2018-11-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posture', '0003_auto_20181109_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='saX',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='device',
            name='saY',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='device',
            name='saZ',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='device',
            name='sgX',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='device',
            name='sgY',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='device',
            name='sgZ',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='device',
            name='xdegree',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='device',
            name='ydegree',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='device',
            name='zdegree',
            field=models.FloatField(default=0),
        ),
    ]
