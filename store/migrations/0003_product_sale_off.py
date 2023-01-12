# Generated by Django 4.1.4 on 2023-01-10 03:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_off',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]