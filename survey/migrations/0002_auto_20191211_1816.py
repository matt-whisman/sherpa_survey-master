# Generated by Django 3.0 on 2019-12-11 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='question1',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='question2',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='question3',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='question4',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='question5',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='response1',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='response2',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='response3',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='response4',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='response5',
        ),
        migrations.AddField(
            model_name='survey',
            name='room_score1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='room_score2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='room_score3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='room_score4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='room_score5',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
