# Generated by Django 4.2.5 on 2023-09-28 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_campus_diverso', '0006_informacionprofesional_id_informacion_general'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentosautorizacion',
            name='apgar_familiar',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='informaciongeneral',
            name='actividades_especificas_tiempo_libre',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='informaciongeneral',
            name='comentarios_o_sugerencias_de_usuario',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='informaciongeneral',
            name='creencia_religiosa',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='informaciongeneral',
            name='observacion_general_factores_de_riesgo',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='informaciongeneral',
            name='observacion_general_fuente_de_ingresos',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='informaciongeneral',
            name='observacion_general_redes_de_apoyo',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='informaciongeneral',
            name='origen_descubrimiento_campus_diverso',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='informaciongeneral',
            name='relacion_familiar',
            field=models.IntegerField(null=True),
        ),
    ]
