# Generated by Django 5.0.4 on 2024-04-19 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='numReviews',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
