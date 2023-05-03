# Generated by Django 4.1.1 on 2022-11-23 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("modulo_usuario_rol", "0017_alter_estudiante_cod_univalle"),
        ("modulo_geografico", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="facultad",
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
                ("codigo_univalle", models.BigIntegerField()),
                ("nombre", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="programa",
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
                ("codigo_snies", models.BigIntegerField()),
                ("codigo_univalle", models.BigIntegerField()),
                ("nombre", models.CharField(max_length=50)),
                ("jornada", models.CharField(max_length=50)),
                (
                    "id_facultad",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="id_facultad_in_programa",
                        to="modulo_programa.facultad",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="sede",
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
                ("codigo_univalle", models.BigIntegerField()),
                ("nombre", models.CharField(max_length=50)),
                (
                    "id_municipio",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="id_municipio_in_sede",
                        to="modulo_geografico.municipio",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="programa_estudiante",
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
                ("estado", models.BooleanField(default=True)),
                ("traker", models.BooleanField(default=True)),
                (
                    "id_estudiante",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="id_estudiante_in_programa_estudiante",
                        to="modulo_usuario_rol.estudiante",
                    ),
                ),
                (
                    "id_programa",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="id_programa_in_programa_estudiante",
                        to="modulo_programa.programa",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="programa",
            name="id_sede",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="id_sede_in_programa",
                to="modulo_programa.sede",
            ),
        ),
    ]
