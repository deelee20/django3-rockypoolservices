# Generated by Django 3.0.6 on 2020-09-11 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_client',
            name='message',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='repair_request',
            name='message',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
