# Generated by Django 2.0.5 on 2018-05-26 00:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('breeds', '0013_auto_20180525_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
