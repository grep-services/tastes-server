# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from main import views
"""
from rest_framework import routers

# for rest
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
"""
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # all-auth
    # url(r'^accounts/', include('allauth.urls')),

    # test
    # url(r'^image/get/$', views.get_image),
    url(r'^image/add/$', views.image_add),
    url(r'^image/tag/$', views.image_tag),
    url(r'^image/get/$', views.image_get),
    url(r'^image/list/$', views.image_list),
    url(r'^tag/list/$', views.tag_list),
    url(r'^test/$', views.test),
    url(r'^test/utf/$', views.utf_test),

    # rest
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

# for media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
