# Generated by Django 3.0.7 on 2020-06-29 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0008_auto_20200629_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='telephone',
            field=models.CharField(default='', max_length=200),
        ),
    ]
