# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, sys, base64
from rest_framework.response import Response
from django.shortcuts import render
from django.conf import settings
from rest_framework import generics, permissions, viewsets
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    UpdateAPIView, 
    DestroyAPIView, 
    CreateAPIView, 
    RetrieveUpdateAPIView 
    )
#Importamos modelos
from catalogos.models import (
	Paises,
    Ciudades,
    Localidades,
    Materias,
    Comunidades,
    Legales,
    ConocimientoRedProbono,
    EstadoClearing,
    SubEstadosClearing,
    EntidadesProbono,
	)

#Importamos serializers 
from catalogos.serializers import (
    PaisesSerializer,
    CiudadesSerializer,
    LocalidadesSerializer,
    MateriasEnfoqueSerializer,
    ComunidadesSerializer,
    MateriasLegalesSerializer,
    ConocimientoProbonoSerializer,
    EstadosClearingSerializer,
    SubEstadosClearingSerializer,
    EntidadesPrononoSerializer,
)

# Create your views here.
class PaisesList(generics.ListCreateAPIView):
    queryset = Paises.objects.all()
    serializer_class = PaisesSerializer
    permission_classes = [permissions.AllowAny]

class PaisesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paises.objects.all()
    serializer_class = PaisesSerializer
    permission_classes = [permissions.AllowAny]

class CiudadesList(generics.ListCreateAPIView):
    queryset = Ciudades.objects.all()
    serializer_class = CiudadesSerializer
    permission_classes = [permissions.AllowAny]

class CiudadesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ciudades.objects.all()
    serializer_class = CiudadesSerializer
    permission_classes = [permissions.AllowAny]

class LocalidadesList(generics.ListCreateAPIView):
    queryset = Localidades.objects.all()
    serializer_class = LocalidadesSerializer
    permission_classes = [permissions.AllowAny]

class LocalidadesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Localidades.objects.all()
    serializer_class = LocalidadesSerializer
    permission_classes = [permissions.AllowAny]

class MateriasEnfoqueList(generics.ListCreateAPIView):
    queryset = Materias.objects.all()
    serializer_class = MateriasEnfoqueSerializer
    permission_classes = [permissions.AllowAny]

class MateriasEnfoqueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Materias.objects.all()
    serializer_class = MateriasEnfoqueSerializer
    permission_classes = [permissions.AllowAny]

class ComunidadesList(generics.ListCreateAPIView):
    queryset = Comunidades.objects.all()
    serializer_class = ComunidadesSerializer
    permission_classes = [permissions.AllowAny]

class ComunidadesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comunidades.objects.all()
    serializer_class = ComunidadesSerializer
    permission_classes = [permissions.AllowAny]

class MateriasLegalesList(generics.ListCreateAPIView):
    queryset = Legales.objects.all()
    serializer_class = MateriasLegalesSerializer
    permission_classes = [permissions.AllowAny]

class MateriasLegalesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Legales.objects.all()
    serializer_class = MateriasLegalesSerializer
    permission_classes = [permissions.AllowAny]

class ConocimientoProbonoList(generics.ListCreateAPIView):
    queryset = ConocimientoRedProbono.objects.all()
    serializer_class = ConocimientoProbonoSerializer
    permission_classes = [permissions.AllowAny]

class ConocimientoProbonoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConocimientoRedProbono.objects.all()
    serializer_class = ConocimientoProbonoSerializer
    permission_classes = [permissions.AllowAny]

class EstadosClearingList(generics.ListCreateAPIView):
    queryset = EstadoClearing.objects.all()
    serializer_class = EstadosClearingSerializer
    permission_classes = [permissions.AllowAny]

class EstadosClearingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstadoClearing.objects.all()
    serializer_class = EstadosClearingSerializer
    permission_classes = [permissions.AllowAny]

class SubEstadosClearingList(generics.ListCreateAPIView):
    queryset = SubEstadosClearing.objects.all()
    serializer_class = SubEstadosClearingSerializer
    permission_classes = [permissions.AllowAny]

class SubEstadosClearingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubEstadosClearing.objects.all()
    serializer_class = SubEstadosClearingSerializer
    permission_classes = [permissions.AllowAny]

class EntidadesProbonoList(generics.ListCreateAPIView):
    queryset = EntidadesProbono.objects.all()
    serializer_class = EntidadesPrononoSerializer
    permission_classes = [permissions.AllowAny]

class EntidadesProbonoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EntidadesProbono.objects.all()
    serializer_class = EntidadesPrononoSerializer
    permission_classes = [permissions.AllowAny]