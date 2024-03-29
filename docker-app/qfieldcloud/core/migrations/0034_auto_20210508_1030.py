# Generated by Django 3.2 on 2021-05-08 10:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0033_auto_20210419_1908"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="has_accepted_tos",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="has_newsletter_subscription",
            field=models.BooleanField(default=False),
        ),
    ]
