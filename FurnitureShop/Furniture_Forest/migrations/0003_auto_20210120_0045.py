# Generated by Django 3.1.5 on 2021-01-20 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Furniture_Forest', '0002_auto_20210120_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
