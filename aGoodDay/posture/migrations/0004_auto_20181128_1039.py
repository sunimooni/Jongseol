# Generated by Django 2.1.3 on 2018-11-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posture', '0003_auto_20181128_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posture',
            name='date',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]