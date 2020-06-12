# Generated by Django 2.2.12 on 2020-05-29 15:18

from django.db import migrations, models
import djongo.models.fields
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200528_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='MesiboGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.IntegerField(blank=True)),
                ('status', models.BooleanField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MesiboUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=100)),
                ('access_token', models.CharField(blank=True, max_length=100)),
                ('groups', djongo.models.fields.ArrayField(blank=True, model_container=user.models.MesiboGroup)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='mesibo_token',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mesibo_uid',
        ),
        migrations.AddField(
            model_name='user',
            name='mesibo_details',
            field=djongo.models.fields.EmbeddedField(blank=True, model_container=user.models.MesiboUser, null=True),
        ),
    ]