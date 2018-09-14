from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from formulario import views

urlpatterns = [
   url(r'^$', views.FormularioList.as_view()),
   url(r'^(?P<pk>[0-9]+)/$', views.FormularioDetail.as_view()),   
   url(r'^contar-solicitudes/$', views.ClearingCount.as_view(), name='contar_solicitudes'),
   url(r'^contar-solicitudes-por-fecha/$', views.ClearingCountByDates.as_view(), name='contar_solicitudes_por_fecha'),
#    url(r'^test/$', views.GetDonantesByProyectoId.as_view(), name='test_name'),
   url(r'^test/(?P<fecha>.+)/$', views.GetDonantesByProyectoId.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)