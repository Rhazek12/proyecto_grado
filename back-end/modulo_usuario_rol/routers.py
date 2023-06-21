from rest_framework.routers import DefaultRouter
from modulo_usuario_rol.views import *

router = DefaultRouter()

router.register(r'user',user_viewsets,basename = 'user')
router.register(r'estudiante',estudiante_viewsets,basename = 'estudiante')
router.register(r'rol',rol_viewsets,basename = 'rol')
router.register(r'usuario_rol',usuario_rol_viewsets,basename = 'usuario_rol')
router.register(r'usuario_rol_old',usuario_rol_old_viewsets,basename = 'usuario_rol_old')
router.register(r'profesional',profesional_viewsets,basename = 'profesional')
router.register(r'practicante',practicante_viewsets,basename = 'practicante')
router.register(r'monitor',monitor_viewsets,basename = 'monitor')
router.register(r'estudiante_selected',estudiante_selected_viewsets,basename = 'estudiante_selected')
router.register(r'estudiante_actualizacion',estudiante_actualizacion_viewsets,basename = 'estudiante_actualizacion')
router.register(r'user_actualizacion',user_actualizacion_viewsets,basename = 'user_actualizacion')

router.register(r'grupos_etnicos',Grupo_etnico_viewsets,basename = 'grupos_etnicos')
router.register(r'actividad_simultanea',Actividad_simultanea_viewsets,basename = 'actividad_simultanea')
router.register(r'identidad_gen',Identidad_gen_viewsets,basename = 'identidad_gen')
router.register(r'estado_civil',Estado_civil_viewsets,basename = 'estado_civil')
router.register(r'condicion_de_excepcion',Condicion_de_excepcion_viewsets,basename = 'condicion_de_excepcion')
router.register(r'ids_estudiantes_del_monitor',ids_estudiantes_del_monitor_viewsets,basename = 'ids_estudiantes_del_monitor')
router.register(r'info_estudiantes_sin_seguimientos',info_estudiantes_sin_seguimientos_viewsets,basename = 'info_estudiantes_sin_seguimientos')
router.register(r'ultimo_seguimiento_individual',ultimo_seguimiento_individual_ViewSet,basename = 'ultimo_seguimiento_individual')
router.register(r'reporte_seguimientos',reporte_seguimientos_viewsets,basename = 'reporte_seguimientos')
router.register(r'cohorte_estudiante_info',cohorte_estudiante_info_viewsets,basename = 'cohorte_estudiante_info')
router.register(r'cohortes_lista',cohortes_lista_viewsets,basename = 'cohortes_lista')

router.register(r'historial_monitor',historial_monitor_viewsets,basename = 'historial_monitor')


urlpatterns = router.urls