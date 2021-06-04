# Generated by Django 3.1.2 on 2021-05-31 11:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acceleration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ax', models.FloatField(default=0)),
                ('Bx', models.FloatField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('sleeptime', models.DateTimeField(default=datetime.datetime(2021, 5, 31, 11, 45, 5, 212867, tzinfo=utc), null=True)),
            ],
            options={
                'db_table': 'Acceleration',
            },
        ),
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sound', models.FloatField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('sleeptime', models.DateTimeField(default=datetime.datetime(2021, 5, 31, 11, 45, 5, 213489), null=True)),
            ],
            options={
                'db_table': 'Sound',
            },
        ),
    ]
