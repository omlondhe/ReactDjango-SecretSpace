# Generated by Django 3.1.4 on 2020-12-12 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_secrets'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secrets',
            old_name='timestamp',
            new_name='at',
        ),
    ]