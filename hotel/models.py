from django.db import models


class Type(models.Model):
    title = models.CharField(max_length = 140)
    
    def __unicode__(self):
        return self.title


class Hotel(models.Model):
    title = models.CharField(max_length=140)
    favorite = models.IntegerField(default = 0)
    description = models.TextField()
    category = models.ForeignKey(Type)
    timestamp = models.DateTimeField(auto_now_add=True)
    logoHotel = models.ImageField(upload_to = 'hoteles/logos',null=True,blank=True)
    imagenHotel = models.ImageField(upload_to='hoteles/images', blank=True, null=True)
    latitud = models.FloatField(null=True,blank=True,default=4.667216550739034)
    longitud = models.FloatField(null=True,blank=True,default=-74.05947089195251)

    def __unicode__(self):
        return "%s" % (self.title)