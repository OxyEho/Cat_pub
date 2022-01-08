# Generated by Django 4.0 on 2022-01-05 18:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookedModel',
            fields=[
                ('booked_date', models.DateTimeField(primary_key=True, serialize=False)),
                ('booked_uid', models.UUIDField(default=uuid.uuid4)),
                ('table_id', models.IntegerField()),
                ('person_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TableModel',
            fields=[
                ('_id', models.IntegerField(primary_key=True, serialize=False)),
                ('max_person_count', models.IntegerField()),
            ],
        ),
    ]
