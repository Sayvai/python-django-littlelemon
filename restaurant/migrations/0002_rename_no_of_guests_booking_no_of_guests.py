# Generated by Django 4.2.3 on 2023-07-21 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='No_of_guests',
            new_name='no_of_guests',
        ),
    ]
