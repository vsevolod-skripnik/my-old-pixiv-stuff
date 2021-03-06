# Generated by Django 2.1 on 2018-09-23 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kirisame', '0006_auto_20180923_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='account',
            field=models.CharField(default=' ', max_length=255, verbose_name='Account'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name'),
        ),
    ]
