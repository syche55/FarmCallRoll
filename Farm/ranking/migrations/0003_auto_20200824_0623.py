# Generated by Django 3.1 on 2020-08-24 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0002_auto_20200824_0608'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Player',
            new_name='User',
        ),
    ]
