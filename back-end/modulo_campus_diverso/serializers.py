"""
Autor: Juan D. Gil T.
Correo: juan.gil.trujillo@correounivalle.edu.co
Versión: 1.0.0
Fecha: 2023-07-08
Descripción: Este código importa los serializadores de 'Django' 'rest_framework' y los modelos de modulo_campus_diverso.
Los cuales se utilizan para serializar los datos de los modelos correspondientes, y por ende dinamizar las peticiones HTTP.
La clase 'Meta' se define en cada serializador y especifica el modelo y los campos a incluir en la serialización.  
"""

from rest_framework import serializers
from modulo_campus_diverso.models import *



# ====================== Módulo Diversidad Sexual ====================== #

class RespuestaCambioDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaCambioDocumento
        fields = '__all__'

class OrientacionSexualSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrientacionSexual
        fields = '__all__'

class ExpresionGeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpresionGenero
        fields = '__all__'

class IdentidadGeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentidadGenero
        fields = '__all__'

class PronombreSerializer(serializers.ModelSerializer):
    nombre_pronombre = serializers.CharField(max_length=50, required=True)
    
    class Meta:
        model = Pronombre
        fields = '__all__'

# Listing Fields de los serializers

class RespuestaCambioDocumentoListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_respuesta_cambio_documento
   
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict):
            return data['nombre_respuesta_cambio_documento'].strip()
        raise serializers.ValidationError('Invalid input format.')

class OrientacionSexualListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_orientacion_sexual
   
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict):
            return data['nombre_orientacion_sexual'].strip()
        raise serializers.ValidationError('Invalid input format.')

class ExpresionGeneroListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_expresion_genero
   
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict):
            return data['nombre_expresion_genero'].strip()
        raise serializers.ValidationError('Invalid input format.')

class IdentidadGeneroListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_identidad_genero
    
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict):
            return data['nombre_identidad_genero'].strip()
        raise serializers.ValidationError('Invalid input format.')


class PronombreListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_pronombre
    
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict):
            return data['nombre_pronombre'].strip()
        raise serializers.ValidationError('Invalid input format.')

class DiversidadSexualSerializer(serializers.ModelSerializer):
    id_persona = serializers.CharField(max_length=30, required=True)
    
    respuestas_cambio_documento = RespuestaCambioDocumentoListingField(
        many=True,
        queryset= RespuestaCambioDocumento.objects.all(),
        required=False,
    )
    
    orientaciones_sexuales = OrientacionSexualListingField(
        many=True,
        queryset= OrientacionSexual.objects.all(),
        required=False,
    )

    expresiones_de_genero = ExpresionGeneroListingField(
        many=True,
        queryset=ExpresionGenero.objects.all(),
        required=False,
    )
    
    identidades_de_genero = IdentidadGeneroListingField(
        many=True,
        queryset=IdentidadGenero.objects.all(),
        required=False,
    )
    
    pronombres = PronombreListingField(
        many=True,
        queryset=Pronombre.objects.all(),
        required=False,
    )
    
     
    class Meta:
        model = DiversidadSexual
        fields = '__all__'
    
    def create(self, validated_data):
        # Extracción de campos de la petición JSON
        id_persona = validated_data.pop('id_persona')
        respuestas_cambio_documento = validated_data.pop('respuestas_cambio_documento')
        orientaciones_sexuales = validated_data.pop('orientaciones_sexuales')
        expresiones_de_genero = validated_data.pop('expresiones_de_genero')
        pronombres = validated_data.pop('pronombres', [])
        identidades_de_genero = validated_data.pop('identidades_de_genero')
        
        persona = Persona.objects.get(numero_documento=id_persona) #! Así son más fáciles las consultas
        
        # Creación del objeto DiversidadSexual
        diversidad_sexual = DiversidadSexual.objects.create(id_persona=persona, **validated_data)
        
        # RespuestaCambioDocumento
        for nombre_respuesta_cambio_documento in respuestas_cambio_documento:
            respuesta_cambio_documento, _ = RespuestaCambioDocumento.objects.get_or_create(nombre_respuesta_cambio_documento=nombre_respuesta_cambio_documento)
            diversidad_sexual.respuestas_cambio_documento.add(respuesta_cambio_documento) 
        
        # OrientacionSexual
        for nombre_orientacion_sexual in orientaciones_sexuales:
            orientacion_sexual, _ = OrientacionSexual.objects.get_or_create(nombre_orientacion_sexual=nombre_orientacion_sexual)
            diversidad_sexual.orientaciones_sexuales.add(orientacion_sexual) 
        
       # ExpresionGenero
        for nombre_expresion_genero in expresiones_de_genero:
            expresion_genero, _ = ExpresionGenero.objects.get_or_create(nombre_expresion_genero=nombre_expresion_genero)
            diversidad_sexual.expresiones_de_genero.add(expresion_genero) 
        
        # IdentidadGenero
        for nombre_identidad_genero in identidades_de_genero:
            identidad_genero, _ = IdentidadGenero.objects.get_or_create(nombre_identidad_genero=nombre_identidad_genero)
            diversidad_sexual.identidades_de_genero.add(identidad_genero)
            
        # Pronombre
        for pronombre in pronombres:
            pronombres, _ = Pronombre.objects.get_or_create(nombre_pronombre=pronombre)
            diversidad_sexual.pronombres.add(pronombres)
        
        return diversidad_sexual 











# ====================== Módulo Información General ====================== #
  
  
class FuenteIngresosSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuenteIngresos
        fields = '__all__'

class OcupacionActualSerializer(serializers.ModelSerializer):
    class Meta:
        model = OcupacionActual
        fields = '__all__' 

class ActividadTiempoLibreSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ActividadTiempoLibre
        fields = "__all__"

class ConvivenciaViviendaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ConvivenciaVivienda
        fields = "__all__"
        
class RedApoyoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = RedApoyo
        fields = "__all__"
        
class FactorRiesgoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = FactorRiesgo
        fields = "__all__"

class EncuentroDiaHoraSerializer(serializers.ModelSerializer): 
    class Meta:
        model = EncuentroDiaHora
        fields = "__all__"

#! Se utilizó esta clase para que excluya el campo id_informacion_general al momento de realizar la petición HTTP
class EncuentroDiaHoraGetSerializer(serializers.ModelSerializer): 
    class Meta:
        model = EncuentroDiaHora
        exclude = ['id_informacion_general']

# ListingField
class OcupacionActualListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_ocupacion_actual
   
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict):
            return data['nombre_ocupacion_actual'].strip()
        raise serializers.ValidationError('Invalid input format.')


class ActividadTiempoLibreListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'nombre_actividad_tiempo_libre': value.nombre_actividad_tiempo_libre,
            'observacion_actividad_tiempo_libre': value.observacion_actividad_tiempo_libre
        }

    def to_internal_value(self, data):
        if isinstance(data, dict):
            nombre_actividad = data.get('nombre_actividad_tiempo_libre', '').strip()
            observacion_actividad = data.get('observacion_actividad_tiempo_libre', '').strip()
            return {
                'nombre_actividad_tiempo_libre': nombre_actividad,
                'observacion_actividad_tiempo_libre': observacion_actividad
            }
        raise serializers.ValidationError('Invalid input format.')


# Serializer Informacion General
class InformacionGeneralSerializer(serializers.ModelSerializer):

    id_persona = serializers.CharField(max_length=30, required=True) 
    
    ocupaciones_actuales = OcupacionActualListingField(
        many=True,
        queryset=OcupacionActual.objects.all(),
        required=False,
    )
    
    actividades_tiempo_libre = ActividadTiempoLibreSerializer(many=True)
    fuentes_de_ingresos = FuenteIngresosSerializer(many=True)
    convivencias_en_vivienda = ConvivenciaViviendaSerializer(many=True)
    redes_de_apoyo = RedApoyoSerializer(many=True)
    factores_de_riesgo = FactorRiesgoSerializer(many=True)
    encuentro_dias_horas = EncuentroDiaHoraGetSerializer(many=True)
    
    class Meta:
        model = InformacionGeneral
        fields = '__all__'
    
    def create(self, validated_data):
        id_persona = validated_data.pop('id_persona',[])
        
        ocupaciones_actuales = validated_data.pop('ocupaciones_actuales',[])
        actividades_tiempo_libre = validated_data.pop('actividades_tiempo_libre',[])
        fuentes_de_ingresos = validated_data.pop('fuentes_de_ingresos',[])
        convivencias_en_vivienda = validated_data.pop('convivencias_en_vivienda',[])
        redes_de_apoyo = validated_data.pop('redes_de_apoyo',[])
        factores_de_riesgo = validated_data.pop('factores_de_riesgo',[])
        encuentro_dias_horas = validated_data.pop('encuentro_dias_horas',[])
        
        persona = Persona.objects.get(numero_documento=id_persona)
        
        informacion_general = InformacionGeneral.objects.create(id_persona=persona, **validated_data)
        
         # OcupacionActual
        for nombre_ocupacion_actual in ocupaciones_actuales:
            ocupacion_actual, _ = OcupacionActual.objects.get_or_create(nombre_ocupacion_actual=nombre_ocupacion_actual)
            informacion_general.ocupaciones_actuales.add(ocupacion_actual)
         
        # ActividadTiempoLibre    
        for actividad_tiempo_libre_data in actividades_tiempo_libre: 
            ActividadTiempoLibre.objects.create(id_informacion_general=informacion_general,**actividad_tiempo_libre_data)
        
        # FuenteIngresos
        for fuente_ingreso_data in fuentes_de_ingresos:
            FuenteIngresos.objects.create(id_informacion_general=informacion_general, **fuente_ingreso_data)
            
        # ConvivenciaVivienda
        for convivencia_vivienda_data in convivencias_en_vivienda:
            ConvivenciaVivienda.objects.create(id_informacion_general=informacion_general, **convivencia_vivienda_data)
        
        # RedApoyo
        for red_apoyo_data in redes_de_apoyo:
            RedApoyo.objects.create(id_informacion_general=informacion_general, **red_apoyo_data)
            
        # FactorRiesgo
        for factor_riesgo_data in factores_de_riesgo:
            FactorRiesgo.objects.create(id_informacion_general=informacion_general, **factor_riesgo_data)
            
        # EncuentroDiaHora
        for encuentro_dia_hora_data in encuentro_dias_horas:
            # EncuentroDiaHora.objects.create(id_informacion_general=informacion_general, **encuentro_dia_hora_data)
            # encuentro_dia_hora = EncuentroDiaHora.objects.get_or_create(**encuentro_dia_hora_data)
            # informacion_general.encuentro_dias_horas.add(encuentro_dia_hora)
            encuentro_dia_hora = EncuentroDiaHora.objects.filter(**encuentro_dia_hora_data).first()
            if not encuentro_dia_hora:
                encuentro_dia_hora = EncuentroDiaHora.objects.create(**encuentro_dia_hora_data)
            informacion_general.encuentro_dias_horas.add(encuentro_dia_hora)
         
        return informacion_general









# ====================== Módulo Información Académica ====================== # 

class EstamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estamento
        fields = '__all__'

class EstamentoListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_estamento
   
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict):
            return data['nombre_estamento'].strip()
        raise serializers.ValidationError('Invalid input format.')

class InformacionAcademicaSerializer(serializers.ModelSerializer):

    id_persona = serializers.CharField(max_length=30, required=True)
    estamentos = EstamentoListingField(
        many=True,
        queryset= Estamento.objects.all(),
        required=False,
    )
    
    class Meta:
        model = InformacionAcademica
        fields = '__all__'
    
    def create(self, validated_data):
        id_persona = validated_data.pop('id_persona')
        
        estamentos = validated_data.pop('estamentos',[])
        
        persona = Persona.objects.get(numero_documento=id_persona)
        
        informacion_academica = InformacionAcademica.objects.create(id_persona=persona, **validated_data)
        
        for nombre_estamento in estamentos:
            estamento,_ = Estamento.objects.get_or_create(nombre_estamento=nombre_estamento)
            informacion_academica.estamentos.add(estamento)
        
        return informacion_academica
        
    
    







# ====================== Módulo Documentos Autorización ====================== # 

class DocumentosAutorizacionSerializer(serializers.ModelSerializer):
  
    id_persona = serializers.CharField(max_length=30, required=True)
  
    class Meta:
        model = DocumentosAutorizacion
        fields = '__all__'
        
    def create(self, validated_data):
        id_persona = validated_data.pop('id_persona')
        
        persona = Persona.objects.get(numero_documento=id_persona)
        documentos_autorizacion = DocumentosAutorizacion.objects.create(id_persona=persona, **validated_data)
        
        return documentos_autorizacion








# ====================== Módulo Seguimiento ====================== #   
class SeguimientoSerializer(serializers.ModelSerializer):
    id_persona = serializers.CharField(max_length=30, required=True)
    
    class Meta:
        model = Seguimiento
        fields = '__all__'
        
    def create(self, validated_data):
        id_persona = validated_data.pop('id_persona')
        
        persona = Persona.objects.get(numero_documento=id_persona)
        seguimiento = Seguimiento.objects.create(id_persona=persona, **validated_data)
        return seguimiento
      
      
      
      


# ====================== Módulo Persona ====================== #

class PertenenciaGrupoPoblacionalSerializer(serializers.ModelSerializer):
    nombre_grupo_poblacional = serializers.CharField(max_length=300, required=True)
    class Meta:
        model = PertenenciaGrupoPoblacional
        fields = '__all__'

class PertenenciaGrupoPoblacionalListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_grupo_poblacional
    
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict) and 'nombre_grupo_poblacional' in data:
            return data['nombre_grupo_poblacional'].strip()
        raise serializers.ValidationError('Invalid input format.')
    
    

class PersonaSerializer(serializers.ModelSerializer):
 
    diversidad_sexual = DiversidadSexualSerializer(required=False)
    informacion_academica = InformacionAcademicaSerializer(required=False)
    informacion_general = InformacionGeneralSerializer(required=False)
    documentos_autorizacion = DocumentosAutorizacionSerializer(required=False)
    seguimientos = SeguimientoSerializer(many=True, required=False)
    
    ciudad_nacimiento = serializers.CharField(max_length=100, default="Ciudad no especificada", required=False)
    municipio_nacimiento = serializers.CharField(max_length=100, default="Municipio no especificado", required=False)
    corregimiento_nacimiento = serializers.CharField(max_length=100, default="Corregimiento no especificado", required=False)
    ciudad_residencia = serializers.CharField(max_length=100, default="Ciudad no especificada", required=False)
    municipio_residencia = serializers.CharField(max_length=100, default="Municipio no especificado", required=False)
    corregimiento_residencia = serializers.CharField(max_length=100, default="Corregimiento no especificado", required=False)
    
    pertenencia_grupo_poblacional = PertenenciaGrupoPoblacionalListingField(
        many=True, 
        queryset=PertenenciaGrupoPoblacional.objects.all(),
        required=False, 
        ) 
    
    class Meta:
        model = Persona
        fields = '__all__'
   

    def create(self, validated_data):
        
        pertenencia_grupo_poblacional_names = validated_data.pop('pertenencia_grupo_poblacional',[]) 
        persona = Persona.objects.create(**validated_data) 
        print(pertenencia_grupo_poblacional_names)
        
        for pertenencia_grupo_poblacional_name in pertenencia_grupo_poblacional_names:  
            try: 
                pertenencia_grupo_poblacional = PertenenciaGrupoPoblacional.objects.get (nombre_grupo_poblacional=pertenencia_grupo_poblacional_name.strip()) 
            except PertenenciaGrupoPoblacional.DoesNotExist: 
                pertenencia_grupo_poblacional = PertenenciaGrupoPoblacional.objects.create(nombre_grupo_poblacional=pertenencia_grupo_poblacional_name.strip())    
            persona.pertenencia_grupo_poblacional.add(pertenencia_grupo_poblacional)
         
        return persona