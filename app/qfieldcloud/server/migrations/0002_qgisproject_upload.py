# Generated by Django 2.2 on 2019-11-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qgisproject',
            name='upload',
            field=models.FileField(default=None, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
