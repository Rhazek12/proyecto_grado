# Generated by Django 4.1.1 on 2023-09-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modulo_seguimiento", "0003_alter_seguimiento_individual_academico_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seguimiento_individual",
            name="lugar",
            field=models.CharField(max_length=500),
        ),
    ]
