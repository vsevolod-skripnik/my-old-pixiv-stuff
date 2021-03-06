# Generated by Django 2.1 on 2018-09-23 12:24

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kirisame', '0008_artwork_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='url',
        ),
        migrations.AddField(
            model_name='artwork',
            name='image_urls',
            field=django.contrib.postgres.fields.jsonb.JSONField(default='{}', verbose_name='Image URLs'),
            preserve_default=False,
        ),
    ]
