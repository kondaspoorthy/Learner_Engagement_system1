# Generated by Django 4.1.2 on 2022-12-14 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LES1', '0008_alter_event_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Day',
            field=models.DateField(default=datetime.date(2022, 12, 14)),
        ),
        migrations.AlterField(
            model_name='event',
            name='Description',
            field=models.TextField(max_length=100),
        ),
    ]
