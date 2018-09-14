from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from catalogos import views

urlpatterns = [
    url(r'paises/', views.PaisesList.as_view()),
    url(r'ciudades/', views.CiudadesList.as_view()),
    url(r'localidades/', views.LocalidadesList.as_view()),
    url(r'materias-enfoque/', views.MateriasEnfoqueList.as_view()),
    url(r'comunidades/', views.ComunidadesList.as_view()),
    url(r'materias-legales/', views.MateriasLegalesList.as_view()),
    url(r'conocimiento-probono/', views.ConocimientoProbonoList.as_view()),
    url(r'subestados/', views.SubEstadosClearingList.as_view()),
    url(r'fases/', views.EstadosClearingList.as_view()),
    url(r'entidades/', views.EntidadesProbonoList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)