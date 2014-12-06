from django.conf.urls import patterns, include, url
from django.contrib import admin

from tag.views import hello

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # all-auth
    # url(r'^accounts/', include('allauth.urls')),

    # test for hello
    url(r'^tag/get/$', hello),
)
