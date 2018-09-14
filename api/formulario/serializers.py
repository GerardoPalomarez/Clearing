from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

# Para lo del correo y envio de plantilla html
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.shortcuts import render

from rest_framework.serializers import (
	ModelSerializer, 
	ReadOnlyField, 
	Serializer,
    CharField,
	)
#Importamos modelos
from formulario.models import  (
    Formulario
)

class FormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = '__all__'
        
    def create(self, data):
        id_clearing = data['id']
        nombre_osc = data['nombre_osc']
        descripcion_caso = data['descripcion_caso']
        # formulario = data.pop('formulario')
        # print(data)
        formulario = Formulario.objects.create(**data)
        formulario.save()
        to_email = "gerardo@minimalist.mx"
        subject = "Nueva solicitud"
        message = "Hola te notificamos que una nueva solicitud con No. "+id_clearing+""
        message += "se encuentra en estado de revisi&oacute;n; de la OSC: "+nombre_osc+" con el tema de: "
        message += ""+descripcion_caso+". Recuerda que tienes 5 d&iacute;as para dar seguimiento al caso"
        content = render_to_string('Email.html', {
		  'title': 'Nueva solicitud', 'user': 'Admin', 'message': message, })
        send_mail(
            subject,
            "",
            'from@example.com',
            ['gerardo@minimalist.mx'],
            html_message=content,
            fail_silently=False,
        )
		# send_mail(subject, "", "gerardo@minimalist.mx", [mail], content, fail_silently=False)
        return data

class ClearingCountSerializer(Serializer):
    enRevision = ReadOnlyField() 
    comprobado = ReadOnlyField() 
    enClearing = ReadOnlyField() 
    asignado = ReadOnlyField() 
    cerrado = ReadOnlyField() 
    finalizado = ReadOnlyField() 
    todos =  ReadOnlyField() 
    fecha_inicial = CharField(required=True)
    fecha_actual = CharField(required=True)

    def create(self, data):
        return ClearingCountSerializer

        
