# Generated by Django 2.0.7 on 2018-07-25 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chirp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chirp',
            name='datetime',
        ),
        migrations.AddField(
            model_name='chirp',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
