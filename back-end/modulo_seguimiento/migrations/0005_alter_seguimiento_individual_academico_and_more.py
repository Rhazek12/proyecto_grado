# Generated by Django 4.1.1 on 2023-09-07 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modulo_seguimiento", "0004_alter_seguimiento_individual_lugar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="academico",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="economico",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="familiar",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="individual",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="objetivos",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="observaciones",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="vida_universitaria_ciudad",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
