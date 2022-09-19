from django.db import models
from modulo_usuario_rol.models import estudiante

# Create your models here.

class instancia (models.Model):

    codigo= models.IntegerField()
    nombre= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=150)

    class Meta:
        db_table = "instancia"

class semestre (models.Model):

    nombre= models.CharField(max_length=30)
    fecha_inicio= models.DateTimeField(auto_now_add=False)
    fecha_fin= models.DateTimeField(auto_now_add=False)
    id_instancia= models.ForeignKey(instancia ,on_delete=models.CASCADE,default=0)
    semestre_actual= models.BooleanField(default= False)


    class Meta:
        db_table = "semestre"

class cohorte (models.Model):

    id_number= models.IntegerField()
    nombre= models.CharField(max_length=30)
    tiempo_creacion= models.DateTimeField(auto_now_add=True)
    tiempo_modificacion= models.DateTimeField(auto_now_add=False)


    class Meta:
        db_table = "cohorte"

class cohorte_instancia (models.Model):

    id_cohorte= models.ForeignKey(cohorte,on_delete=models.CASCADE,default=0)
    id_instancia= models.ForeignKey(instancia,on_delete=models.CASCADE,default=0)
    
    class Meta:
        db_table = "cohorte_instancia"

class cohorte_estudiante(models.Model):

    id_cohorte= models.ForeignKey(cohorte,on_delete=models.CASCADE,default=0)
    id_estudiante= models.ForeignKey(estudiante,on_delete=models.CASCADE,default=0)
    tiempo_creacion= models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "cohorte_estudiante"