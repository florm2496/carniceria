# Generated by Django 3.0.6 on 2020-10-23 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vino', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vino',
            name='foto',
        ),
    ]
