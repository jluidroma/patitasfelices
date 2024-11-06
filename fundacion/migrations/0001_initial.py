# Generated by Django 5.1.1 on 2024-11-04 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Administrador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=128)),
                ("telefono", models.CharField(blank=True, max_length=15)),
                ("fecha_creacion", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Mascota",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("especie", models.CharField(max_length=50)),
                ("raza", models.CharField(blank=True, max_length=50)),
                ("edad", models.PositiveIntegerField()),
                (
                    "sexo",
                    models.CharField(
                        choices=[("M", "Macho"), ("H", "Hembra")], max_length=1
                    ),
                ),
                ("descripcion", models.TextField(blank=True)),
                ("imagen", models.ImageField(upload_to="mascotas/")),
                (
                    "estado_adopcion",
                    models.CharField(default="Disponible", max_length=20),
                ),
                ("fecha_registro", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="SolicitudAdopcion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_solicitante", models.CharField(max_length=100)),
                ("email_solicitante", models.EmailField(max_length=254)),
                ("telefono_solicitante", models.CharField(max_length=15)),
                ("direccion_solicitante", models.CharField(max_length=200)),
                ("fecha_solicitud", models.DateField(auto_now_add=True)),
                (
                    "estado_solicitud",
                    models.CharField(
                        choices=[
                            ("Pendiente", "Pendiente"),
                            ("Aprobada", "Aprobada"),
                            ("Rechazada", "Rechazada"),
                        ],
                        default="Pendiente",
                        max_length=10,
                    ),
                ),
                ("observaciones", models.TextField(blank=True)),
                (
                    "mascota",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="solicitudes",
                        to="fundacion.mascota",
                    ),
                ),
            ],
        ),
    ]