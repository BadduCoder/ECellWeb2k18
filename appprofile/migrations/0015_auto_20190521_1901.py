# Generated by Django 2.0.5 on 2019-05-21 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appprofile', '0014_auto_20190521_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ca_requests',
            old_name='ca_requests',
            new_name='user',
        ),
    ]