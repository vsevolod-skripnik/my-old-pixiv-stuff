# Generated by Django 2.1 on 2018-09-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kirisame', '0007_auto_20180923_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='type',
            field=models.SmallIntegerField(choices=[(0, 'Illust'), (1, 'Manga'), (2, 'Ugoira')], default=0, verbose_name='Type'),
        ),
    ]
