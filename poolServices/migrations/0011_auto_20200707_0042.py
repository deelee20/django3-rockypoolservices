# Generated by Django 3.0.6 on 2020-07-07 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poolServices', '0010_auto_20200707_0039'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service',
            new_name='MonthlyService',
        ),
    ]
