# Generated by Django 4.0 on 2022-01-05 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablemodel',
            old_name='_id',
            new_name='id',
        ),
    ]