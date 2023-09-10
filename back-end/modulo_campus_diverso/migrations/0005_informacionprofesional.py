# Generated by Django 4.2.4 on 2023-08-28 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_campus_diverso', '0004_alter_acompañamientorecibido_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformacionProfesional',
            fields=[
                ('id_profesional_que_brindo_atencion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_profesional_que_brindo_atencion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'campus_diverso_informacion_profesional',
            },
        ),
    ]