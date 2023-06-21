from ast import And
from operator import and_
from queue import Empty
from datetime import datetime
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, Serializer
from modulo_usuario_rol.models import rol, usuario_rol, estudiante, act_simultanea, cond_excepcion, discap_men, estado_civil,  etnia, identidad_gen, cohorte_estudiante
from modulo_geografico.models import barrio, departamento, municipio
from modulo_programa.models import programa_estudiante, programa, historial_estado_programa_estudiante
from modulo_instancia.models import semestre, cohorte
from modulo_asignacion.models import asignacion
from modulo_seguimiento.models import inasistencia, seguimiento_individual

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from modulo_usuario_rol import serializers
from django.db.models import F
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import  user_serializer,estudiante_serializer,rol_serializer,usuario_rol_serializer, Estudiante_actualizacion,user_selected, Grupo_etnico_serializer, Actividad_simultanea_serializer, Identidad_de_genero_serializer, Estado_civil_serializer, Condicion_de_excepcion_serializer, cohorte_estudiante_serializer, user_actualizacion
from modulo_programa.serializers import  programa_estudiante_serializer, programa_serializer, historial_estado_programa_estudiante_serializer
from modulo_instancia.serializers import semestre_serializer, cohorte_serializer
from modulo_asignacion.serializers import asignacion_serializer
from modulo_seguimiento.serializers import seguimiento_individual_serializer, inasistencia_serializer

from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import action

from rest_framework.viewsets import ModelViewSet
import pandas as pd

# Create your views here.
class user_viewsets (viewsets.ModelViewSet):
    serializer_class = user_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = user_serializer.Meta.model.objects.all()


class estudiante_viewsets(viewsets.ModelViewSet):
    serializer_class = estudiante_serializer
    queryset = estudiante_serializer.Meta.model.objects.all()

    def retrieve(self, request, pk=None):
        var_estudiante = estudiante.objects.get(id=pk)
        serializer_estudiante = estudiante_serializer(var_estudiante)
        diccionario_estudiante = serializer_estudiante.data
        #llamado y seteo de barrios, ciudades y otros campos que hagan llamada a otra tabla ademas de estudiante (osea, estudiante tiene el id del campo a llamar de otra tabla)
        #barrio_ini         barrio_res
        barrio_ini_id = diccionario_estudiante['barrio_ini']
        barrio_res_id = diccionario_estudiante['barrio_res']
        try:
            barrio_ini_obj = barrio.objects.get(codigo_barrio=barrio_ini_id)
            diccionario_estudiante['barrio_ini'] = barrio_ini_obj.nombre
        except barrio.DoesNotExist:
            diccionario_estudiante['barrio_ini'] = None
        try:
            barrio_res_obj = barrio.objects.get(codigo_barrio=barrio_res_id)
            diccionario_estudiante['barrio_res'] = barrio_res_obj.nombre
            estrato_obj = barrio.objects.get(codigo_barrio=barrio_res_id)
            estrato_nombre = estrato_obj.estrato
            diccionario_estrato = {'estrato': estrato_nombre}
            diccionario_estudiante.update(diccionario_estrato)
        except barrio.DoesNotExist:
            diccionario_estudiante['barrio_res'] = None
        #municipio_nac          municipio_ini          municipio_res
        municipio_nac_id = diccionario_estudiante['ciudad_nac']
        municipio_ini_id = diccionario_estudiante['ciudad_ini']
        municipio_res_id = diccionario_estudiante['ciudad_res']
        try:
            municipio_nac_obj = municipio.objects.get(codigo_divipola=municipio_nac_id)
            diccionario_estudiante['ciudad_nac'] = municipio_nac_obj.nombre
        except municipio.DoesNotExist:
            diccionario_estudiante['ciudad_nac'] = None
        try:
            municipio_ini_obj = municipio.objects.get(codigo_divipola=municipio_ini_id)
            diccionario_estudiante['ciudad_ini'] = municipio_ini_obj.nombre
        except municipio.DoesNotExist:
            diccionario_estudiante['ciudad_ini'] = None
        try:
            municipio_res_obj = municipio.objects.get(codigo_divipola=municipio_res_id)
            diccionario_estudiante['ciudad_res'] = municipio_res_obj.nombre
        except municipio.DoesNotExist:
            diccionario_estudiante['ciudad_res'] = None
        #cond_excepcion          discap_men
        cond_excepcion_id = diccionario_estudiante['id_cond_excepcion']
        discap_men_id = diccionario_estudiante['id_discapacidad']
        # diccionarion_cond_excepcion = {'el_id_de_cond_excepcion':cond_excepcion_id}
        try:
            cond_excepcion_obj = cond_excepcion.objects.get(id=cond_excepcion_id)
            # diccionario_estudiante['id_cond_excepcion'] = cond_excepcion_obj.alias
            diccionarion_cond_excepcion = {'el_id_de_cond_excepcion':cond_excepcion_obj.alias}
            diccionario_estudiante.update(diccionarion_cond_excepcion)
        except cond_excepcion.DoesNotExist:
            diccionario_estudiante['id_cond_excepcion'] = None
        try:
            discap_men_obj = discap_men.objects.get(codigo_men=discap_men_id)
            diccionario_estudiante['id_discapacidad'] = discap_men_obj.nombre
        except discap_men.DoesNotExist:
            diccionario_estudiante['id_discapacidad'] = None
        #identidad_gen          etnia       estado_civil        act_simultanea
        identidad_gen_id = diccionario_estudiante['id_identidad_gen']
        etnia_id = diccionario_estudiante['id_etnia']
        estado_civil_id = diccionario_estudiante['id_estado_civil']
        act_simultanea_id = diccionario_estudiante['id_act_simultanea']
        # diccionarion_identidad_gen = {'el_id_de_identidad_gen':identidad_gen_id}
        # diccionarion_etnia = {'el_id_de_etnia':etnia_id}
        # diccionarion_estado_civil = {'el_id_de_estado_civil':estado_civil_id}
        # diccionarion_act_simultanea = {'el_id_de_act_simultanea':act_simultanea_id}
        try:
            identidad_gen_obj = identidad_gen.objects.get(opcion_general=identidad_gen_id)
            # diccionario_estudiante['id_identidad_gen'] = identidad_gen_obj.genero
            diccionarion_identidad_gen = {'el_id_de_identidad_gen':identidad_gen_obj.genero}
            diccionario_estudiante.update(diccionarion_identidad_gen)
        except identidad_gen.DoesNotExist:
            diccionario_estudiante['id_identidad_gen'] = None
        try:
            etnia_obj = etnia.objects.get(opcion_general=etnia_id)
            # diccionario_estudiante['id_etnia'] = etnia_obj.etnia
            diccionarion_etnia = {'el_id_de_etnia':etnia_obj.etnia}
            diccionario_estudiante.update(diccionarion_etnia)
        except etnia.DoesNotExist:
            diccionario_estudiante['id_etnia'] = None
        try:
            estado_civil_obj = estado_civil.objects.get(id=estado_civil_id)
            # diccionario_estudiante['id_estado_civil'] = estado_civil_obj.estado_civil
            diccionarion_estado_civil = {'el_id_de_estado_civil':estado_civil_obj.estado_civil}
            diccionario_estudiante.update(diccionarion_estado_civil)
        except estado_civil.DoesNotExist:
            diccionario_estudiante['id_estado_civil'] = None
        try:
            act_simultanea_obj = act_simultanea.objects.get(opcion_general=act_simultanea_id)
            # diccionario_estudiante['id_act_simultanea'] = act_simultanea_obj.actividad
            diccionarion_act_simultanea = {'el_id_de_act_simultanea':act_simultanea_obj.actividad}
            diccionario_estudiante.update(diccionarion_act_simultanea)
        except act_simultanea.DoesNotExist:
            diccionario_estudiante['id_act_simultanea'] = None
        programas = programa_estudiante.objects.filter(id_estudiante=serializer_estudiante.data['id']).values()
        lista_programas = []
        for i in programas:
            var_programa = programa.objects.filter(id=i['id_programa_id']).values()
            dic_programa = {'nombre_programa': var_programa[0]['nombre'], 'cod_univalle': var_programa[0]['codigo_univalle']}
            dic = i
            dic.update(dic_programa)
            lista_programas.append(dic)
        diccionario_programas = {'programas': lista_programas}

        diccionario_estudiante.update(diccionario_programas)

        try:
            semestre_activo = semestre.objects.get(semestre_actual=True)
            serializer_semestre = semestre_serializer(semestre_activo)
            el_monitor_asignado = asignacion.objects.get(id_semestre=serializer_semestre.data['id'], id_estudiante=pk)
            serializer_monitor_asignado = asignacion_serializer(el_monitor_asignado)

            info_monitor = usuario_rol.objects.get(id_usuario = serializer_monitor_asignado.data['id_usuario'], id_semestre=serializer_semestre.data['id'])

            serilalizer_info_monitor = usuario_rol_serializer(info_monitor)

            su_practicante = usuario_rol.objects.get(id_usuario=serilalizer_info_monitor.data['id_jefe'], id_semestre=serializer_semestre.data['id'])
            serializer_su_practicante = usuario_rol_serializer(su_practicante)

            su_profesional = usuario_rol.objects.get(id_usuario=serializer_su_practicante.data['id_jefe'], id_semestre=serializer_semestre.data['id'])
            serializer_su_profesional = usuario_rol_serializer(su_profesional)

            consulta_practicante = User.objects.get(id =serializer_su_practicante.data['id_usuario'])
            serializer_practicante = user_selected(consulta_practicante)

            consulta_profesional = User.objects.get(id =serializer_su_profesional.data['id_usuario'])
            serializer_profesional = user_selected(consulta_profesional)

            consulta_monitor = User.objects.get(id =serilalizer_info_monitor.data['id_usuario'])
            serializer_monitor = user_selected(consulta_monitor)

            datos_encargados = {
                    'profesional': serializer_profesional.data, 
                    'practicante': serializer_practicante.data,
                    'info_monitor': serializer_monitor.data
                    }
        except:
            datos_encargados = {
                    'profesional': 'sin asignacion', 
                    'practicante': 'sin asignacion',
                    'info_monitor': 'sin asignacion'
                    }

        diccionario_estudiante.update(datos_encargados)

        return Response(diccionario_estudiante)








class rol_viewsets (viewsets.ModelViewSet):
    serializer_class = rol_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = rol_serializer.Meta.model.objects.all()



class profesional_viewsets (viewsets.ModelViewSet):
    serializer_class = usuario_rol_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = usuario_rol_serializer.Meta.model.objects.all()

    def list(self, request):
        list_profesional = []

        val_rol = rol.objects.get(nombre = 'Profesional')
        serializer_rol= rol_serializer(val_rol)
        id_rol_profesional = serializer_rol.data['id']

        consulta_id_profesional = list(usuario_rol.objects.filter(id_rol = id_rol_profesional,estado = 'ACTIVO'))
        for i in consulta_id_profesional:
            serializer_usuario_rol =usuario_rol_serializer(i)
            consulta_profesional= User.objects.get(id =serializer_usuario_rol.data['id_usuario'])
            serializer_profesional= user_selected(consulta_profesional)
            list_profesional.append(serializer_profesional.data)

        return Response(list_profesional,status=status.HTTP_200_OK)

class practicante_viewsets (viewsets.ModelViewSet):
    serializer_class = usuario_rol_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = usuario_rol_serializer.Meta.model.objects.all()

    def list(self, request):
        list_practicante = []

        val_rol = rol.objects.get(nombre = 'Practicante')
        id_rol_practicante = (rol_serializer(val_rol)).data['id']

        consulta_id_practicante = list(usuario_rol.objects.filter(id_rol = id_rol_practicante,estado = 'ACTIVO'))
        for i in consulta_id_practicante:
            serializer_usuario_rol =usuario_rol_serializer(i)
            consulta_practicante = User.objects.get(id =serializer_usuario_rol.data['id_usuario'])
            serializer_practicante= user_selected(consulta_practicante)
            list_practicante.append(serializer_practicante.data)

        return Response(list_practicante,status=status.HTTP_200_OK)


    def retrieve(self, request, pk):
        list_practicante = []
        list_practicante_selected = []

        val_rol = rol.objects.get(nombre = 'Practicante')
        id_rol_practicante = (rol_serializer(val_rol)).data['id']

        consulta_id_practicante = list(usuario_rol.objects.filter(id_rol = id_rol_practicante,estado = 'ACTIVO'))
        for i in consulta_id_practicante:
            serializer_usuario_rol =usuario_rol_serializer(i)
            consulta_practicante = User.objects.get(id =serializer_usuario_rol.data['id_usuario'])
            serializer_practicante = user_selected(consulta_practicante)
            list_practicante.append(serializer_practicante.data)

        consulta_id_practicante_selected = list(usuario_rol.objects.filter(id_jefe = pk, id_rol = id_rol_practicante))

        for i in consulta_id_practicante_selected:
            serializer_usuario_rol_selected =usuario_rol_serializer(i)
            consulta_practicante_selected  = User.objects.get(id =serializer_usuario_rol_selected.data['id_usuario'])
            serializer_practicante_selected  = user_selected(consulta_practicante_selected )
            list_practicante_selected.append(serializer_practicante_selected.data)
            for i in list_practicante:
                if i['id'] == serializer_practicante_selected.data['id']:
                    list_practicante.remove(i)

        datos = [list_practicante_selected,list_practicante]
        return Response(datos,status=status.HTTP_200_OK)

class monitor_viewsets (viewsets.ModelViewSet):
    serializer_class = usuario_rol_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = usuario_rol_serializer.Meta.model.objects.all()

    def list(self, request):
        list_monitores = []

        val_rol = rol.objects.get(nombre = 'monitor')
        id_rol_monitor = (rol_serializer(val_rol)).data['id']
        consulta_id_monitores = list(usuario_rol.objects.filter(id_rol = id_rol_monitor,estado = 'ACTIVO'))
        print(consulta_id_monitores)
        for i in consulta_id_monitores:
            serializer_usuario_rol =usuario_rol_serializer(i)
            consulta_monitor = User.objects.get(id =serializer_usuario_rol.data['id_usuario'])
            serializer_monitor = user_selected(consulta_monitor)
            list_monitores.append(serializer_monitor.data)

        return Response(list_monitores,status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        list_monitores = []
        list_monitores_selected = []
        
        val_rol = rol.objects.get(nombre = 'monitor')
        id_rol_monitor = (rol_serializer(val_rol)).data['id']

        consulta_id_monitores = list(usuario_rol.objects.filter(id_rol = id_rol_monitor,estado = 'ACTIVO'))
        for i in consulta_id_monitores:
            serializer_usuario_rol =usuario_rol_serializer(i)
            consulta_monitor = User.objects.get(id =serializer_usuario_rol.data['id_usuario'])
            serializer_monitor = user_selected(consulta_monitor)
            list_monitores.append(serializer_monitor.data)

        consulta_id_monitores_selected = list(usuario_rol.objects.filter(id_jefe = pk, id_rol = id_rol_monitor))

        for i in consulta_id_monitores_selected:
            serializer_usuario_rol_selected =usuario_rol_serializer(i)
            consulta_monitor_selected  = User.objects.get(id =serializer_usuario_rol_selected.data['id_usuario'])
            serializer_monitor_selected  = user_selected(consulta_monitor_selected )
            list_monitores_selected.append(serializer_monitor_selected.data)
            for i in list_monitores:
                if i['id'] == serializer_monitor_selected.data['id']:
                    list_monitores.remove(i)
        datos = [list_monitores_selected,list_monitores]
        return Response(datos,status=status.HTTP_200_OK)

class estudiante_selected_viewsets (viewsets.ModelViewSet):
    serializer_class = usuario_rol_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = usuario_rol_serializer.Meta.model.objects.all()

    def list(self, request):
        list_estudiantes = []

        list_all_estudiantes = list(estudiante.objects.all())
        for i in list_all_estudiantes: 
            serializer_estudiante =estudiante_serializer(i)
            list_estudiantes.append(serializer_estudiante.data)

        return Response(list_estudiantes,status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        list_estudiantes = []
        list_estudiantes_selected = []

        consulta_estudiantes = list(estudiante.objects.all())
        for i in consulta_estudiantes: 
            serializer_estudiante =estudiante_serializer(i)
            list_estudiantes.append(serializer_estudiante.data)

        lista_asignacion = list(asignacion.objects.filter(id_usuario = pk, estado=True))

        for i in lista_asignacion:
            serializer_asignacion =asignacion_serializer(i)
            estudiante_selected =estudiante.objects.get(id = serializer_asignacion.data['id_estudiante']) 
            serializer_estudiante =estudiante_serializer(estudiante_selected)
            list_estudiantes_selected.append(serializer_estudiante.data)
            for i in list_estudiantes:
                if i['id'] == serializer_estudiante.data['id']:
                    list_estudiantes.remove(i)

        datos = [list_estudiantes_selected,list_estudiantes]
        return Response(datos,status=status.HTTP_200_OK)



class usuario_rol_viewsets (viewsets.ModelViewSet):
    serializer_class = usuario_rol_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = usuario_rol_serializer.Meta.model.objects.all()
    

    def list(self, request):
        list_user_rol = list()
        var_semestre = get_object_or_404(semestre, semestre_actual = True)
        for user_rol in usuario_rol.objects.filter(id_semestre =var_semestre.id, estado = "ACTIVO").values():
            rols= rol.objects.filter(id =user_rol['id_rol_id']).annotate(id_rol=F('id')).values('id_rol','nombre')[0]
            usuarios= User.objects.filter(id =user_rol['id_usuario_id']).values('id','username','first_name','last_name', 'email')[0]
            usuarios.update(rols)
            list_user_rol.append(usuarios)

        
        return Response (list_user_rol)

    def retrieve(self, request, pk=None):
        try:
            var_semestre = get_object_or_404(semestre, semestre_actual = True)
            var_user_rol =usuario_rol.objects.get(id_usuario=pk,id_semestre =var_semestre.id,estado = "ACTIVO")
            serializer_user_rol= usuario_rol_serializer(var_user_rol)
            var_rol = rol.objects.get(id =serializer_user_rol.data['id_rol'])
            serializer_rol= rol_serializer(var_rol)
            return Response(serializer_rol.data['nombre'])
        except:
            return Response(
            {'mensaje':'Este usuario no tiene rol.'},
            status=status.HTTP_404_NOT_FOUND
            )



    def update(self, request, pk=None):
        # serializer = self.serializer_class(data=request.data)
        # print('esta es la info: '+ str(request.data))
        # if (serializer.is_valid()):
            var_usuario =User.objects.get(id=pk)
            serializer_usuario= user_serializer(var_usuario)
            var_semestre =semestre.objects.get(semestre_actual = True)
            serializer_semestre= semestre_serializer(var_semestre)
            print(serializer_usuario.data['id'])
            print(serializer_semestre.data['id'])

            # try:
            var_old_user_rol = usuario_rol.objects.get(id_usuario = serializer_usuario.data['id'],  id_semestre = serializer_semestre.data['id'],estado = 'ACTIVO')

            # except:
            #     return Response(
            #     status=status.HTTP_404_NOT_FOUND
            #     )

            var_user_rol= var_old_user_rol
            var_user_rol.estado = "INACTIVO"
            var_user_rol.save()

            return Response({'Respuesta': 'True'},status=status.HTTP_200_OK)

    def create(self, request,pk=None):
        serializer = self.serializer_class(data=request.data)
        if (serializer.is_valid()):
            id_user_request = serializer.data['id_usuario']
            id_rol_request = serializer.data['id_rol']

            var_usuario = get_object_or_404(User, id = id_user_request)
            var_rol = get_object_or_404(rol, id = id_rol_request)
            var_semestre = get_object_or_404(semestre, semestre_actual = True)

            try:
                var_old_user_rol = get_object_or_404(usuario_rol, id_usuario = var_usuario,  id_semestre = var_semestre)
            except:
                var_old_user_rol = Empty
            # print(var_semestre.id)
            # print(var_old_user_rol.id_semestre)
            # print(var_semestre.id)
            # print(var_old_user_rol.estado)
            if(var_old_user_rol != Empty and var_old_user_rol.estado == "ACTIVO"):
                print("entre a 1")
                var_user_rol= var_old_user_rol
                var_user_rol.id_usuario= var_usuario
                var_user_rol.id_rol = var_rol
                var_user_rol.id_semestre = var_semestre
                var_user_rol.save()
            elif(var_old_user_rol == Empty) :
                print("entre a 2")
                var_user_rol= usuario_rol()
                var_user_rol.id_usuario= var_usuario
                var_user_rol.id_rol = var_rol
                var_user_rol.id_semestre = var_semestre
                var_user_rol.save()
            elif(var_old_user_rol != Empty and var_old_user_rol.estado == "INACTIVO"):
                print("entre a 3")
                var_user_rol= var_old_user_rol
                var_user_rol.id_usuario= var_usuario
                var_user_rol.id_rol = var_rol
                var_user_rol.estado = "ACTIVO"
                var_user_rol.id_semestre = var_semestre
                var_user_rol.save()
            else:
                Response(
                    serializer.errors,
                    status=status.HTTP_406_NOT_ACCEPTABLE
                )


            return Response({'Respuesta': 'User_rol creado o modificado satisfactoriamente.'},status=status.HTTP_200_OK)

        return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class usuario_rol_old_viewsets (viewsets.ModelViewSet):
    serializer_class = usuario_rol_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = usuario_rol_serializer.Meta.model.objects.all()
    

    def list(self, request):
        list_user_rol = list()
        var_semestre = semestre.objects.filter(semestre_actual = False).order_by('-fecha_inicio').first()
        print(var_semestre.nombre)
        for user_rol in usuario_rol.objects.filter(id_semestre =var_semestre.id, estado = "ACTIVO").values():
            rols= rol.objects.filter(id =user_rol['id_rol_id']).annotate(id_rol=F('id')).values('id_rol','nombre')[0]
            usuarios= User.objects.filter(id =user_rol['id_usuario_id']).values('id','username','first_name','last_name', 'email')[0]
            usuarios.update(rols)
            list_user_rol.append(usuarios)
        return Response(list_user_rol)
        














class user_actualizacion_viewsets(viewsets.ViewSet):
    serializer_class = user_actualizacion

    def update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            first_name_request = serializer.validated_data['first_name']
            last_name_request = serializer.validated_data['last_name']
            print('entra al calid')
            print(first_name_request)
            print(last_name_request)
            try:
                user = User.objects.get(pk=pk)
                user.first_name = first_name_request
                user.last_name = last_name_request
                user.save()

                return Response({'Respuesta': 'True'}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'Respuesta': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











class estudiante_actualizacion_viewsets (viewsets.ModelViewSet):
    serializer_class = Estudiante_actualizacion
    queryset = estudiante_serializer.Meta.model.objects.all()

    def post(self, request, pk=None):
        # serializer = self.serializer_class(data=request.data)
        # print('esta es la info: '+ str(request.data))
        # if (serializer.is_valid()):
        serializer = self.serializer_class(data=request.data)

        print('este es jajaja : ' + str(serializer))
        if serializer.is_valid():

            puntaje_icfes_request = serializer.data['puntaje_icfes']
            telefono_res_request = serializer.data['telefono_res']
            celular_request = serializer.data['celular']
            email_request = serializer.data['email']
            sexo_request = serializer.data['sexo']
            cantidad_hijo_request = serializer.data['hijos']
            deporte_request = serializer.data['actividades_ocio_deporte']
            acudiente_emergencia_request = serializer.data['acudiente']
            tel_acudiente_emergencia_request = serializer.data['telefono_acudiente']

            etnia_request = serializer.data['id_etnia']
            act_simultanea_request = serializer.data['id_act_simultanea']
            identidad_gen_request = serializer.data['id_identidad_gen']
            estado_civil_request = serializer.data['id_estado_civil']
            cond_excepcion_request = serializer.data['id_cond_excepcion']

            var_estudiante = estudiante.objects.get(id=pk)
            serializer_estudiante = estudiante_serializer(var_estudiante)

            try:
                var_old_estudiante = estudiante.objects.get(pk = serializer_estudiante.data['id'])
                var_estudiante = var_old_estudiante

                var_estudiante.puntaje_icfes = puntaje_icfes_request
                var_estudiante.telefono_res = telefono_res_request
                var_estudiante.celular = celular_request
                var_estudiante.email = email_request
                var_estudiante.sexo = sexo_request
                var_estudiante.actividades_ocio_deporte = deporte_request
                var_estudiante.hijos = cantidad_hijo_request
                var_estudiante.acudiente = acudiente_emergencia_request
                var_estudiante.telefono_acudiente = tel_acudiente_emergencia_request

                try:
                    etnia_obj = etnia.objects.get(id=etnia_request)
                    var_estudiante.id_etnia = etnia_obj
                except:
                    print('no hiz etnia')

                try:
                    act_simultanea_obj = act_simultanea.objects.get(id=act_simultanea_request)
                    var_estudiante.id_act_simultanea = act_simultanea_obj
                except:
                    print('no hiz act_simultanea')

                try:
                    identidad_gen_obj = identidad_gen.objects.get(id=identidad_gen_request)
                    var_estudiante.id_identidad_gen = identidad_gen_obj
                except:
                    print('no hiz identidad_gen')

                try:
                    estado_civil_obj = estado_civil.objects.get(id=estado_civil_request)
                    var_estudiante.id_estado_civil = estado_civil_obj
                except:
                    print('no hiz estado_civil')

                try:
                    cond_excepcion_obj = cond_excepcion.objects.get(id=cond_excepcion_request)
                    var_estudiante.id_cond_excepcion = cond_excepcion_obj
                except:
                    print('no hiz cond_excepcion')



                
                # etnia_obj = etnia.objects.get(id=etnia_request)
                # var_estudiante.id_etnia = etnia_obj

                # act_simultanea_obj = act_simultanea.objects.get(id=act_simultanea_request)
                # var_estudiante.id_act_simultanea = act_simultanea_obj

                # identidad_gen_obj = identidad_gen.objects.get(id=identidad_gen_request)
                # var_estudiante.id_identidad_gen = identidad_gen_obj

                # estado_civil_obj = estado_civil.objects.get(id=estado_civil_request)
                # var_estudiante.id_estado_civil = estado_civil_obj

                # cond_excepcion_obj = cond_excepcion.objects.get(id=cond_excepcion_request)
                # var_estudiante.id_cond_excepcion = cond_excepcion_obj

                var_estudiante.save()
                return Response({'Respuesta': 'True'},status=status.HTTP_200_OK)
            except estudiante.DoesNotExist:
                print('primer print')
                return Response({'Respuesta': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        print('segundo print')
        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Grupo_etnico_viewsets(viewsets.ModelViewSet):
    serializer_class = Grupo_etnico_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = etnia.objects.all()

    def list(self, request):
        try:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Actividad_simultanea_viewsets(viewsets.ModelViewSet):
    serializer_class = Actividad_simultanea_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = act_simultanea.objects.all()

    def list(self, request):
        try:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Identidad_gen_viewsets(viewsets.ModelViewSet):
    serializer_class = Identidad_de_genero_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = identidad_gen.objects.all()

    def list(self, request):
        try:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Estado_civil_viewsets(viewsets.ModelViewSet):
    serializer_class = Estado_civil_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = estado_civil.objects.all()

    def list(self, request):
        try:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Condicion_de_excepcion_viewsets(viewsets.ModelViewSet):
    serializer_class = Condicion_de_excepcion_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = cond_excepcion.objects.all()

    def list(self, request):
        try:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






class ids_estudiantes_del_monitor_viewsets(viewsets.ModelViewSet):
    serializer_class = usuario_rol_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = usuario_rol_serializer.Meta.model.objects.all()

    def retrieve(self, request, pk):
        # Obtener el ID del monitor desde el front-end
        id_monitor = pk

        # Filtrar los registros de usuario_rol para obtener los estudiantes del monitor específico
        estudiantes_monitor = usuario_rol.objects.filter(id_usuario=id_monitor).values_list('id_estudiante', flat=True)

        # Convertir el resultado en una lista
        lista_estudiantes = list(estudiantes_monitor)

        return Response(lista_estudiantes, status=status.HTTP_200_OK)


class info_estudiantes_sin_seguimientos_viewsets(viewsets.ModelViewSet):
    serializer_class = usuario_rol_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = usuario_rol_serializer.Meta.model.objects.all()

    def retrieve(self, request, pk):
        list_total_datos = []

        list_estudiantes = []

        list_inasistencia = []
        list_seguimientos = []

        id = '',
        cedula = '',
        nombres = '',
        apellidos = '',
        practicante = '',
        profesional = '',

        list_semestre = list(semestre.objects.all().filter(semestre_actual = True))
        # Realiza la lista de estudiantes y los serializa
        consulta_estudiantes = list(estudiante.objects.all())

        for i in consulta_estudiantes: 
            serializer_estudiante =estudiante_serializer(i)
            list_estudiantes.append(serializer_estudiante.data)

        # Serializa el id del profesional
        val_rol_profesional = rol.objects.get(nombre = 'Profesional')
        serializer_rol= rol_serializer(val_rol_profesional)
        id_rol_profesional = serializer_rol.data['id']

        # Serializa el id del practicante
        val_rol_practicante = rol.objects.get(nombre = 'Practicante')
        id_rol_practicante = (rol_serializer(val_rol_practicante)).data['id']

        # Serializa el id del monitor
        val_rol_monitor = rol.objects.get(nombre = 'monitor')
        id_rol_monitor = (rol_serializer(val_rol_monitor)).data['id']

        consulta_id_profesional = list(usuario_rol.objects.filter(id_rol = id_rol_profesional, id_semestre=pk))
        
        for i in consulta_id_profesional:
            print('entra a los profesionales, son :' + str(consulta_id_profesional))
            serializer_usuario_rol = usuario_rol_serializer(i)
            consulta_profesional = User.objects.get(id =serializer_usuario_rol.data['id_usuario'])
            serializer_profesional = user_selected(consulta_profesional)
            # profesional = serializer_profesional.data['first_name']
            profesional = f"{serializer_profesional.data['first_name']} {serializer_profesional.data['last_name']}"

            consulta_id_practicante_selected = list(usuario_rol.objects.filter(id_semestre=pk, id_jefe = serializer_profesional.data['id'], id_rol = id_rol_practicante))

            for j in consulta_id_practicante_selected:
                print('entra a los practicantes, son :' + str(consulta_id_practicante_selected))
                serializer_usuario_rol_selected =usuario_rol_serializer(j)
                consulta_practicante_selected  = User.objects.get(id = serializer_usuario_rol_selected.data['id_usuario'])
                serializer_practicante_selected  = user_selected(consulta_practicante_selected )
                practicante = f"{serializer_practicante_selected.data['first_name']} {serializer_practicante_selected.data['last_name']}"

                consulta_id_monitores_selected = list(usuario_rol.objects.filter(id_semestre=pk, id_jefe = serializer_practicante_selected.data['id'], id_rol = id_rol_monitor))

                for k in consulta_id_monitores_selected:
                    print('entra a los monitores, son :' + str(consulta_id_monitores_selected))
                    serializer_usuario_rol_selected =usuario_rol_serializer(k)
                    consulta_monitor_selected  = User.objects.get(id =serializer_usuario_rol_selected.data['id_usuario'])
                    serializer_monitor_selected  = user_selected(consulta_monitor_selected )
                    # monitor = serializer_monitor_selected.data['first_name']
                    monitor = f"{serializer_monitor_selected.data['first_name']} {serializer_monitor_selected.data['last_name']}"

                    lista_asignacion = list(asignacion.objects.filter(id_usuario = serializer_monitor_selected.data['id'], estado=True, id_semestre=pk))

                    for l in lista_asignacion:
                        print('entra a los estudiantes, son :' + str(lista_asignacion))
                        serializer_asignacion =asignacion_serializer(l)
                        estudiante_selected =estudiante.objects.get(id = serializer_asignacion.data['id_estudiante']) 
                        serializer_estudiante =estudiante_serializer(estudiante_selected)
                        id = serializer_estudiante.data['id']
                        cedula = serializer_estudiante.data['num_doc']
                        nombres = serializer_estudiante.data['nombre']
                        apellidos = serializer_estudiante.data['apellido']
                        print('datos estudiante : ')
                        print(id)

                        list_seguimientos_individual = list(seguimiento_individual.objects.filter(id_estudiante = id))
                        list_inasistencia_individual = list(inasistencia.objects.filter(id_estudiante = id))

                        for i in list_inasistencia_individual: 
                            serializer_inasistencia =inasistencia_serializer(i)
                            list_inasistencia.append(serializer_inasistencia.data)
                        for i in list_seguimientos_individual: 
                            serializer_seguimiento_individual =seguimiento_individual_serializer(i)
                            list_seguimientos.append(serializer_seguimiento_individual.data)

                        for m in list_semestre:
                            lista_inasistencia = []
                            lista_seguimientos = []

                            serializer_semestre =semestre_serializer(m)

                            for j in list_inasistencia:
                                if j['fecha'] > serializer_semestre.data['fecha_inicio'] and j['fecha'] < serializer_semestre.data['fecha_fin']:
                                    lista_inasistencia.append(j)        

                            for j in list_seguimientos:
                                if j['fecha'] > serializer_semestre.data['fecha_inicio'] and j['fecha'] < serializer_semestre.data['fecha_fin']:
                                    lista_seguimientos.append(j)

                            count_inasistencias = len(lista_inasistencia)
                            count_seguimientos = len(lista_seguimientos)
                            count_total_fichas = count_inasistencias + count_seguimientos

                            datos = {
                                'id': id,
                                'cedula': cedula,
                                'nombres': nombres,
                                'apellidos': apellidos,
                                'cantidad_de_fichas': count_seguimientos,
                                'cantidad_de_inasistencias': count_inasistencias,
                                'total_fichas': count_total_fichas,
                                'monitor': monitor,
                                'practicante': practicante,
                                'profesional': profesional,
                                }

                            list_total_datos.append(datos)

        return Response(list_total_datos,status=status.HTTP_200_OK)




class ultimo_seguimiento_individual_ViewSet(viewsets.ModelViewSet):
    serializer_class = seguimiento_individual_serializer
    # permission_classes = (IsAuthenticated,)
    queryset =  seguimiento_individual_serializer.Meta.model.objects.all()
    print('que pasaaaaaa 1qqqe')

    def list(self, request):
        estudiante_id = request.query_params.get('estudiante_id')

        try:
            # Obtener el seguimiento más reciente del estudiante especificado
            seguimiento_reciente = seguimiento_individual.objects.filter(id_estudiante=estudiante_id).latest('fecha')

            # Crear un diccionario con los datos de riesgo del seguimiento
            riesgo = {
                'riesgo_individual': seguimiento_reciente.riesgo_individual,
                'riesgo_familiar': seguimiento_reciente.riesgo_familiar,
                'riesgo_academico': seguimiento_reciente.riesgo_academico,
                'riesgo_economico': seguimiento_reciente.riesgo_economico,
                'riesgo_vida_universitaria_ciudad': seguimiento_reciente.riesgo_vida_universitaria_ciudad
            }
            print('que pasaaaaaa')
            # Devolver el riesgo en la respuesta
            return Response(riesgo)
        except seguimiento_individual.DoesNotExist:
            # Si no se encuentra ningún seguimiento para el estudiante especificado, devolver una respuesta vacía
            return Response({})




# class ultimo_seguimiento_individual_ViewSet (viewsets.ModelViewSet):
#     serializer_class = seguimiento_individual_serializer
#     # permission_classes = (IsAuthenticated,)
#     queryset = seguimiento_individual_serializer.Meta.model.objects.all()

#     def retrieve(self, request, pk=None):

#         seguimiento_reciente = seguimiento_individual.objects.filter(id_estudiante=pk).latest('fecha')

#         list_seguimientos_individual = list(seguimiento_individual.objects.filter(id_estudiante = pk))
    

#         riesgo = {
#             'riesgo_individual': seguimiento_reciente.riesgo_individual,
#             'riesgo_familiar': seguimiento_reciente.riesgo_familiar,
#             'riesgo_academico': seguimiento_reciente.riesgo_academico,
#             'riesgo_economico': seguimiento_reciente.riesgo_economico,
#             'riesgo_vida_universitaria_ciudad': seguimiento_reciente.riesgo_vida_universitaria_ciudad
#             }

#         return Response(riesgo,status=status.HTTP_200_OK)






class reporte_seguimientos_viewsets (viewsets.ModelViewSet):
    serializer_class = usuario_rol_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = usuario_rol_serializer.Meta.model.objects.all()

    def retrieve(self, request, pk):
        list_practicante = []
        list_practicante_selected = []
        list_monitor_selected = []
        list_estudiante_selected = []
        total_estudiantes = 0

        val_rol = rol.objects.get(nombre = 'Practicante')
        id_rol_practicante = (rol_serializer(val_rol)).data['id']

        # seteo del semestre a analizar
        list_semestre = list(semestre.objects.all().filter(semestre_actual = True))
        serializer_semestre = semestre_serializer(list_semestre[0])

        consulta_id_practicante = list(usuario_rol.objects.filter(id_rol = id_rol_practicante,estado = 'ACTIVO'))
        for i in consulta_id_practicante:
            serializer_usuario_rol =usuario_rol_serializer(i)
            consulta_practicante = User.objects.get(id =serializer_usuario_rol.data['id_usuario'])
            serializer_practicante = user_selected(consulta_practicante)
            list_practicante.append(serializer_practicante.data)

        consulta_id_practicante_selected = list(usuario_rol.objects.filter(id_jefe = pk, id_rol = id_rol_practicante))

        for i in consulta_id_practicante_selected:
            serializer_usuario_rol_selected =usuario_rol_serializer(i)
            consulta_practicante_selected  = User.objects.get(id =serializer_usuario_rol_selected.data['id_usuario'])
            serializer_practicante_selected  = user_selected(consulta_practicante_selected )

            list_monitores_selected = []
            
            val_rol = rol.objects.get(nombre = 'monitor')
            id_rol_monitor = (rol_serializer(val_rol)).data['id']

            consulta_id_monitores_selected = list(usuario_rol.objects.filter(id_jefe = serializer_practicante_selected.data['id'], id_rol = id_rol_monitor))
            total_estudiantes = 0
            list_monitor_selected =[]
            #reinicio_conteo proacticante
            practicante_list_inasistencia=0
            practicante_list_seguimientos=0
            practicante_count_seguimientos_individual_practicante= 0
            practicante_count_count_inasistencias_pendientes_profesional= 0
            practicante_count_count_seguimientos_pendientes_practicante= 0
            practicante_count_seguimientos_pendientes_profesional= 0

            for i in consulta_id_monitores_selected:
                serializer_usuario_rol_selected =usuario_rol_serializer(i)
                consulta_monitor_selected  = User.objects.get(id =serializer_usuario_rol_selected.data['id_usuario'])
                serializer_monitor_selected  = user_selected(consulta_monitor_selected )
                lista_asignacion = list(asignacion.objects.filter(id_usuario = serializer_monitor_selected.data['id'], estado=True, id_semestre=serializer_semestre.data['id']))

                print('id monitor')
                print(serializer_monitor_selected.data['id'])
                list_estudiante_selected =[]
    
                #reinicio_conteo monitor
                monitor_list_inasistencia=0
                monitor_list_seguimientos=0
                monitor_count_seguimientos_individual_practicante= 0
                monitor_count_count_inasistencias_pendientes_profesional= 0
                monitor_count_count_seguimientos_pendientes_practicante= 0
                monitor_count_seguimientos_pendientes_profesional= 0
    
    
                for i in lista_asignacion:
                    serializer_asignacion =asignacion_serializer(i)
                    estudiante_selected =estudiante.objects.get(id = serializer_asignacion.data['id_estudiante']) 
                    serializer_estudiante =estudiante_serializer(estudiante_selected)


                    fecha_inicio = datetime.strptime(serializer_semestre.data['fecha_inicio'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")
                    fecha_fin = datetime.strptime(serializer_semestre.data['fecha_fin'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")
                    print('el priiiiiiint' + str(serializer_semestre))
                    # print('id estudiante')
                    # print(serializer_estudiante.data['id'])
                    list_seguimientos_individual_practicante = seguimiento_individual.objects.filter(
                                                        id_estudiante = serializer_estudiante.data['id'],
                                                        revisado_practicante = False,
                                                        ).count()

                    list_inasistencia_individual_practicante = inasistencia.objects.filter(
                                                        id_estudiante = serializer_estudiante.data['id'], 
                                                        revisado_practicante = False,
                                                        fecha__gt = fecha_inicio,
                                                        fecha__lt =fecha_fin
                                                        ).count()

                    list_seguimientos_individual_profesional = seguimiento_individual.objects.filter(
                                                        id_estudiante = serializer_estudiante.data['id'], 
                                                        revisado_profesional = False,
                                                        fecha__gt = fecha_inicio,
                                                        fecha__lt =fecha_fin
                                                        ).count()
                    list_inasistencia_individual_profesional = inasistencia.objects.filter(
                                                        id_estudiante = serializer_estudiante.data['id'], 
                                                        revisado_profesional = False,
                                                        fecha__gt = fecha_inicio,
                                                        fecha__lt =fecha_fin
                                                        ).count()
                    list_inasistencia = inasistencia.objects.filter(
                                                        id_estudiante = serializer_estudiante.data['id'], 
                                                        fecha__gt = fecha_inicio,
                                                        fecha__lt =fecha_fin
                                                        ).count()

                    list_seguimientos = seguimiento_individual.objects.filter(
                                                        id_estudiante = serializer_estudiante.data['id'], 
                                                        fecha__gt = fecha_inicio,
                                                        fecha__lt =fecha_fin
                                                        ).count()
                    
                    # for i in list_inasistencia_individual: 
                    #     serializer_inasistencia =inasistencia_serializer(i)
                    #     list_inasistencia.append(serializer_inasistencia.data)

                    # count_inasistencias = len(list_inasistencia)
                    # count_seguimientos =len(list_seguimientos)
                    counts = {
                        'cantidad_seguimientos':{
                            'count_inasistencias': list_inasistencia,
                            'count_seguimientos': list_seguimientos,
                            'count_seguimientos_individual_practicante': list_seguimientos_individual_practicante,
                            'count_inasistencias_pendientes_profesional': list_seguimientos_individual_profesional,
                            'count_seguimientos_pendientes_practicante': list_inasistencia_individual_practicante,
                            'count_seguimientos_pendientes_profesional': list_inasistencia_individual_profesional,
                            }
                    }
                    data_estudiantes = dict(serializer_estudiante.data, **counts)

                    # conteos del monitor
                    monitor_list_inasistencia+=list_inasistencia
                    monitor_list_seguimientos+=list_seguimientos
                    monitor_count_seguimientos_individual_practicante+=list_seguimientos_individual_practicante
                    monitor_count_count_inasistencias_pendientes_profesional+=list_seguimientos_individual_profesional
                    monitor_count_count_seguimientos_pendientes_practicante+=list_inasistencia_individual_practicante
                    monitor_count_seguimientos_pendientes_profesional+=list_inasistencia_individual_profesional
                    #conteos practicante
                    practicante_list_inasistencia+=list_inasistencia
                    practicante_list_seguimientos+=list_seguimientos
                    practicante_count_seguimientos_individual_practicante+=list_seguimientos_individual_practicante
                    practicante_count_count_inasistencias_pendientes_profesional+=list_seguimientos_individual_profesional
                    practicante_count_count_seguimientos_pendientes_practicante+=list_inasistencia_individual_practicante
                    practicante_count_seguimientos_pendientes_profesional+=list_inasistencia_individual_profesional
                    
                    list_estudiante_selected.append(data_estudiantes)


                diccionario_cantidad_reportes_monitor = {'tipo_usuario': 'monitor',
                            'cantidad_estudiantes': len(list_estudiante_selected),
                            'cantidad_reportes' : {
                                    "count_inasistencias":monitor_list_inasistencia,
                                    "count_seguimientos":monitor_list_seguimientos,
                                    'count_inasistencias_pendientes_practicante': monitor_count_seguimientos_individual_practicante, 
                                    'count_inasistencias_pendientes_profesional': monitor_count_count_inasistencias_pendientes_profesional,
                                    'count_seguimientos_pendientes_practicante': monitor_count_count_seguimientos_pendientes_practicante, 
                                    'count_seguimientos_pendientes_profesional': monitor_count_seguimientos_pendientes_profesional,
                                  },'estudiantes_del_monitor':list_estudiante_selected,
                            }

                data_monitores = dict(serializer_monitor_selected.data, **diccionario_cantidad_reportes_monitor)



                
                list_monitor_selected.append(data_monitores)
                total_estudiantes += len(list_estudiante_selected)  # Línea añadida

            diccionario_cantidad_reportes_practicante = {'tipo_usuario': 'practicante',
                                        'cantidad_estudiantes': 0,
                                        'cantidad_reportes' : {
                                                "count_inasistencias":practicante_list_inasistencia,
                                                "count_seguimientos":practicante_list_seguimientos,
                                                'count_inasistencias_pendientes_practicante': practicante_count_seguimientos_individual_practicante, 
                                                'count_inasistencias_pendientes_profesional': practicante_count_count_inasistencias_pendientes_profesional,
                                                'count_seguimientos_pendientes_practicante': practicante_count_count_seguimientos_pendientes_practicante, 
                                                'count_seguimientos_pendientes_profesional': practicante_count_seguimientos_pendientes_profesional,
                                                },
                                        'monitores_del_practicante':list_monitor_selected,}

            data_practicantes = dict(serializer_practicante_selected.data, **diccionario_cantidad_reportes_practicante)

            data_practicantes["cantidad_estudiantes"] = total_estudiantes  # Línea añadida

            list_practicante_selected.append(data_practicantes)

        return Response(list_practicante_selected,status=status.HTTP_200_OK)





class cohortes_lista_viewsets (viewsets.ModelViewSet):
    serializer_class = cohorte_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = cohorte_serializer.Meta.model.objects.all()

    def list(self, request):
        list_final = []

        list_estudiantes_de_la_cohorte = cohorte.objects.all()
        print(list_estudiantes_de_la_cohorte)
        for i in list_estudiantes_de_la_cohorte:
            serializer_usuario_rol =cohorte_serializer(i)
            list_final.append(serializer_usuario_rol.data)

        return Response(list_final,status=status.HTTP_200_OK)



class cohorte_estudiante_info_viewsets (viewsets.ModelViewSet):
    serializer_class = cohorte_estudiante_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = cohorte_estudiante_serializer.Meta.model.objects.all()

    def list(self, request):
        list_final = []

        list_estudiantes_de_la_cohorte = cohorte_estudiante.objects.all()
        print(list_estudiantes_de_la_cohorte)
        for i in list_estudiantes_de_la_cohorte:
            serializer_usuario_rol =cohorte_estudiante_serializer(i)
            list_final.append(serializer_usuario_rol.data)

        return Response(list_final,status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        data_estudiante = []
        data_periodos = []
        result = []

        list_estudiantes_de_la_cohorte = list(cohorte_estudiante.objects.filter(id_cohorte=pk))

        for i in list_estudiantes_de_la_cohorte:
            serializer_list = cohorte_estudiante_serializer(i)
            nombre_estudiante = estudiante.objects.get(id=serializer_list.data['id_estudiante'])
            nombre = nombre_estudiante.nombre
            apellido = nombre_estudiante.apellido
            num_doc = nombre_estudiante.num_doc
            info_estudiante = {
                        'nombre' : nombre,
                        'apellido' : apellido,
                        'num_doc' : num_doc
            }
            data_estudiante.append(dict(serializer_list.data, info_estudiante=info_estudiante))

            estudiante_selected = historial_estado_programa_estudiante.objects.filter(id_estudiante=serializer_list.data['id_estudiante'])
            for j in estudiante_selected:
                serializer_estudiante = historial_estado_programa_estudiante_serializer(j)
                programa_obj = programa.objects.get(id=serializer_estudiante.data['id_programa'])
                nombre_programa = programa_obj.codigo_univalle
                
                serializer_estudiante.data['nombre_programa'] = nombre_programa
                data_periodos.append(dict(serializer_estudiante.data, nombre_programa=nombre_programa))

            data_estudiante[-1]['periodos'] = data_periodos
            result.append(data_estudiante[-1])
            data_periodos = []

        return Response(result, status=status.HTTP_200_OK)








class historial_monitor_viewsets(viewsets.ModelViewSet):
    serializer_class = asignacion_serializer
    queryset = asignacion_serializer.Meta.model.objects.all()

    def list(self, request):
        list_final = []

        val_rol = rol.objects.get(nombre='monitor')
        id_rol_monitor = (rol_serializer(val_rol)).data['id']

        info_monitor = usuario_rol.objects.filter(id_rol=id_rol_monitor)

        for i in info_monitor:
            serilalizer_info_monitor = usuario_rol_serializer(i)

            sus_estudiantes_ids = asignacion.objects.filter(id_usuario=serilalizer_info_monitor.data['id_usuario']).values_list('id_estudiante', flat=True)

            estudiantes = estudiante.objects.filter(id__in=sus_estudiantes_ids).values('nombre', 'apellido', 'cod_univalle')

            consulta_monitor = User.objects.get(id =serilalizer_info_monitor.data['id_usuario'])
            serializer_monitor = user_selected(consulta_monitor)
            
            datos_unidos = {
                            'info_monitor': serializer_monitor.data,
                            'estudiantes': estudiantes} 

            data_monitor = serilalizer_info_monitor.data.copy()  # Crear una copia del diccionario existente
            data_monitor.update(datos_unidos)  # Unir los datos

            list_final.append(data_monitor)

        return Response(list_final, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        list_final = []
       
        val_rol = rol.objects.get(nombre='monitor')
        id_rol_monitor = (rol_serializer(val_rol)).data['id']

        info_monitor = usuario_rol.objects.filter(id_rol = id_rol_monitor, id_usuario = pk)

        for i in info_monitor:
            serilalizer_info_monitor = usuario_rol_serializer(i)

            sus_estudiantes_ids = asignacion.objects.filter(id_usuario=serilalizer_info_monitor.data['id_usuario']).values_list('id_estudiante', flat=True)

            estudiantes = estudiante.objects.filter(id__in=sus_estudiantes_ids).values('nombre', 'apellido', 'cod_univalle')

            su_practicante = usuario_rol.objects.get(id_usuario=serilalizer_info_monitor.data['id_jefe'])
            serializer_su_practicante = usuario_rol_serializer(su_practicante)

            su_profesional = usuario_rol.objects.get(id_usuario=serializer_su_practicante.data['id_jefe'])
            serializer_su_profesional = usuario_rol_serializer(su_profesional)

            consulta_practicante = User.objects.get(id =serializer_su_practicante.data['id_usuario'])
            serializer_practicante = user_selected(consulta_practicante)

            consulta_profesional = User.objects.get(id =serializer_su_profesional.data['id_usuario'])
            serializer_profesional = user_selected(consulta_profesional)

            consulta_monitor = User.objects.get(id =serilalizer_info_monitor.data['id_usuario'])
            serializer_monitor = user_selected(consulta_monitor)

            datos_semestre = semestre.objects.get(id = serilalizer_info_monitor.data['id_semestre'])
            serializer_datos_semestre = semestre_serializer(datos_semestre)

            datos_unidos = {
                            'datos_semestre' : serializer_datos_semestre.data,
                            'info_monitor': serializer_monitor.data,
                            'profesional': serializer_profesional.data, 
                            'practicante': serializer_practicante.data, 
                            'estudiantes': estudiantes}  # Datos a unir

            data_monitor = serilalizer_info_monitor.data.copy()  # Crear una copia del diccionario existente
            data_monitor.update(datos_unidos)  # Unir los datos

            list_final.append(data_monitor)

        return Response(list_final, status=status.HTTP_200_OK)


# class All_user(APIView):

#     def get(self, request):
#         list_user =User.objects.all()
#         print(list_user)
#         return Response (list(list_user.values()))

# class All_user_with_rol(APIView):

#     def get(self, request):
#         list_user_rol = list()
#         var_semestre = get_object_or_404(semestre, semestre_actual = True)
#         for user_rol in usuario_rol.objects.filter(id_semestre =var_semestre.id, estado = "ACTIVO").values():
#             rols= rol.objects.filter(id =user_rol['id_rol_id']).annotate(id_rol=F('id')).values('id_rol','nombre')[0]
#             usuarios= User.objects.filter(id =user_rol['id_usuario_id']).values('id','username','first_name','last_name', 'email')[0]
#             usuarios.update(rols)
#             list_user_rol.append(usuarios)

        
#         return Response (list_user_rol)

# class All_rol(APIView):

#     def get(self, request):
#         print(request)
#         list_rol =rol.objects.all()
#         return Response (list(list_rol.values()))

# class All_estudiante(APIView):

#     def get(self, request):
#         print(request)
#         list_estudiante =estudiante.objects.all()
#         return Response (list(list_estudiante.values()))

# class Estudiante_manage(APIView):

#     serializer_class =serializers.Estudiante_manage

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if (serializer.is_valid()):

#             id_request = serializer.validated_data.get('id')
#             var_estudiante =estudiante.objects.filter(id =id_request.id).values()
#             return Response(var_estudiante[0])
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#             )

# class User_manage(APIView):

#     serializer_class =serializers.User_manage

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if (serializer.is_valid()):

#             id_request = serializer.validated_data.get('id')
#             var_usuario =User.objects.filter(id =id_request).values()
#             return Response(var_usuario[0])
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#             )

# class Rol_manage(APIView):

#     serializer_class =serializers.Rol_manage

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if (serializer.is_valid()):

#             id_request = serializer.validated_data.get('id')
#             var_rol =rol.objects.filter(id =id_request).values()
#             return Response(var_rol[0])
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#             )

# class User_rol_manage(APIView):

#     serializer_class =serializers.Rol_manage

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if (serializer.is_valid()):
#             id_user_request = serializer.validated_data.get('id')
#             var_user_rol =get_object_or_404(usuario_rol, id_usuario = id_user_request,estado = "ACTIVO")
#             id_rol = var_user_rol.id_rol.id
#             var_rol = get_object_or_404(rol, id = id_rol)
#             id_rol_result = var_rol.nombre
#             return Response(id_rol_result)
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#             )

# class delete_user_rol(APIView):
#     serializer_class =serializers.User_manage
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         print('esta es la info: '+ str(request.data))
#         if (serializer.is_valid()):
#             id_user_request = serializer.validated_data.get('id')
#             var_usuario = get_object_or_404(User, id = id_user_request)
#             var_semestre = get_object_or_404(semestre, semestre_actual = True)
#             try:
#                 var_old_user_rol = get_object_or_404(usuario_rol, id_usuario = var_usuario,  id_semestre = var_semestre)
#             except:
#                 return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#                 )

#             var_user_rol= var_old_user_rol
#             var_user_rol.estado = "INACTIVO"
#             var_user_rol.save()

#             return Response({'Respuesta': 'True'})

# class User_rol(APIView):

#     serializer_class =serializers.User_rol
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if (serializer.is_valid()):

#             id_user_request = serializer.validated_data.get('id_user')
#             id_rol_request = serializer.validated_data.get('id_rol')
#             var_usuario = get_object_or_404(User, id = id_user_request)
#             var_rol = get_object_or_404(rol, id = id_rol_request)
#             var_semestre = get_object_or_404(semestre, semestre_actual = True)
#             try:
#                 var_old_user_rol = get_object_or_404(usuario_rol, id_usuario = var_usuario,  id_semestre = var_semestre)
#             except:
#                 var_old_user_rol = Empty
#             # print(var_semestre.id)
#             # print(var_old_user_rol.id_semestre)
#             # print(var_semestre.id)
#             # print(var_old_user_rol.estado)
#             if(var_old_user_rol != Empty and var_old_user_rol.id_semestre.id == var_semestre.id and var_old_user_rol.estado == "ACTIVO"):
#                 print("entre a 1")
#                 var_user_rol= var_old_user_rol
#                 var_user_rol.id_usuario= var_usuario
#                 var_user_rol.id_rol = var_rol
#                 var_user_rol.id_semestre = var_semestre
#                 var_user_rol.save()
#             elif(var_old_user_rol == Empty):
#                 print("entre a 2")
#                 var_user_rol= usuario_rol()
#                 var_user_rol.id_usuario= var_usuario
#                 var_user_rol.id_rol = var_rol
#                 var_user_rol.id_semestre = var_semestre
#                 var_user_rol.save()
#             elif(var_old_user_rol != Empty and var_old_user_rol.id_semestre.id != var_semestre):
#                 print("entre a 3")
#                 var_user_rol= usuario_rol()
#                 var_user_rol.id_usuario= var_usuario
#                 var_user_rol.id_rol = var_rol
#                 var_user_rol.id_semestre = var_semestre
#                 var_user_rol.save()
#             elif(var_old_user_rol != Empty and var_old_user_rol.id_semestre.id == var_semestre and var_old_user_rol.estado != "ACTIVO"):
#                 print("entre a 4")
#                 var_user_rol= var_old_user_rol
#                 var_user_rol.id_usuario= var_usuario
#                 var_user_rol.id_rol = var_rol
#                 var_user_rol.estado = "ACTIVO"
#                 var_user_rol.id_semestre = var_semestre
#                 var_user_rol.save()
#             else:
#                 Response(
#                     serializer.errors,
#                     status=status.HTTP_400_BAD_REQUEST
#                 )


#             return Response({'Respuesta': 'True'})

#         return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )






# class All_semestres(APIView):

#     def get(self, request):
#         print(request)
#         list_semestre =semestre.objects.all()
#         return Response (list(list_semestre.values()))



class Estudiante_actualizacion(APIView):

    serializer_class =serializers.Estudiante_actualizacion
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if (serializer.is_valid()):
            print("entre a serializ")
            num_doc_request = serializer.validated_data.get('id_nuevo_num_doc')
            telefono_res_request = serializer.validated_data.get('id_nuevo_telefono_res')
            # var_num_doc = get_object_or_404(estudiante, num_doc = num_doc_request)
            # var_telefono_res = get_object_or_404(estudiante, telefono_res = telefono_res_request)
            
            try:
                var_old_usuario = get_object_or_404(estudiante, num_doc = num_doc_request)
                print("entra aqui")
            except:
                print("entra aqui 2")
                var_old_usuario = Empty
            # print(var_semestre.id)
            # print(var_old_usuario.id_semestre)
            # print(var_semestre.id)
            # print(var_old_usuario.estado)
            if(var_old_usuario != Empty ):
                print("entre a 1")
                var_usuario= var_old_usuario
                var_usuario.telefono_res = telefono_res_request
                var_usuario.save()
            else:
                print("entre a 2")
                Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

            return Response({'Respuesta': 'True'})

        return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
