from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #media
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}),

    #Login
    url(r'^', include('apps.login.urls')),
    url(r'^', include('apps.usuario.urls')),
    url(r'^', include('apps.sir.urls')),


)

