"""linpeco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#doplnene
#from django.conf.urls.defaults import patterns, include
from django.conf.urls import url, include
#doplnene
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('today/', views.today, name='today'),
    path('day/', views.day, name='day'),
    path('year/', views.year, name='year'),
    path('total/', views.total, name='total'),
    path('month/', views.total, name='month'),
    path('event/', views.event, name='event'),
#    path('css/(?P<path>.*)$', ),
#    path('', views.index, name='index'),
#    path('css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/linpeco/css', 'show_indexes': True}),
]


#urlpatterns = patterns('',
#    (r'^admin/', include('django.contrib.admin.urls')),
#    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/linpeco/css', 'show_indexes': True}),
    #(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/koprda/Work/Projects/LinPeCo/linpeco/css', 'show_indexes': True}),
#)

#urlpatterns = urlpatterns + patterns('app.views',
#    (r'^today/', 'today'),
#    (r'^total/', 'total'),
#    (r'^year/', 'year'),
#    (r'^month/', 'month'),
#    (r'^day/',   'day'),
#    (r'^event/', 'event'),
#)

#urlpatterns = urlpatterns + patterns('',
#    (r'.*', 'django.views.generic.simple.redirect_to', {'url': '/today'}),
#)
