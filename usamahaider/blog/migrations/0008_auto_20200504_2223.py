# Generated by Django 3.0.3 on 2020-05-04 21:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200504_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 21, 23, 55, 431105, tzinfo=utc)),
        ),
    ]
