# Generated by Django 2.0.5 on 2018-08-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='year',
            field=models.CharField(default=2018, max_length=4),
        ),
    ]