from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(max_length = 140)
    
    def __unicode__(self):
        return self.titulo


class Hotel(models.Model):
    titulo = models.CharField(max_length=140)
    favoritos = models.IntegerField(default = 0)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria)
    timestamp = models.DateTimeField(auto_now_add=True)
    #imagen = models.ImageField(upload_to='enlaces/', blank=True, null=True)

    def __unicode__(self):
        return "%s -  %s" % (self.titulo,self.enlace)