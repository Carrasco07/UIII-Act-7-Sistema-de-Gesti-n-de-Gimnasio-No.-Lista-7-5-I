from django.db import models


class Membresia(models.Model):
    tipo_membresia = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_meses = models.IntegerField()
    beneficios = models.TextField()
    num_sesiones_incluidas = models.IntegerField()
    es_activa = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo_membresia


class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    fecha_registro = models.DateField()
    tipo_membresia = models.ForeignKey(
        Membresia, on_delete=models.SET_NULL, null=True
    )
    fecha_vencimiento_membresia = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    certificado = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Clase(models.Model):
    nombre_clase = models.CharField(max_length=100)
    descripcion = models.TextField()
    horario = models.CharField(max_length=100)
    duracion_minutos = models.IntegerField()
    entrenador = models.ForeignKey(
        Entrenador, on_delete=models.CASCADE
    )
    cupo_maximo = models.IntegerField()
    costo_clase = models.DecimalField(max_digits=10, decimal_places=2)
    nivel_dificultad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_clase


class ReservaClase(models.Model):
    socio = models.ForeignKey(
        Socio, on_delete=models.CASCADE
    )
    clase = models.ForeignKey(
        Clase, on_delete=models.CASCADE
    )
    fecha_reserva = models.DateTimeField()
    estado_reserva = models.CharField(max_length=50)
    fecha_cancelacion = models.DateTimeField(null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Reserva de {self.socio} en {self.clase}"


class Pago(models.Model):
    socio = models.ForeignKey(
        Socio, on_delete=models.CASCADE
    )
    fecha_pago = models.DateTimeField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    concepto = models.CharField(max_length=100)
    membresia_pagada = models.ForeignKey(
        Membresia, on_delete=models.SET_NULL, null=True
    )
    estado_pago = models.CharField(max_length=50)

    def __str__(self):
        return f"Pago {self.monto} - {self.socio}"


class RutinaPersonalizada(models.Model):
    socio = models.ForeignKey(
        Socio, on_delete=models.CASCADE
    )
    entrenador = models.ForeignKey(
        Entrenador, on_delete=models.CASCADE
    )
    fecha_creacion = models.DateField()
    objetivo = models.CharField(max_length=100)
    descripcion_ejercicios = models.TextField()
    frecuencia = models.CharField(max_length=50)
    duracion_semanas = models.IntegerField()

    def __str__(self):
        return f"Rutina de {self.socio}"
