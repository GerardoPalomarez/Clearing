from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
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

class PaisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paises
        fields = '__all__'

class CiudadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudades
        fields = ('id', 'nombre', 'pais_id')

class LocalidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidades
        fields = ('id', 'nombre', 'ciudad_id')

class MateriasEnfoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materias
        fields = ('id', 'nombre')

class ComunidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunidades
        fields = ('id', 'nombre')

class MateriasLegalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legales
        fields = ('id', 'nombre')

class ConocimientoProbonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConocimientoRedProbono
        fields = ('id', 'nombre')

class EstadosClearingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoClearing
        fields = ('id', 'nombre')

class SubEstadosClearingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubEstadosClearing
        fields = ('id', 'nombre', 'subestado_clearing')


class EntidadesPrononoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntidadesProbono
        fields = ('id', 'nombre')

