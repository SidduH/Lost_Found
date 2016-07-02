# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-06 05:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoundItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LostItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('contact_number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='lostitems',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User'),
        ),
        migrations.AddField(
            model_name='founditems',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User'),
        ),
    ]
