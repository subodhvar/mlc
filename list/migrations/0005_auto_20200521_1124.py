# Generated by Django 3.0.1 on 2020-05-21 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_aligarh_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='Booth',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='list',
            name='TEHSIL',
            field=models.CharField(blank=True, default='  ', max_length=100),
        ),
        migrations.AlterField(
            model_name='list',
            name='section',
            field=models.IntegerField(default=0),
        ),
    ]
