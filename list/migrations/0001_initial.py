# Generated by Django 3.0.1 on 2020-05-19 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booth', models.IntegerField()),
                ('section', models.IntegerField()),
                ('center', models.CharField(max_length=100)),
                ('name_hindi', models.CharField(blank=True, max_length=100)),
                ('name_english', models.CharField(blank=True, default='  ', max_length=100)),
                ('relation_name_hindi', models.CharField(blank=True, default='  ', max_length=100)),
                ('relation_name_english', models.CharField(blank=True, default='  ', max_length=100)),
                ('relation_type', models.CharField(blank=True, default='  ', max_length=100)),
                ('address_hindi', models.CharField(blank=True, max_length=100)),
                ('address_english', models.CharField(blank=True, max_length=100)),
                ('TEHSIL', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(blank=True, max_length=100)),
                ('dob', models.DateField(blank=True, null=True)),
                ('MOBILE', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Agra',
            fields=[
                ('list_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='list.list')),
            ],
            bases=('list.list',),
        ),
        migrations.CreateModel(
            name='Aligarh',
            fields=[
                ('list_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='list.list')),
            ],
            bases=('list.list',),
        ),
        migrations.CreateModel(
            name='Auraiya',
            fields=[
                ('list_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='list.list')),
            ],
            bases=('list.list',),
        ),
        migrations.CreateModel(
            name='Etah',
            fields=[
                ('list_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='list.list')),
            ],
            bases=('list.list',),
        ),
        migrations.CreateModel(
            name='Etawah',
            fields=[
                ('list_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='list.list')),
            ],
            bases=('list.list',),
        ),
        migrations.CreateModel(
            name='Farrukhabad',
            fields=[
                ('list_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='list.list')),
            ],
            bases=('list.list',),
        ),
        migrations.CreateModel(
            name='Firozabad',
            fields=[
                ('list_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='list.list')),
            ],
            bases=('list.list',),
        ),
        migrations.CreateModel(
            name='Hathras',
            fields=[
                ('list_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='list.list')),
            ],
            bases=('list.list',),
        ),
        migrations.CreateModel(
            name='Kannauj',
            fields=[
                ('list_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='list.list')),
            ],
            bases=('list.list',),
        ),
        migrations.CreateModel(
            name='Kasganj',
            fields=[
                ('list_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='list.list')),
            ],
            bases=('list.list',),
        ),
        migrations.CreateModel(
            name='Mainpuri',
            fields=[
                ('list_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='list.list')),
            ],
            bases=('list.list',),
        ),
        migrations.CreateModel(
            name='Mathura',
            fields=[
                ('list_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='list.list')),
            ],
            bases=('list.list',),
        ),
    ]
