# Generated by Django 3.1.6 on 2021-04-17 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presta', '0005_auto_20210405_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='presta',
            name='presta_start',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='presta',
            name='presta_end',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
