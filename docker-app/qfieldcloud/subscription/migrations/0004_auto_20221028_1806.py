# Generated by Django 3.2.16 on 2022-10-28 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0059_auto_20221028_1806"),
        ("subscription", "0003_alter_plan_user_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="PackageTypeJobMinutes",
            fields=[
                (
                    "packagetype_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="subscription.packagetype",
                    ),
                ),
                ("minutes", models.PositiveIntegerField()),
            ],
            bases=("subscription.packagetype",),
        ),
        migrations.CreateModel(
            name="PackageTypeStorage",
            fields=[
                (
                    "packagetype_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="subscription.packagetype",
                    ),
                ),
                ("megabytes", models.PositiveIntegerField()),
            ],
            bases=("subscription.packagetype",),
        ),
        migrations.RenameModel(
            old_name="ExtraPackage",
            new_name="Package",
        ),
        migrations.RemoveField(
            model_name="extrapackagetypestorage",
            name="extrapackagetype_ptr",
        ),
        migrations.RenameModel(
            old_name="ExtraPackageType",
            new_name="PackageType",
        ),
        migrations.DeleteModel(
            name="ExtraPackageTypeJobMinutes",
        ),
        migrations.DeleteModel(
            name="ExtraPackageTypeStorage",
        ),
    ]
