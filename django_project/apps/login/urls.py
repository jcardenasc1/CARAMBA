from django.conf.urls import patterns, include, url
from .views import LogOut,userlogin
from django.contrib.auth.views import password_reset, password_reset_done, \
    password_reset_confirm, password_reset_complete

urlpatterns = patterns('',
    url(r'^$',userlogin, name='login'),

    url(r'^cerrar/$' , LogOut, name='logout'),

    url(r'^reset/password_reset', password_reset,
        {'template_name':'registration/password_reset_form.html',
        'email_template_name': 'registration/password_reset_email.html'},
        name='password_reset'),
    url(r'^password_reset_done', password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),
)
