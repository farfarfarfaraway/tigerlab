# Generated by Django 3.2.4 on 2021-06-20 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='accident_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 20, 10, 3, 32, 378480)),
        ),
        migrations.AlterField(
            model_name='claim',
            name='vehicle_year_make',
            field=models.DateField(default=datetime.datetime(2021, 6, 20, 10, 3, 32, 378386)),
        ),
    ]