# Generated by Django 2.1 on 2018-09-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kirisame', '0020_auto_20180930_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toot',
            name='publish_date',
        ),
        migrations.AddField(
            model_name='toot',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Published at'),
        ),
        migrations.AddField(
            model_name='toot',
            name='scheduled_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Scheduled at'),
        ),
    ]
