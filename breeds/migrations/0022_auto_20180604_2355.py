# Generated by Django 2.0.5 on 2018-06-04 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breeds', '0021_auto_20180604_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breedimage',
            name='image_name',
            field=models.ImageField(null=True, upload_to='breed_images'),
        ),
    ]
