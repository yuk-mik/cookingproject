# Generated by Django 4.0.6 on 2022-08-03 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookrecord', '0002_recordmodel_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordmodel',
            name='editor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]