# Generated by Django 5.0.4 on 2024-04-16 11:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('productname', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('productbrand', models.CharField(blank=True, max_length=100, null=True)),
                ('brandcategory', models.CharField(blank=True, max_length=100, null=True)),
                ('productinfo', models.TextField(blank=True, null=True)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=8)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('stockcount', models.IntegerField(blank=True, default=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
