# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models



# Create your models here.
class Paises(models.Model):
    abreviatura = models.CharField(max_length=5, null=True, blank=True, unique=True)
    nombre = models.CharField(max_length=150, null=False, blank=False)

    def __unicode__(self):
		return self.nombre 

class Ciudades(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    pais_id = models.ForeignKey(Paises, null=True, blank=True, related_name="ciudad_pais")

    def __unicode__(self):
	    return self.nombre

class Localidades(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    ciudad_id = models.ForeignKey(Ciudades, null=True, blank=True, related_name="ciudad_localidad")

    def __unicode__(self):
	    return self.nombre


class Comunidades(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    
    def __unicode__(self):
	    return self.nombre

class Legales(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    
    def __unicode__(self):
	    return self.nombre

class Materias(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    
    def __unicode__(self):
	    return self.nombre

class ConocimientoRedProbono(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    
    def __unicode__(self):
	    return self.nombre

class EstadoClearing(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    
    def __unicode__(self):
	    return self.nombre
        
class SubEstadosClearing(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    subestado_clearing = models.ForeignKey(EstadoClearing, null=True, blank=True, related_name="subestado_estado")
    
    def __unicode__(self):
	    return self.nombre

class EntidadesProbono(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)

    def __unicode__(self):
        return self.nombre
