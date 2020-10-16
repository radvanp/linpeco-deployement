from django.conf.urls.defaults import patterns, include

urlpatterns = patterns('',
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/linpeco/css', 'show_indexes': True}),
    #(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/koprda/Work/Projects/LinPeCo/linpeco/css', 'show_indexes': True}),
)

urlpatterns = urlpatterns + patterns('app.views',
    (r'^today/', 'today'),
    (r'^total/', 'total'),
    (r'^year/', 'year'),
    (r'^month/', 'month'),
    (r'^day/',   'day'),
    (r'^event/', 'event'),
)

urlpatterns = urlpatterns + patterns('',
    (r'.*', 'django.views.generic.simple.redirect_to', {'url': '/today'}),
)
