# Generated by Django 2.0.5 on 2018-05-25 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breeds', '0008_auto_20180525_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='binomial_name',
            field=models.CharField(blank=True, default=' ', max_length=255),
        ),
    ]
