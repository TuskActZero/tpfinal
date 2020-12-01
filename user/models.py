from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('secretaria', 'secretaria'),
        ('gerencia', 'gerencia'),
        ('ventas', 'ventas'),
        ('taller', 'taller'),
        ('profesionales', 'profesionales'),
    )

    sector = models.CharField(max_length=15 ,choices= USER_TYPE_CHOICES)

    def __str__(self):
        return f"se a creado {self.sector}"


# Usuarios

class Profesional(models.Model):
    nombre = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f" {self.nombre}"

class Secretaria(models.Model):
    nombre = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f" {self.nombre}"

class Ventas(models.Model):
    nombre = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f" {self.nombre}"

class Gerencia(models.Model):
    nombre = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f" {self.nombre}"

class Taller(models.Model):
    nombre = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f" {self.nombre}"


class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField(unique=True)
    asistencia = models.BooleanField(default=True)
    historial_medico = models.TextField()
    id_medico = models.OneToOneField(Profesional, on_delete=models.CASCADE, related_name="elmedico")
    id_secretaria = models.ForeignKey('Secretaria', on_delete=models.CASCADE, related_name="elsecreta")

    def __str__(self):
        return f"el paciente {self.nombre}"


class Turno(models.Model):
    turno = models.DateTimeField(unique=True)
    id_paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, related_name="elpaciente")

    def __str__(self):
        return f"el turno {self.turno}"

class Pedido(models.Model):
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name="pacientele")
    precio = models.IntegerField()
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, related_name="elproducto")
    taller = models.ForeignKey('Taller', on_delete=models.CASCADE, related_name="eltaller")

    def __str__(self):
        return f"el pedido {self.producto} fue creado para el paciente {self.id_paciente}"


class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    lente = models.BooleanField(default=False)
    lejos = models.BooleanField(default=False)
    cerca = models.BooleanField(default=False) 
    izquierda = models.BooleanField(default=False)
    derecha = models.BooleanField(default=False)
    armazon = models.BooleanField(default=False)
    pendiente = models.BooleanField(default=True)
    ventas = models.ForeignKey('Ventas', on_delete=models.CASCADE, related_name="elventas")

    def __str__(self):
        return f"el producto {self.nombre} a sido creado"



 

