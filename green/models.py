from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid


class Post(models.Model):
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4)
    slug = models.SlugField(max_length=20)
    grados=(
        ('Primero basico', 'Primero basico'),
        ('Segundo basico', 'Segundo basico'),
        ('Tercero basico', 'Tercero basico'),
        ('Cuarto basico', 'Cuarto basico'),
        ('Quinto basico', 'Quinto basico'),
        ('Sexto basico', 'Sexto basico'),
        ('Septimo basico', 'Septimo basico'),
        ('Octavo basico', 'Octavo basico'),
        ('Primero medio', 'Primero medio'),
        ('Segundo medio', 'Segundo medio'),
        ('Tercero medio', 'Tercero medio'),
        ('Cuarto medio', 'Cuarto medio'),
        ('PDT', 'PDT'),
    )
    grado = models.CharField(max_length=14, choices=grados)
    asignaturas_Basica= (
        ('No', 'No'),
        ('Matemáticas', 'Matemáticas '),
        ('Ciencias Naturales', 'Ciencias Naturales'),
        ('Lenguaje y comunicación', 'Lenguaje y comunicación'),
        ('Historia, Geografía y Ciencias Sociales', 'Historia, Geografía y Ciencias Sociales'),
        ('Ingles', 'Ingles'),
        ('Otros', 'Otros'),
    )
    asignatura_Basica= models.CharField(max_length=39, choices= asignaturas_Basica,default='N')
    asignaturas_Media= (
        ('No', 'No'),
        ('Matemáticas', 'Matemáticas '),
        ('Matemáticas avanzadas', 'Matemáticas avanzadas'),
        ('Lenguaje y comunicación', 'Lenguaje y comunicación'),
        ('Historia, Geografía y Ciencias Sociales', 'Historia, Geografía y Ciencias Sociales'),
        ('Física', 'Física '),
        ('Física avanzada', 'Física avanzada'),
        ('Química', 'Química '),
        ('Química avanzada', 'Química avanzada'),
        ('Biología', 'Biología '),
        ('Biología avanzada', 'Biología avanzada'),
        ('Inglés', 'Inglés'),
        ('Otros', 'Otros'),
    )
    asignatura_Media= models.CharField(max_length=39, choices=asignaturas_Media, default='No' )
    contactos=(
    ("Email", "Email"),
    ("instagram", "instagram"),
    ("whatsapp", "whatsapp")
    )
    contacto = models.CharField(max_length=20, choices=contactos, default="Email")


    dato_de_contacto = models.TextField(default="")
    description = models.TextField()
    image = models.ImageField(
        upload_to="images/",
        default="images/Fondo.png"
    )
    published = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="green_post"
    )
    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return self.description



from django.contrib.auth.models import User

class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)





