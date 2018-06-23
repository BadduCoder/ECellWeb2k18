# Generated by Django 2.0.4 on 2018-05-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0002_auto_20180519_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='spons_type',
            field=models.CharField(choices=[('AS', 'Associate Sponsors'), ('PLTS', 'Platinum Sponsors'), ('GS', 'Gold Sponsors'), ('TS', 'Title Sponsors'), ('PRTS', 'Partner Sponsors')], default='AS', max_length=4),
        ),
    ]
