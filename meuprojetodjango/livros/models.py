from django.db import models

# Create your models here.
class livros(models.Model):
    titulo = models.CharField(max_length=40, verbose_name="titulo")  
    autor = models.CharField(max_length=20, verbose_name="autor")  