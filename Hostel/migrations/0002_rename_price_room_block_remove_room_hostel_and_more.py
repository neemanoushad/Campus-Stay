# Generated by Django 4.1.5 on 2023-11-24 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='price',
            new_name='block',
        ),
        migrations.RemoveField(
            model_name='room',
            name='hostel',
        ),
        migrations.RemoveField(
            model_name='room',
            name='image',
        ),
    ]
