# Generated by Django 5.1.1 on 2024-11-06 05:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fundacion", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="solicitudadopcion",
            name="fecha_solicitud",
        ),
    ]
