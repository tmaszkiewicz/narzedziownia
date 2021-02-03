"""T3000 URL Configuration

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
from apps.narzedziownia import views
urlpatterns = [
    url(r'^$', views.start,name="start"),
    url(r'^narzedzia_lista/$', views.narzedzia_lista,name="narzedzia_lista"),
    url(r'^odziez_lista/$', views.odziez_lista,name="odziez_lista"),
    url(r'^szablony_lista/(?P<dzial>[\w\s]+)/(?P<wariant>[\w\s-]+)/$', views.szablony_lista,{},name="szablony_lista"),
    url(r'^szablony_wybor/$', views.szablony_wybor,name="szablony_lista"),
    url(r'^narzedzia_edit/(?P<pk>\d+)/$', views.narzedzia_edit,{},name="narzedzia_edit"),
    url(r'odziez_edit/(?P<pk>\d+)/$', views.odziez_edit,{},name="odziez_edit"),
    url(r'^narzedzia_usun/(?P<pk>\d+)/$', views.narzedzia_usun,{},name="narzedzia_usun"),
    url(r'^odziez_usun/(?P<pk>\d+)/$', views.odziez_usun,{},name="odziez_usun"),
    url(r'^szablony_usun/(?P<pk>\d+)/(?P<dzial>[\w\s]+)/(?P<wariant>[\w\s-]+)/$', views.szablony_usun,{},name="szablony_usun"),
    url(r'^narzedzia_new/$', views.narzedzia_new,name="narzedzia_new"),
    url(r'^odziez_new/$', views.odziez_new,name="odziez_new"),
    url(r'^import_pracownikow/$', views.import_pracownikow,name="import_pracownikow"),
    url(r'^pracownicy_lista/$', views.pracownicy_lista,name="pracownicy_lista"),
    url(r'^pracownicy_edit/(?P<pk>\d+)/$', views.pracownicy_edit,{},name="pracownicy_edit"),
    url(r'^pracownicy_edit_barcode/(?P<pk>\d+)/$', views.pracownicy_edit_barcode,{},name="pracownicy_edit_barcode"),
    #url(r'^pracownicy_szablon/(?P<pk_prac>\d+)/$', views.pracownicy_szablon,{},name="pracownicy_szablon"),
    url(r'^pracownicy_szablon/(?P<dzial>[\w\s]+)/(?P<wariant>[\w\s-]+)/(?P<pk_prac>\d+)/$', views.pracownicy_szablon,{},name="pracownicy_szablon"),
    url(r'^pracownicy_usun_pobranie/(?P<pk_prac>\d+)/(?P<pk_pobr>\d+)/$', views.pracownicy_usun_pobranie,name="pracownicy_usun_pobranie"),
    url(r'^pracownicy_usun_pobranie_barcode/(?P<pk_prac>\d+)/(?P<pk_pobr>\d+)/$', views.pracownicy_usun_pobranie_barcode,name="pracownicy_usun_pobranie_barcode"),
    url(r'^pracownicy_view/(?P<pk>\d+)/$', views.pracownicy_view,{},name="pracownicy_view"),
    url(r'^potwierdz/(?P<pk>\d+)/$', views.potwierdz,{},name="potwierdz"),
    url(r'^potwierdz_barcode/(?P<pk>\d+)/$', views.potwierdz_barcode,{},name="potwierdz_barcode"),
    url(r'^login/$', views.login,name="login"),
    url(r'^awaiting/$', views.awaiting,name="awaiting"),
    url(r'^confirmed/$', views.confirmed,name="confirmed"),
    url(r'^sign_test/$', views.sign_test,name="sign_test"),

]
