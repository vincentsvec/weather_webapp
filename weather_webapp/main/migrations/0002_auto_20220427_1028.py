# Generated by Django 3.2.9 on 2022-04-27 10:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='location',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), default=None, null=True, size=2),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='saved_cities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default=list, null=True, size=8),
        ),
    ]