# Generated by Django 4.1.2 on 2022-12-15 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LES1', '0011_alter_event_day_alter_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Day',
            field=models.DateField(default=datetime.date(2022, 12, 15)),
        ),
    ]
