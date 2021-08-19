from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Cursos(models.Model):
    materia=models.CharField(max_length=20, verbose_name="Nombre del curso")
    horas=models.FloatField(verbose_name="Horas del curso" )
    aprobado=models.BooleanField(verbose_name="Marca solo si aprobaste")
    turno=models.TextField(verbose_name="Turno")
    inicio=models.DateField(verbose_name="Inicio del curso")
    fin=models.DateField(verbose_name="Fin del cuerso")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografia")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["-created"]
#El menos indica que se ordenara del mas reciente al mas viejo
    def _str_(self):
        return self.materia
#Indica que se mostrara el nombre como valor de la en la tabla

class Comentario(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE,verbose_name="Materia")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    coment = RichTextField(verbose_name="Comentario") 
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created"]
    def __str__(self):
        return self.coment

class ComentarioForm(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre = models.TextField(verbose_name="Usuario")
    correo = models.TextField(verbose_name="Correo")
    curso = models.TextField(verbose_name="Curso")
    mensaje = models.TextField(verbose_name="Comentario")
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    class Meta:
        verbose_name = "Comentario Formulario"
        verbose_name_plural = "Comentarios Formularios"
        ordering = ["-created"]
    def __str__(self):
        return self.mensaje


class ComentarioCurso(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    mat = models.TextField(verbose_name="Curso")
    tur = models.TextField(verbose_name="Turno")
    matricula = models.TextField(verbose_name="Matricula")
    calif = models.TextField(verbose_name="Calificación")
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    class Meta:
        verbose_name = "Comentario Curso"
        verbose_name_plural = "Comentarios Cursos"
        ordering = ["-created"]
    def __str__(self):
        return self.matricula


class Archivos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    archivo = models.FileField(upload_to="archivos", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
        ordering = ["-created"]

    def __str__(self):
        return self.titulo


