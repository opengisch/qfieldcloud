# Generated by Django 3.2 on 2021-04-08 01:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0026_auto_20210409_1339"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccount",
            name="avatar_uri",
            field=models.CharField(
                blank=True,
                max_length=255,
                verbose_name="Profile Picture URI",
            ),
        ),
    ]
