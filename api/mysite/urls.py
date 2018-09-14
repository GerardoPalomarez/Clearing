"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from formulario import views
from catalogos import views

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^rest-auth/password/reset/confirm/', include('rest_auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^clearing/', include('formulario.urls')),
    url(r'^catalogos/', include('catalogos.urls')),
    # url(r'^account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
    #     name='account_confirm_email'),
    # url(
    #     regex=r'^contrib/password_reset/$',
    #     view=password_reset,
    #     name='password_reset'
    # ),
    # url(
    #     regex=r'^contrib/password_reset/done/$',
    #     view=password_reset_done,
    #     name='password_reset_done'
    # ),
    # url(
    #     regex=r'^contrib/reset/(?P<uidb64>[0-9A-Za-z_\-]+)'
    #           r'/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     view=password_reset_confirm,
    #     name='password_reset_confirm'
    # ),
    # url(
    #     regex=r'^contrib/reset/done/$',
    #     view=password_reset_complete,
    #     name='password_reset_complete'
    # ),
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
