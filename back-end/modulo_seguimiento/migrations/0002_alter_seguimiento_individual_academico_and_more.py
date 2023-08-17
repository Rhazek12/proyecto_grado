# Generated by Django 4.1.1 on 2023-08-17 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modulo_seguimiento", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="academico",
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="economico",
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="familiar",
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="individual",
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="objetivos",
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="observaciones",
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="vida_universitaria_ciudad",
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]