# Generated by Django 4.2.2 on 2024-02-16 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0003_room_room_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_type',
        ),
    ]
