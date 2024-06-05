from django.db import models

class Direccion(models.Model):
    calle = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)

class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    profesores = models.ManyToManyField(Profesor, related_name='cursos')

class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)
    cursos = models.ManyToManyField(Curso, related_name='estudiantes')