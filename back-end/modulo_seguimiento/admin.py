from django.contrib import admin
from modulo_seguimiento.models import *

class seguimiento_individual_admin(admin.ModelAdmin):
    list_display = ('id','fecha', 'id_estudiante') 

class inasistencia_admin(admin.ModelAdmin):
    list_display = ('id','fecha', 'id_estudiante') 


admin.site.register(seguimiento_individual,seguimiento_individual_admin)
admin.site.register(inasistencia,inasistencia_admin)
