from django.db import models

class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128, null=False)
    
class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128, null=False)
    apellido = models.CharField(max_length=128, null=False)
    mostrar = models.CharField(max_length=256, null=False)

class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128, null=False)
    cant_alumnos = models.IntegerField(null=False, default=5)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    
class Aula(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=128, null=False)
    ubicacion = models.CharField(max_length=128, null=False)
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)
    
class ReservaAula(models.Model):
    id = models.AutoField(primary_key=True)
    id_aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    fh_desde = models.DateTimeField(null=False)
    fh_hasta = models.DateTimeField(null=False)
    obversacion = models.CharField(max_length=256)

class HorarioMateria(models.Model):
    id = models.AutoField(primary_key=True)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    id_reserva = models.ForeignKey(ReservaAula, on_delete=models.CASCADE)
    fh_desde = models.DateTimeField(null=False)
    fh_hasta = models.DateTimeField(null=False)

    