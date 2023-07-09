"""
Autor: Juan D. Gil T.
Correo: juan.gil.trujillo@correounivalle.edu.co
Versión: 1.0.0
Fecha: 2023-07-08
Descripción: Este código define varios modelos que se utilizan para representar 
los diferentes módulos que conforman la ficha de registro para utilizar el servicio 
de acompañamiento de Campus Diverso
Cada modelo define diferentes campos y relaciones que se utilizan para almacenar 
información específica en una base de datos.
Adicionalmente existen modelos diccionario que tienen como propósito realizar una 
relación de "muchos a muchos" además de extender la información de dichos 
campos según sea necesario (después de todo, en la ficha de registro existen campos 
con respuestas abiertas por la persona o usuario) 
Todos los modelos están asociados con una su tabla específica de la base de datos, que se define mediante la propiedad "db_table" de su clase "Meta".
"""

from django.db import models

# Create your models here.

# ====================== Módulo Persona ====================== #

class PertenenciaGrupoPoblacional(models.Model):
    """
    Esta clase es una tabla diccionario del modelo Persona
    """
    id_grupo_poblacional = models.AutoField(primary_key=True)
    nombre_grupo_poblacional = models.CharField(max_length=300, unique=True) 

    class Meta:
        db_table = "campus_diverso_pertenencia_grupo_poblacional"
    
    def __str__(self):
        return self.nombre_grupo_poblacional

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    incluir_correo_en_respuesta = models.BooleanField(default=False)
    nombre_identitario = models.CharField(max_length=150)
    nombre_y_apellido = models.CharField(max_length=150)
    tipo_documento = models.CharField(max_length=50)
    numero_documento = models.CharField(max_length=30, unique=True)
    fecha_nacimiento = models.DateField()
    estrato_socioeconomico = models.IntegerField()
    ciudad_nacimiento = models.CharField(max_length=100, default="Ciudad no especificada")
    municipio_nacimiento = models.CharField(max_length=100, default="Municipio no especificado")
    corregimiento_nacimiento = models.CharField(max_length=100, default="Corregimiento no especificado")
    departamento_nacimiento = models.CharField(max_length=100)
    pais_nacimiento = models.CharField(max_length=100)
    ciudad_residencia = models.CharField(max_length=100, default="Ciudad no especificada")
    municipio_residencia = models.CharField(max_length=100, default="Municipio no especificado")
    corregimiento_residencia = models.CharField(max_length=100, default="Corregimiento no especificado")
    zona_residencial = models.CharField(max_length=100)
    direccion_residencia = models.CharField(max_length=200)
    barrio_residencia = models.CharField(max_length=150)
    comuna_barrio = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    estado_civil = models.CharField(max_length=30)
    identidad_etnico_racial = models.CharField(max_length=70)
    nombre_persona_de_confianza = models.TextField()
    relacion_persona_de_confianza = models.TextField()
    telefono_persona_de_confianza = models.TextField()
    pertenencia_grupo_poblacional = models.ManyToManyField(PertenenciaGrupoPoblacional,max_length=300, related_name="personas", blank=False) 
    
    def __str__(self):
        return f"Persona ID: {self.id_persona}, número documento: {self.numero_documento}, nombre: {self.nombre_y_apellido}"  

    class Meta:
        db_table = "campus_diverso_persona"
        



# ====================== Módulo Diversidad Sexual ====================== #

class RespuestaCambioDocumento(models.Model):
    """
    Esta clase es una tabla diccionario del modelo DiversidadSexual
    """
    id_respuesta_cambio_documento = models.AutoField(primary_key=True)
    nombre_respuesta_cambio_documento = models.TextField(unique=True)
    
    def __str__(self):
        return f"{self.nombre_respuesta_cambio_documento}"
      
    class Meta:
        db_table = "campus_diverso_respuesta_cambio_documento"

class OrientacionSexual(models.Model):
    """
    Esta clase es una tabla diccionario del modelo DiversidadSexual
    """
    id_orientacion_sexual = models.AutoField(primary_key=True)
    nombre_orientacion_sexual = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return f"{self.nombre_orientacion_sexual}"
      
    class Meta:
        db_table = "campus_diverso_orientacion_sexual"

class ExpresionGenero(models.Model):
    """
    Esta clase es una tabla diccionario del modelo DiversidadSexual
    """
    id_expresion_genero = models.AutoField(primary_key=True)
    nombre_expresion_genero = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return f"{self.nombre_expresion_genero}"
      
    class Meta:
        db_table = "campus_diverso_expresion_genero"

class IdentidadGenero(models.Model):
    """
    Esta clase es una tabla diccionario del modelo DiversidadSexual
    """
    id_identidad_genero = models.AutoField(primary_key=True)
    nombre_identidad_genero = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return f"{self.nombre_identidad_genero}"
      
    class Meta:
        db_table = "campus_diverso_identidad_genero"

class Pronombre(models.Model):
    """
    Esta clase es una tabla diccionario del modelo DiversidadSexual
    """
    id_pronombre = models.AutoField(primary_key=True)
    nombre_pronombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.nombre_pronombre}"
      
    class Meta:
        db_table = "campus_diverso_pronombre"

class DiversidadSexual(models.Model):
    id_diversidad_sexual = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Persona, on_delete=models.CASCADE, null=False, blank=False, related_name="diversidad_sexual") 
    cambio_nombre_sexo_documento = models.CharField(max_length=50)
    recibir_orientacion_cambio_en_documento = models.BooleanField()
    pronombres = models.ManyToManyField(Pronombre, max_length=50)
    identidades_de_genero = models.ManyToManyField(IdentidadGenero,max_length=200)
    expresiones_de_genero = models.ManyToManyField(ExpresionGenero,max_length=200)
    orientaciones_sexuales = models.ManyToManyField(OrientacionSexual,max_length=200)
    respuestas_cambio_documento = models.ManyToManyField(RespuestaCambioDocumento)

    class Meta:
        db_table = "campus_diverso_diversidad_sexual"
    
    def __str__(self):
        return f"ID DiversidadSexual: {self.id_diversidad_sexual}, Persona: {self.id_persona}"
      

# ====================== Módulo Información General ====================== #
 

class OcupacionActual(models.Model):
    """
    Esta clase es una tabla diccionario del modelo InformacionGeneral
    """
    id_ocupacion_actual = models.AutoField(primary_key=True)
    nombre_ocupacion_actual = models.CharField(max_length=200, unique=True)
    
    class Meta:
        db_table = "campus_diverso_ocupacion_actual"
    
    def __str__(self):
        return f"OcupacionActual: {self.nombre_ocupacion_actual}"
    
    
class ActividadTiempoLibre(models.Model):
    id_actividad_tiempo_libre = models.AutoField(primary_key=True)
    nombre_actividad_tiempo_libre = models.CharField(max_length=200)
    observacion_actividad_tiempo_libre = models.TextField(blank=True, null=False, default="Sin observación")
    id_informacion_general = models.ForeignKey('InformacionGeneral', on_delete=models.CASCADE, related_name="actividades_tiempo_libre", blank=True)
    
    class Meta:
        db_table = "campus_diverso_actividad_tiempo_libre"
    
    def __str__(self):
        return f"ActividadTiempoLibre {self.id_actividad_tiempo_libre}," + f" nombre: {self.nombre_actividad_tiempo_libre}," + f" Informacion General: {self.id_informacion_general}"

class FuenteIngresos(models.Model):
    id_fuente_ingresos = models.AutoField(primary_key=True)
    nombre_fuente_ingresos = models.CharField(max_length=200)
    observacion_fuente_ingresos = models.TextField(blank=True, default="Sin Observación")
    id_informacion_general = models.ForeignKey('InformacionGeneral', on_delete=models.CASCADE, related_name='fuentes_de_ingresos', blank=True)
    
    class Meta:
        db_table = "campus_diverso_fuente_ingresos"
    
    def __str__(self):
        return f"FuenteIngresos {self.id_fuente_ingresos}" + f" nombre: {self.nombre_fuente_ingresos}," + f" Informacion General: {self.id_informacion_general}"
 
 
class ConvivenciaVivienda(models.Model):
    id_convivencia_vivienda = models.AutoField(primary_key=True)
    nombre_convivencia_vivienda = models.CharField(max_length=200)
    observacion_convivencia_vivienda = models.TextField(blank=True, default="Sin observacion")
    id_informacion_general = models.ForeignKey('InformacionGeneral', on_delete=models.CASCADE, related_name='convivencias_en_vivienda', blank=True)
    
    class Meta:
        db_table = "campus_diverso_convivencia_vivienda"
    
    def __str__(self):
        return f"ConvivenciaVivienda {self.id_convivencia_vivienda}" + f" nombre: {self.nombre_convivencia_vivienda}," + f" Informacion General: {self.id_informacion_general}"
    
class RedApoyo(models.Model):
    id_red_apoyo = models.AutoField(primary_key=True)
    nombre_red_apoyo = models.CharField(max_length=200)
    observacion_red_apoyo = models.TextField(blank=True, default="Sin observacion")
    id_informacion_general = models.ForeignKey('InformacionGeneral', on_delete=models.CASCADE, related_name='redes_de_apoyo', blank=True)
    
    class Meta:
        db_table = "campus_diverso_red_apoyo"
    
    def __str__(self):
        return f"RedApoyo {self.id_red_apoyo}" + f" nombre: {self.nombre_red_apoyo}," + f" Informacion General: {self.id_informacion_general}"

class FactorRiesgo(models.Model):
    id_factor_riesgo = models.AutoField(primary_key=True)
    nombre_factor_riesgo = models.CharField(max_length=200)
    observacion_factor_riesgo = models.TextField(blank=True, default="Sin observacion")
    id_informacion_general = models.ForeignKey('InformacionGeneral', on_delete=models.CASCADE, related_name='factores_de_riesgo', blank=True)
    
    class Meta:
        db_table = "campus_diverso_factor_riesgo"
    
    def __str__(self):
        return f"FactorRiesgo {self.id_factor_riesgo}" + f" nombre: {self.nombre_factor_riesgo}," + f" Informacion General: {self.id_informacion_general}"

class EncuentroDiaHora(models.Model):
    """
    Esta clase es una tabla diccionario del modelo InformacionGeneral
    """
    id_encuentro_dia_hora = models.AutoField(primary_key=True)  
    dia = models.CharField(max_length=20)
    hora = models.TimeField() 
    id_informacion_general = models.ManyToManyField('InformacionGeneral', related_name='encuentro_dias_horas', blank=True)
    
    class Meta:
        db_table = "campus_diverso_encuentro_dia_hora"
    
    def __str__(self):
        return f"EncuentroDiaHora {self.id_encuentro_dia_hora}" + f" dia: {self.dia}," + f" hora: {self.hora},"  + f" Informacion General: {self.id_informacion_general}" 
 
class InformacionGeneral(models.Model):
    id_informacion_general = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Persona, on_delete=models.CASCADE, null=False, blank=False, related_name="informacion_general")
    dedicacion_externa = models.CharField(max_length=100)
    tipo_acompanamiento_recibido = models.CharField(max_length=70)
    observacion_tipo_acompanamiento_recibido = models.TextField()
    tipo_entidad_acompanamiento_recibido = models.TextField()
    tipo_profesional_acompanamiento_recibido = models.TextField()
    calificacion_acompanamiento_recibido = models.IntegerField(null=True)
    motivo_calificacion_acompanamiento = models.TextField(null=True)
    actividades_especificas_tiempo_libre = models.TextField()
    observacion_general_actividades_especificas_tiempo_libre = models.TextField()
    observacion_general_fuente_de_ingresos = models.TextField()
    observacion_general_relacion_familiar = models.TextField()
    relacion_familiar = models.IntegerField()
    observacion_general_redes_de_apoyo = models.TextField()
    observacion_general_factores_de_riesgo = models.TextField()
    creencia_religiosa = models.TextField()
    encuentro_inicial = models.CharField(max_length=30)
    observacion_horario = models.TextField(blank=False, default="Sin observación")
    origen_descubrimiento_campus_diverso = models.CharField(max_length=300)
    comentarios_o_sugerencias_de_usuario = models.TextField()
    ocupaciones_actuales = models.ManyToManyField(OcupacionActual, max_length=200, related_name="informaciones_generales") 
    # encuentros_dias_horas = models.ManyToManyField(EncuentroDiaHora, related_name="informacion_general_id")

    class Meta:
        db_table = "campus_diverso_informacion_general"
    
    def __str__(self):
        return f"IdInformacionGeneral: {self.id_informacion_general}, persona: {self.id_persona}"




# ====================== Módulo Información Académica ====================== # 

class Estamento(models.Model):
    """
    Esta clase es una tabla diccionario del modelo InformacionAcademica
    """
    id_estamento = models.AutoField(primary_key=True)
    nombre_estamento = models.CharField(max_length=100, unique=True)
    
    class Meta:
        db_table = "campus_diverso_estamento"
    
    def __str__(self):
        return f"Estamento: {self.nombre_estamento}"

class InformacionAcademica(models.Model):
    id_informacion_academica = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Persona, on_delete=models.CASCADE, null=False, blank=False, related_name="informacion_academica")
    pertenencia_univalle = models.BooleanField()
    sede_universidad = models.CharField(max_length=20)
    nombre_programa_academico = models.CharField(max_length=100)
    codigo_estudiante = models.CharField(max_length=20, unique=True)
    semestre_academico = models.IntegerField()
    estamentos = models.ManyToManyField(Estamento, max_length=100, related_name="id_informacion_academica")
    
    class Meta:
        db_table = "campus_diverso_informacion_academica"
    
    def __str__(self):
        return f"InformacionAcademica: {self.id_informacion_academica}, persona: {self.id_persona}"



# ====================== Módulo Documentos Autorización ====================== # 

class DocumentosAutorizacion(models.Model):
    id_documentos_autorizacion = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Persona, on_delete=models.CASCADE, null=False, blank=False, related_name="documentos_autorizacion")
    autorizacion_manejo_de_datos = models.BooleanField()
    firma_consentimiento_informado = models.BooleanField()
    firma_terapia_hormonal = models.BooleanField(null=True, blank=True)
    documento_digital_y_archivo = models.BooleanField(null=True, blank=True)
    apgar_familiar = models.IntegerField()
    ecomapa = models.BooleanField(null=True, blank=True)
    arbol_familiar = models.BooleanField(null=True, blank=True)

    class Meta:
        db_table = "campus_diverso_documentos_autorizacion"

    def __str__(self):
        return f"DocumentosAutorizacion {self.id_documentos_autorizacion}, persona: {self.id_persona}"



# ====================== Módulo Seguimiento ====================== #   

class Seguimiento(models.Model):
    id_seguimiento = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False, related_name="seguimientos")
    nombre_profesional = models.CharField(max_length=150)
    fecha = models.DateField()
    observacion = models.TextField(blank=False, null=False)
    
    class Meta:
        db_table = "campus_diverso_seguimiento"
    
    def __str__(self):
        return f"Seguimiento: {self.id_seguimiento}, persona: {self.id_persona}"
