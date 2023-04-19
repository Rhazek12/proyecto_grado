from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from modulo_base.serializers import (
    CustomTokenObtainPairSerializer, user_token, group_serializer
)
from modulo_instancia.serializers import semestre_serializer, instancia_serializer
from modulo_usuario_rol.serializers import usuario_rol_serializer, rol_serializer
from django.contrib.auth.models import User

from modulo_instancia.models import semestre, instancia
from modulo_usuario_rol.models import rol, usuario_rol



class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            print('1')
            if user.is_active:
                print('2')
                if login_serializer.is_valid():
                    print('3')
                    user_serializer = user_token(user)
                    print(user.id)
                    dato_usuario_rol = usuario_rol.objects.get(id_usuario = user.id,estado = "ACTIVO")
                    serializer_usuario_rol = usuario_rol_serializer(dato_usuario_rol)
                    dato_rol = rol.objects.get(id =serializer_usuario_rol.data['id_rol'] )
                    serializer_rol = rol_serializer(dato_rol)
                    dato_semestre = semestre.objects.get(semestre_actual = True, id =serializer_usuario_rol.data['id_semestre'])
                    serializer_semestre =semestre_serializer(dato_semestre)
                    dato_instancia = instancia.objects.get(id = serializer_semestre.data['id_instancia'])
                    serializer_instancia = instancia_serializer(dato_instancia)
    
                    extra_info = {'nombre_completo' : user_serializer.data.get('first_name') +" "+ user_serializer.data.get('last_name'),
                                'rol' : serializer_rol.data['nombre'],
                                'semestre_actual': serializer_semestre.data['nombre'],
                                'instancia':serializer_instancia.data['nombre'],
                                'instancia_id':serializer_instancia.data['id'],
                                }
                    data = dict(user_serializer.data, **extra_info)
                    print(data)
                    return Response({
                        'token': login_serializer.validated_data.get('access'),
                        'refresh-token': login_serializer.validated_data.get('refresh'),
                        'user': data,
                        'message': 'Inicio de Sesion Exitoso'
                    }, status=status.HTTP_200_OK)
                return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': 'El usuario no está activo'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario.'}, status=status.HTTP_400_BAD_REQUEST)
        