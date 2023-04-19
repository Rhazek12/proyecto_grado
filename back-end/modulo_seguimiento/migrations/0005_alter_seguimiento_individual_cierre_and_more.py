# Generated by Django 4.1.1 on 2023-01-04 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modulo_seguimiento", "0004_alter_inasistencia_revisado_practicante_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="cierre",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="primer_acercamiento",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="revisado_practicante",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="revisado_profesional",
            field=models.BooleanField(default=False),
        ),
    ]