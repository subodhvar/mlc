# Generated by Django 3.0.1 on 2020-05-22 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0009_delete_agra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agra',
            fields=[
                ('list_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='list.list')),
            ],
            bases=('list.list',),
        ),
    ]