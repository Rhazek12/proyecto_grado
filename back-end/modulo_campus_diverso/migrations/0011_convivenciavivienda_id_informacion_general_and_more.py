# Generated by Django 4.2.5 on 2023-10-02 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_campus_diverso', '0010_remove_convivenciavivienda_id_informacion_general_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='convivenciavivienda',
            name='id_informacion_general',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='convivencias_en_vivienda', to='modulo_campus_diverso.informaciongeneral'),
        ),
        migrations.AlterField(
            model_name='acompañamientorecibido',
            name='nombre_acompañamiento_recibido',
            field=models.CharField(default='Sin nombre', max_length=200),
        ),
        migrations.AlterField(
            model_name='acompañamientorecibido',
            name='observacion_acompanamiento_recibido',
            field=models.TextField(blank=True, default='Sin observaciones'),
        ),
        migrations.AlterField(
            model_name='convivenciavivienda',
            name='observacion_convivencia_vivienda',
            field=models.TextField(blank=True, default='Sin observacion', null=True),
        ),
        migrations.AlterField(
            model_name='diversidadsexual',
            name='cambio_nombre_sexo_documento',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AlterField(
            model_name='encuentrodiahora',
            name='dia',
            field=models.CharField(default='N/A', max_length=20),
        ),
        migrations.AlterField(
            model_name='encuentrodiahora',
            name='hora',
            field=models.TimeField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='factorriesgo',
            name='nombre_factor_riesgo',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AlterField(
            model_name='fuenteingresos',
            name='nombre_fuente_ingresos',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AlterField(
            model_name='informacionprofesional',
            name='nombre_profesional_que_brindo_atencion',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='redapoyo',
            name='nombre_red_apoyo',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='nombre_profesional',
            field=models.CharField(default='N/A', max_length=150),
        ),
    ]