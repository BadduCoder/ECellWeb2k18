# Generated by Django 2.0.5 on 2018-08-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cumulative_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
