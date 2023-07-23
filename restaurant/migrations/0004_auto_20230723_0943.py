# Generated by Django 4.2.3 on 2023-07-23 09:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0003_alter_booking_no_of_guests_alter_menu_inventory"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="name",
        ),
        migrations.AddField(
            model_name="booking",
            name="user",
            field=models.ForeignKey(
                to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
            ),
        ),
    ]
