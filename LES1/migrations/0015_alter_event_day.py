# Generated by Django 4.1.2 on 2022-12-21 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LES1", "0014_remove_forum_date_created_alter_event_day"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="Day",
            field=models.DateField(default=datetime.date(2022, 12, 21)),
        ),
    ]
