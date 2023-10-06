# Generated by Django 4.2.5 on 2023-10-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_campus_diverso', '0008_alter_informaciongeneral_decision_encuentro_inicial_con_profesional_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acompañamientorecibido',
            name='nombre_acompañamiento_recibido',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='convivenciavivienda',
            name='nombre_convivencia_vivienda',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='diversidadsexual',
            name='cambio_nombre_sexo_documento',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='encuentrodiahora',
            name='dia',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='encuentrodiahora',
            name='hora',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='factorriesgo',
            name='nombre_factor_riesgo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='fuenteingresos',
            name='nombre_fuente_ingresos',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='informacionprofesional',
            name='nombre_profesional_que_brindo_atencion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='redapoyo',
            name='nombre_red_apoyo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
