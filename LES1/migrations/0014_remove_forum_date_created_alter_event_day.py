# Generated by Django 4.1.2 on 2022-12-18 16:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LES1", "0013_forum_alter_event_day_discussion"),
    ]

    operations = [
        migrations.RemoveField(model_name="forum", name="date_created",),
        migrations.AlterField(
            model_name="event",
            name="Day",
            field=models.DateField(default=datetime.date(2022, 12, 18)),
        ),
    ]
