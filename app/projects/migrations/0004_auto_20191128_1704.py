# Generated by Django 2.2.6 on 2019-11-28 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20191128_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collaborator',
            old_name='type',
            new_name='role',
        ),
    ]
