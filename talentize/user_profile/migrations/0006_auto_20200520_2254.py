# Generated by Django 2.2.12 on 2020-05-20 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20200520_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='from_date',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='college',
            name='to_date',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]