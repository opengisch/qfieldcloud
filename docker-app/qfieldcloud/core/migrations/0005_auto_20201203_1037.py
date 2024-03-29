# Generated by Django 2.2.17 on 2020-12-03 10:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_auto_20201201_1209"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delta",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "STATUS_PENDING"),
                    (2, "STATUS_BUSY"),
                    (3, "STATUS_APPLIED"),
                    (4, "STATUS_CONFLICT"),
                    (5, "STATUS_NOT_APPLIED"),
                    (6, "STATUS_ERROR"),
                ],
                default=1,
            ),
        ),
    ]
