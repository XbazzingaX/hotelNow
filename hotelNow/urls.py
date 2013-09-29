from django.conf.urls import patterns, include, url
from django.conf import settings

from hotel.views import HotelViewSet, TypeViewSet

from rest_framework import routers
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'Hotels',HotelViewSet)
router.register(r'Types',TypeViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Examples:
    # url(r'^$', 'hotelNow.views.home', name='home'),
    # url(r'^hotelNow/', include('hotelNow.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
