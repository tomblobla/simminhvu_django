# Generated by Django 4.1.4 on 2023-01-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_sale_off'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='products', related_query_name='product', to='store.tag'),
        ),
    ]
