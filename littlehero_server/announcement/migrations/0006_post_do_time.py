# Generated by Django 3.0.7 on 2020-06-29 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0005_auto_20200629_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='do_time',
            field=models.CharField(default='', max_length=200),
        ),
    ]
