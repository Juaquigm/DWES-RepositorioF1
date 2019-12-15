from django.db import models
from django.utils import timezone

# Creamos los modelos para nuestra aplicacion

class Agente(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=150)
    Apellidos = models.CharField(max_length=300)
    Pais = models.CharField(max_length=100)

    def guarda(self):
        self.save()

    def __str__(self):
        resultado = self.Apellidos + ' ' + self.Nombre
        return resultado

class Serie(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=300)
    Localizacion = models.CharField(max_length=50)

    def guarda(self):
        self.save()
    
    def __str__(self):
        return self.Nombre

class Suministrador(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=300)
    Pais = models.CharField(max_length=300)
    Cilindrada = models.PositiveIntegerField() #Campo numerico que nos fuerza a introducir un numero positivo

    def guarda(self):
        self.save()
    
    def __str__(self):
        return self.Nombre

class Neumaticos(models.Model):
    Neumaticos_Choice = (
        ('Blandos', 'Blandos'),
        ('Duros', 'Duros'),
        ('Lluvia', 'Lluvia'),
        ('Extremos','Extremos'),
    )
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=300)
    Tipo = models.CharField(max_length=15,choices=Neumaticos_Choice)

    def guarda(self):
        self.save()
    
    def __str__(self):
        return self.Nombre

class Circuito(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=300)
    Ciudad = models.CharField(max_length=300)
    Pais = models.CharField(max_length=100)
    Id_Serie = models.ForeignKey(Serie,on_delete=models.CASCADE)
    Longitud = models.IntegerField()

    def guarda(self):
        self.save()
    
    def __str__(self):
        return self.Nombre

class Equipo(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=300)
    Fecha_Creacion = models.DateField()
    Presupuesto = models.IntegerField()
    Motor = models.ForeignKey(Suministrador,on_delete=models.CASCADE)
    Pais_Origen = models.CharField(max_length=300)

    def guarda(self):
        self.save()

    def __str__(self):
        return self.Nombre

class Patrocinador(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=300)
    EsPrincipal = models.BooleanField()
    EscuderiaAsig = models.ForeignKey(Equipo,on_delete=models.CASCADE)
    
    def guarda(self):
        self.save()

    def __str__(self):
        return self.Nombre
    
class Piloto(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=300)
    Apellido = models.CharField(max_length=300)
    Id_Escuderia = models.ForeignKey(Equipo,on_delete=models.CASCADE)
    Numero = models.PositiveIntegerField()
    Id_Agente = models.ForeignKey(Agente,on_delete=models.CASCADE)

    def guarda(self):
        self.save()
    
    def __str__(self):
        resultado = self.Nombre + ' ' + self.Apellido + ' ' +'- '+ str(self.Numero)
        return resultado


