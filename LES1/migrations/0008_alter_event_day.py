# Generated by Django 4.1.2 on 2022-12-13 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LES1', '0007_event_day_alter_event_description_alter_event_tittle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Day',
            field=models.DateField(default=datetime.date(2022, 12, 13)),
        ),
    ]