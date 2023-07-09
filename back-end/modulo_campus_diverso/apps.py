"""
Autor: Juan D. Gil T.
Correo: juan.gil.trujillo@correounivalle.edu.co
Versión: 1.0.0
Fecha: 2023-07-08
Descripción: Este código define la configuración del modulo campus_diverso.
Se importa la clase 'AppConfig' de 'Django' y se crea una subclase 'ModuloInstanciaConfig' que establece la configuración por defecto para el campo 'default_auto_field' y el nombre de la aplicación 'name'.
"""

from django.apps import AppConfig


class ModuloCampusDiversoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modulo_campus_diverso'
