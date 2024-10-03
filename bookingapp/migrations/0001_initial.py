# Generated by Django 5.1 on 2024-09-13 17:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabin_number', models.CharField(max_length=50)),
                ('cabin_type', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['cabin_number', 'cabin_type'],
            },
        ),
        migrations.CreateModel(
            name='LivingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_day', models.CharField(max_length=100)),
                ('end_day', models.CharField(max_length=100)),
                ('cabin', models.ForeignKey(default='unknown plane', on_delete=django.db.models.deletion.SET_DEFAULT, to='bookingapp.cabin')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('with_kid', models.BooleanField()),
                ('Visitor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Booked cabin with Visitors',
                'db_table': 'Visitors',
            },
        ),
        migrations.CreateModel(
            name='CabinNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liv_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.livingtime')),
                ('visitor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.visitor')),
            ],
            options={
                'verbose_name': 'Free cabin',
                'verbose_name_plural': 'Free cabins',
            },
        ),
    ]
