# Generated by Django 3.2.8 on 2021-10-27 09:50

from django.db import migrations, models


def rename_export_to_package(apps, schema_editor):
    Job = apps.get_model("core", "Job")
    Job.objects.filter(type="export").update(type="package")


def rename_package_to_export(apps, schema_editor):
    Job = apps.get_model("core", "Job")
    Job.objects.filter(type="package").update(type="export")


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0049_auto_20211117_1843"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="data_last_packaged_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="data_last_updated_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.RenameModel(
            old_name="ExportJob",
            new_name="PackageJob",
        ),
        migrations.AlterField(
            model_name="job",
            name="type",
            field=models.CharField(
                choices=[
                    ("package", "Package"),
                    ("delta_apply", "Delta Apply"),
                    ("process_projectfile", "Process QGIS Project File"),
                ],
                max_length=32,
            ),
        ),
        migrations.RunPython(rename_export_to_package, rename_package_to_export),
    ]
