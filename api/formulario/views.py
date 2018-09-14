# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, sys, base64
from rest_framework.response import Response
from django.db.models import Count
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from rest_framework.views import APIView

# Para lo del correo y envio de plantilla html
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.shortcuts import render

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
from formulario.models import  (
    Formulario
)

#Importamos serializers 
from formulario.serializers import (
    FormularioSerializer,
    ClearingCountSerializer,
)

from django.contrib.auth.models import User
# Create your views here.
class FormularioList(generics.ListCreateAPIView):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer
    permission_classes = [permissions.AllowAny]

class FormularioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer
    permission_classes = [permissions.AllowAny]
    # def update(self, serializer):
    #     id_form = self.request.id
    #     print(id_form)
        # return Response(serializer.data)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        # print(serializer.data)
        to_email = "gerardo@minimalist.mx"
        subject = "Solicitud actualizada"
        message = "Hola se ha actualizado la solicitud No. "+str(serializer.data['id'])+" de la Organización: "+ serializer.data['nombre_osc'] +" ha sido actualizada."
        if serializer.data['estado_clearing'] == 2 :
            message +=" Ahora la solicitud está en estado: Comprobado"
        if serializer.data['estado_clearing'] == 3 :
            message +=" Ahora la solicitud está en estado: En Clearing"
        if serializer.data['estado_clearing'] == 4 :
            message +=" Ahora la solicitud está en estado:Asignada"
        if serializer.data['estado_clearing'] == 5 :
            message +=" Ahora la solicitud está en estado: Cerrada"
        if serializer.data['estado_clearing'] == 6 :
            message +=" Ahora la solicitud ha Finalizado"
        message += "Por favor verifica la información."
        content = render_to_string('Email.html', {
        'title': 'Solicitud actualizada', 'user': 'Admin', 'message': message, })
        send_mail(
            subject,
            "",
            'from@example.com',
            ['gerardo@minimalist.mx'],
            html_message=content,
            fail_silently=False,
        )
        return Response(serializer.data)
   
class ClearingCount(RetrieveAPIView):
    
    def get(self, request):
        fecha_inicial = ''
        fecha_actual = ''
        clearing_all = Formulario.objects.all()
        enRevision = clearing_all.filter(estado_clearing='1').count()
        comprobado = clearing_all.filter(estado_clearing='2').count()
        enClearing = clearing_all.filter(estado_clearing='3').count()
        asignado = clearing_all.filter(estado_clearing='4').count()
        cerrado = clearing_all.filter(estado_clearing='5').count()
        finalizado = clearing_all.filter(estado_clearing='6').count()
        todos = clearing_all.count() 
#         cerrado = clearing_all.filter(estado_clearing_id='5').count()
#         finalizado = clearing_all.filter(estado_clearing_id='6').count()
        response = {'enRevision': enRevision, 'comprobado': comprobado, 'enClearing': enClearing,
            'asignado': asignado, 'cerrado': cerrado, 'finalizado': finalizado, 'todos': todos,
             'fecha_inicial': fecha_inicial, 'fecha_actual': fecha_actual
            }
        serializer= ClearingCountSerializer(response)
        print(serializer)
        return Response(serializer.data)

class GetDonantesByProyectoId(generics.ListAPIView):
   serializer_class = FormularioSerializer
   permission_classes = [permissions.AllowAny]

   def get_queryset(self):
        fecha = self.kwargs['fecha']
    #    return Formulario.objects.filter(fecha_solicitud__range=(fecha.split(",")[0], fecha.split(",")[1]))
        fecha_inicial = fecha.split(",")[0]
        fecha_actual = fecha.split(",")[1]
        clearing_all = Formulario.objects.filter(fecha_solicitud__range=('2018-08-01', '2018-08-30'))
        enRevision = clearing_all.filter(estado_clearing='1').count()
        comprobado = clearing_all.filter(estado_clearing='2').count()
        enClearing = clearing_all.filter(estado_clearing='3').count()
        asignado = clearing_all.filter(estado_clearing='4').count()
        cerrado = clearing_all.filter(estado_clearing='5').count()
        finalizado = clearing_all.filter(estado_clearing='6').count()
        todos = clearing_all.count() 
        response = {'enRevision': enRevision, 'comprobado': comprobado, 'enClearing': enClearing,
            'asignado': asignado, 'cerrado': cerrado, 'finalizado': finalizado, 'todos': todos, 
            'fecha_inicial': fecha_inicial, 'fecha_actual': fecha_actual
            }
        # serializer= ClearingCountSerializer(response)
        # return Response(serializer.data)
        print(response)
        return clearing_all





# class ClearingCountByDates(generics.ListCreateAPIView):
# class ClearingCountByDates(APIView):
class ClearingCountByDates(CreateAPIView):
    serializer_class = ClearingCountSerializer

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            fecha_inicial = request.POST.get('fecha_inicial')
            fecha_actual = request.POST.get('fecha_actual')
            # fecha_inicial = request.POST['fecha_inicial']
            # fecha_actual = request.POST['fecha_actual']
            print(request.POST.get('fecha_inicial'))
            print(fecha_actual)
            clearing_all = Formulario.objects.filter(fecha_solicitud__range=(fecha_inicial, fecha_actual))
            enRevision = clearing_all.filter(estado_clearing='1').count()
            comprobado = clearing_all.filter(estado_clearing='2').count()
            enClearing = clearing_all.filter(estado_clearing='3').count()
            asignado = clearing_all.filter(estado_clearing='4').count()
            cerrado = clearing_all.filter(estado_clearing='5').count()
            finalizado = clearing_all.filter(estado_clearing='6').count()
            todos = clearing_all.count() 
    #         cerrado = clearing_all.filter(estado_clearing_id='5').count()
    #         finalizado = clearing_all.filter(estado_clearing_id='6').count()
            response = {'enRevision': enRevision, 'comprobado': comprobado, 'enClearing': enClearing,
                'asignado': asignado, 'cerrado': cerrado, 'finalizado': finalizado, 'todos': todos, 
                'fecha_inicial': fecha_inicial, 'fecha_actual': fecha_actual
                }
            serializer= ClearingCountSerializer(response)
            return Response(serializer.data)
    
        