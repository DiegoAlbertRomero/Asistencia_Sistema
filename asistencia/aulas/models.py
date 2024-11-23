from django.db import models
from django.core.validators import RegexValidator

class Periodo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    es_periodo_actual = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} ({self.fecha_inicio} - {self.fecha_fin})"

    def save(self, *args, **kwargs):
        # Asegura que solo un periodo sea el periodo actual
        if self.es_periodo_actual:
            Periodo.objects.filter(es_periodo_actual=True).update(es_periodo_actual=False)
        super().save(*args, **kwargs)

class Aula(models.Model):
    TIPOS_AULA = [
        ('R1', 'SISTEMAS Y COMPUTACIÓN'),
        ('R2', 'AULA R2'),
        ('R3', 'AULA R3')
    ]
    
    nombre = models.CharField(max_length=50, choices=TIPOS_AULA, unique=True)
    capacidad = models.IntegerField(default=30)

    def __str__(self):
        return self.get_nombre_display()

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Materia(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Grupo(models.Model):
    DIAS_SEMANA = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado')
    ]

    codigo = models.CharField(max_length=10, unique=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.codigo} - {self.materia.nombre}"

class AsignacionAula(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    dia = models.CharField(max_length=10, choices=Grupo.DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        unique_together = ['aula', 'dia', 'hora_inicio', 'hora_fin']

    def __str__(self):
        return f"{self.grupo} - {self.aula} ({self.dia} {self.hora_inicio}-{self.hora_fin})"