# Generated by Django 2.0.5 on 2018-05-25 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breeds', '0004_breed_breeding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='binomial_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]