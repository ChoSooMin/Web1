# Generated by Django 3.1.5 on 2021-01-20 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Furniture_Forest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]
