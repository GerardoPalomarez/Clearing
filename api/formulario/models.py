# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from catalogos.models import (
	Paises,
    Ciudades,
    Localidades,
    Materias,
    Comunidades,
    Legales,
    ConocimientoRedProbono,
    EstadoClearing,
    SubEstadosClearing
	)


class Formulario(models.Model):
    nombre_osc =  models.CharField(max_length=100, blank=False, null=False)
    fecha_solicitud = models.DateTimeField(auto_now_add=False, auto_now=False)
    descripcion_caso = models.TextField(blank=False, null=False)
    email_osc = models.EmailField(blank=False, null=False)
    sitio_web_osc = models.URLField(blank=False, null=False)
    tel_oficina_osc =  models.CharField(max_length=100, blank=False, null=False)
    direccion_osc = models.CharField(max_length=100, blank=False, null=False)
    pais_osc = models.ForeignKey(Paises, null=True, blank=True, related_name="osc_pais")
    provincia_osc = models.ForeignKey(Ciudades, null=True, blank=True, related_name="osc_ciudad")
    localidad_osc = models.ForeignKey(Localidades, null=True, blank=True, related_name="osc_localidad")
    codigo_postal_osc =  models.CharField(max_length=5, blank=False, null=False)
    razon_social_osc = models.CharField(max_length=100, blank=False, null=False)
    rfc_organizacion = models.CharField(max_length=100, blank=False, null=False)
    direccion_legal_osc = models.CharField(max_length=100, blank=False, null=False)
    descripcion_organizacion = models.CharField(max_length=100, blank=False, null=False)
    nombre_contacto = models.CharField(max_length=100, blank=False, null=False)
    correo_contacto = models.EmailField(blank=False, null=False)
    puesto_contacto = models.CharField(max_length=100, blank=False, null=False)
    telefono_contacto = models.CharField(max_length=100, blank=False, null=False)
    celular_contacto = models.CharField(max_length=100, blank=False, null=False)
    problema_social_proyecto = models.TextField(blank=False, null=False)
    impacto_proyecto = models.TextField(blank=False, null=False)
    # cuenta_con_apoyo = models.BooleanField(blank=False, null=False, default=True)
    cuenta_con_apoyo = models.CharField(max_length=5, blank=False, null=False)
    # fin_religioso = models.BooleanField(blank=False, null=False, default=True)
    fin_religioso = models.CharField(max_length=5, null=False)
    # tiene_discriminacion = models.BooleanField(blank=False, null=False, default=True)
    tiene_discriminacion = models.CharField(max_length=5, null=False)
    # miembro_red_probono = models.BooleanField(blank=False, null=False, default=True)
    miembro_red_probono = models.CharField(max_length=5,  null=False)
    comienzo_organizacion = models.TextField(blank=False, null=False)
    presupuesto_anual = models.IntegerField()
    fuentes_financiamiento = models.TextField(blank=False, null=False)
    # otra_red_abogados = models.BooleanField(blank=False, null=False, default=True)
    otra_red_abogados = models.CharField(max_length=5, null=False)
    # recibio_ayuda_probono = models.BooleanField(blank=False, null=False, default=True)
    recibio_ayuda_probono = models.CharField(max_length=5,  null=False)
    personal_contratado = models.IntegerField()
    voluntarios_osc = models.IntegerField()
    organos_gobierno = models.TextField(blank=False, null=False)
    # cuenta_consejo_independiente = models.BooleanField(blank=False, null=False, default=True)
    cuenta_consejo_independiente = models.CharField(max_length=5, null=False)
    presidente_organizacion = models.CharField(max_length=100, blank=False, null=False)
    consejeros_organizacion = models.CharField(max_length=100, blank=False, null=False)
    beneficiarios_directos = models.TextField(blank=False, null=False)
    beneficiarios_indirectos = models.TextField(blank=False, null=False)
    materias_enfoque = models.ForeignKey(Materias, null=True, blank=True, related_name="osc_ciudad")
    tipo_comunidad = models.ForeignKey(Comunidades, null=True, blank=True, related_name="osc_ciudad")
    caracteristicas_comunidad = models.TextField(blank=False, null=False)
    materias_legales = models.ForeignKey(Legales, null=True, blank=True, related_name="osc_ciudad")
    porque_quiere_fortalecer = models.TextField(blank=False, null=False)
    # cuenta_aviso_privacidad = models.BooleanField(blank=False, null=False, default=True)
    cuenta_aviso_privacidad = models.CharField(max_length=5, null=False)
    # sabe_fechas_avisos_antilavado = models.BooleanField(blank=False, null=False, default=True)
    sabe_fechas_avisos_antilavado = models.CharField(max_length=5, blank=False, null=False)
    # sabe_fecha_entrega_declaracion_anual = models.BooleanField(blank=False, null=False, default=True)
    sabe_fecha_entrega_declaracion_anual = models.CharField(max_length=5,blank=False, null=False)
    # acta_constitutiva_doc = models.FileField(upload_to='uploads/actasconstitutivas/', null=True, blank=True)
    # recibos_sat_doc = models.FileField(upload_to='uploads/recibossat/', null=True, blank=True)
    # cluni_doc = models.FileField(upload_to='uploads/cluni/', null=True, blank=True)
    # relatorio_anual_doc = models.FileField(upload_to='uploads/relatoriosanual/', null=True, blank=True)
    # reporte_logros_doc = models.FileField(upload_to='uploads/reporteslogros/', null=True, blank=True)
    # auditoria_anual_doc = models.FileField(upload_to='uploads/auditoriaanual/', null=True, blank=True)
    acta_constitutiva = models.BooleanField(blank=False, null=False, default=False)
    recibos_sat = models.BooleanField(blank=False, null=False, default=False)
    cluni = models.BooleanField(blank=False, null=False, default=False)
    relatorio_anual = models.BooleanField(blank=False, null=False, default=False)
    reporte_logros = models.BooleanField(blank=False, null=False, default=False)
    auditoria_anual = models.BooleanField(blank=False, null=False, default=False)
    conocimiento_redprobono_mexico = models.ForeignKey(ConocimientoRedProbono, null=True, blank=True, related_name="osc_ciudad")
    comentarios_adicionales = models.TextField(blank=False, null=True)
    # acuerdo_entrega_docs = models.BooleanField(blank=False, null=False, default=True)
    acuerdo_entrega_docs = models.CharField(max_length=5,blank=False, null=False)
    # terminos_condiciones = models.BooleanField(blank=False, null=False, default=True)
    terminos_condiciones = models.CharField(max_length=5, blank=False, null=False)
    estado_clearing =  models.ForeignKey(EstadoClearing, null=True, blank=True, related_name="estado_clearing")
    fecha_actualizacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    subestado_clearing = models.ForeignKey(SubEstadosClearing, null=True, blank=True, related_name="estado_clearing")

    def __str__(self):
        return self.nombre_osc