# Generated by Django 3.0.4 on 2020-03-17 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200317_1556'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.AlterField(
            model_name='mycart',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 17, 21, 3, 35, 345183)),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 17, 21, 3, 35, 345183)),
        ),
    ]
