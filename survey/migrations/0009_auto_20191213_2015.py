# Generated by Django 3.0 on 2019-12-13 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0008_auto_20191211_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='room_score1',
            field=models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='room_score2',
            field=models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='room_score3',
            field=models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='room_score4',
            field=models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='room_score5',
            field=models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
    ]
