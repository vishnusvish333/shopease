# Generated by Django 4.2.4 on 2023-10-17 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
