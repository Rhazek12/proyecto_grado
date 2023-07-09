"""
Autor: Juan D. Gil T.
Correo: juan.gil.trujillo@correounivalle.edu.co
Versión: 1.0.0
Fecha: 2023-07-08
Descripción: Este código importa el módulo 'admin' de Django y los modelos 'campus_diverso' del archivo de modelos.
Luego, registra estos modelos para que sean accesibles desde la interfaz de administración de Django.
"""

from django.contrib import admin
from modulo_campus_diverso.models import *

# Register your models here.

# ====================== Módulo Persona ====================== #
admin.site.register(PertenenciaGrupoPoblacional)
admin.site.register(Persona)


# ====================== Módulo Diversidad Sexual ====================== #
admin.site.register(RespuestaCambioDocumento)
admin.site.register(OrientacionSexual)
admin.site.register(ExpresionGenero)
admin.site.register(IdentidadGenero)
admin.site.register(Pronombre)
admin.site.register(DiversidadSexual)


# ====================== Módulo Información General ====================== #
admin.site.register(OcupacionActual)
admin.site.register(ActividadTiempoLibre)
admin.site.register(FuenteIngresos)
admin.site.register(ConvivenciaVivienda)
admin.site.register(RedApoyo)
admin.site.register(FactorRiesgo)
admin.site.register(EncuentroDiaHora)
admin.site.register(InformacionGeneral)


# ====================== Módulo Información Académica ====================== # 
admin.site.register(Estamento)
admin.site.register(InformacionAcademica)


# ====================== Módulo Documentos Autorización ====================== # 

admin.site.register(DocumentosAutorizacion)


# ====================== Módulo Seguimiento ====================== #   
admin.site.register(Seguimiento)