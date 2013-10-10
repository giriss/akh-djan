from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^lesson1/(?P<name>[a-zA-Z]+)/$', 'learn.views.lesson1', name='lesson1'),
    url(r'^lesson1/$', 'learn.views.lesson1')
)
