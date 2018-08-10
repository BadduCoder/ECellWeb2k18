# Generated by Django 2.0.5 on 2018-08-06 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appprofile', '0006_auto_20180618_1000'),
        ('bquiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAcknowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acknowledge_id', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='question',
            old_name='q_set',
            new_name='set',
        ),
        migrations.RemoveField(
            model_name='question',
            name='q_type',
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('IMG', 'Image Question'), ('TXT', 'Test Question')], default='TXT', max_length=2),
        ),
        migrations.AddField(
            model_name='questionacknowledge',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bquiz.Question'),
        ),
        migrations.AddField(
            model_name='questionacknowledge',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appprofile.Profile'),
        ),
    ]